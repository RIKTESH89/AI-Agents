# main.py

import os
import asyncio
from functools import partial
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
# Import agents, tools, and data from other files
from data import event_planning_data, WEATHER_DATA
from tools import calendar, finance, health, weather, traffic, invite_people, whatsapp_message, email_message
from orchestrator import orchestrator_agent, AgentState
from scheduler import scheduler_agent
from messaging_agent import communication_agent

# ============================================================================
# CONFIGURATION
# ============================================================================
GEMINI_API_KEY = "####" # IMPORTANT: Replace with your actual key
GEMINI_MODEL = "gemini-1.5-flash"

OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MODEL = "hermes3:8b"

if GEMINI_API_KEY == "YOUR_GEMINI_API_KEY" or not GEMINI_API_KEY:
    raise ValueError("Please replace 'YOUR_GEMINI_API_KEY' with your actual Google Generative AI API key.")

# ============================================================================
# TOOLS & MODELS SETUP
# ============================================================================

# Tool lists
scheduler_tools = [calendar, finance, health, weather, traffic, invite_people]
communication_tools = [whatsapp_message, email_message]

# Tool nodes
scheduler_tool_node = ToolNode(scheduler_tools)
communication_tool_node = ToolNode(communication_tools)

# Model initialization
model = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    google_api_key=GEMINI_API_KEY,
    temperature=0.1,
)

# Bind tools to models
scheduler_model = model.bind_tools(scheduler_tools)
communication_model = model.bind_tools(communication_tools)

# ============================================================================
# ASYNC AGENT WRAPPERS
# ============================================================================

async def async_scheduler_agent(state: AgentState, scheduler_model=None) -> AgentState:
    """Async wrapper for scheduler agent."""
    # If your scheduler_agent is already async, just call it directly
    # If not, run it in a thread pool
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, scheduler_agent, state, scheduler_model)

async def async_communication_agent(state: AgentState, communication_model=None) -> AgentState:
    """Async wrapper for communication agent."""
    # If your communication_agent is already async, just call it directly
    # If not, run it in a thread pool
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, communication_agent, state, communication_model)

async def async_orchestrator_agent(state: AgentState) -> AgentState:
    """Async wrapper for orchestrator agent."""
    # If your orchestrator_agent is already async, just call it directly
    # If not, run it in a thread pool
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, orchestrator_agent, state)

# Partial function for agents to pass the model
scheduler_agent_with_model = partial(async_scheduler_agent, scheduler_model=scheduler_model)
communication_agent_with_model = partial(async_communication_agent, communication_model=communication_model)

# ============================================================================
# HUMAN-IN-THE-LOOP NODE
# ============================================================================

async def human_review_node(state: AgentState) -> AgentState:
    """
    Human-in-the-loop node that waits for user input after scheduler execution.
    This node will be interrupted before execution to allow human input.
    """
    messages = state["messages"]
    
    # Get the last human message (which contains the user's decision)
    last_human_msg = None
    for msg in reversed(messages):
        if isinstance(msg, HumanMessage):
            last_human_msg = msg
            break
    
    if last_human_msg:
        user_input = last_human_msg.content.lower().strip()
        
        # Parse user input to determine next action
        if any(keyword in user_input for keyword in ['proceed', 'continue', 'go ahead', 'yes', 'looks good', 'approve']):
            state["next_action"] = "communication"
            state["current_agent"] = "human_review"
            event_planning_data["current_step"] = "scheduling_complete"
            
            # Add a system message to indicate approval
            state["messages"].append(AIMessage(content="✅ Plan approved by user. Proceeding to send invitations."))
        
        elif any(keyword in user_input for keyword in ['modify', 'change', 'update', 'revise', 'reschedule']):
            state["next_action"] = "scheduler"
            state["current_agent"] = "human_review"
            # Add a system message with the modification request
            state["messages"].append(AIMessage(content=f"🔄 User requested modifications: {last_human_msg.content}. Returning to scheduler for updates."))
        
        else:
            # Default to asking for clarification
            state["next_action"] = "communication"  # Default to proceeding
            state["current_agent"] = "human_review"
            state["messages"].append(AIMessage(content="✅ Proceeding with the current plan."))
    
    return state

# ============================================================================
# CONDITIONAL ROUTING
# ============================================================================

def route_after_orchestrator(state: AgentState) -> str:
    """Route from orchestrator to the appropriate agent."""
    next_action = state.get("next_action", "scheduler")
    return next_action

def route_after_scheduler(state: AgentState) -> str:
    """Route from scheduler agent."""
    messages = state["messages"]
    
    if messages and hasattr(messages[-1], 'tool_calls') and messages[-1].tool_calls and isinstance(messages[-1], AIMessage):
        return "scheduler_tools"
    
    # After scheduler completes its work, always go to human review
    return "human_review"

def route_after_human_review(state: AgentState) -> str:
    """Route from human review node based on user decision."""
    next_action = state.get("next_action", "communication")
    
    if next_action == "scheduler":
        return "scheduler"
    else:
        return "communication"

def route_after_communication(state: AgentState) -> str:
    """Route from communication agent."""
    messages = state["messages"]
    if messages and hasattr(messages[-1], 'tool_calls') and messages[-1].tool_calls:
        return "communication_tools"
    return "end"

def route_after_scheduler_tools(state: AgentState) -> str:
    """Route after scheduler tools execution."""
    # After tools execution, go back to scheduler for processing
    return "scheduler"

def route_after_communication_tools(state: AgentState) -> str:
    """Route after communication tools execution."""
    return "end"

# ============================================================================
# GRAPH CONSTRUCTION
# ============================================================================

def create_event_planning_graph():
    """Create the multi-agent event planning graph."""
    
    # Create the graph
    graph = StateGraph(AgentState)
    
    # Add agent nodes (now async)
    graph.add_node("orchestrator", async_orchestrator_agent)
    graph.add_node("scheduler", scheduler_agent_with_model)
    graph.add_node("human_review", human_review_node)
    graph.add_node("communication", communication_agent_with_model)
    
    # Add tool nodes
    graph.add_node("scheduler_tools", scheduler_tool_node)
    graph.add_node("communication_tools", communication_tool_node)
    
    # Set entry point
    graph.set_entry_point("orchestrator")
    
    # Add conditional edges
    graph.add_conditional_edges(
        "orchestrator",
        route_after_orchestrator,
        {
            "scheduler": "scheduler",
            "communication": "communication"
        }
    )
    
    graph.add_conditional_edges(
        "scheduler", 
        route_after_scheduler,
        {
            "scheduler_tools": "scheduler_tools",
            "human_review": "human_review"
        }
    )
    
    graph.add_edge("scheduler_tools", "scheduler")
    
    # Add human review routing
    graph.add_conditional_edges(
        "human_review",
        route_after_human_review,
        {
            "scheduler": "scheduler",
            "communication": "communication"
        }
    )
    
    graph.add_conditional_edges(
        "communication",
        route_after_communication, 
        {
            "communication_tools": "communication_tools",
            "end": END
        }
    )
    
    graph.add_edge("communication_tools", "communication")
    
    memory = MemorySaver()
    
    # Interrupt before human_review to allow for user input
    return graph.compile(interrupt_before=["human_review"], checkpointer=memory)

# ============================================================================
# UTILITY FUNCTIONS FOR FORMATTING
# ============================================================================

def get_visual_length(text: str) -> int:
    """
    Calculates the visual length of a string in a terminal, accounting for common emojis
    that are often double-width. This is a heuristic and may not be perfect for all
    characters or terminal fonts.
    """
    visual_len = 0
    for char in text:
        # These Unicode ranges cover many common emojis. We assume they are double-width.
        if ('\u2600' <= char <= '\u27BF' or          # Miscellaneous Symbols
            '\U0001F300' <= char <= '\U0001F5FF' or  # Misc Symbols and Pictographs
            '\U0001F600' <= char <= '\U0001F64F' or  # Emoticons
            '\U0001F680' <= char <= '\U0001F6FF' or  # Transport and Map Symbols
            '\U0001F900' <= char <= '\U0001F9FF'):   # Supplemental Symbols and Pictographs
            visual_len += 2
        else:
            visual_len += 1
    return visual_len

# ============================================================================
# ASYNC EVENT STREAMING HANDLERS
# ============================================================================

async def handle_stream_event(event):
    """Handle individual stream events from astream_events."""
    event_type = event.get("event")
    name = event.get("name", "")
    data = event.get("data", {})
    
    if event_type == "on_chain_start":
        if name == "orchestrator":
            print(f"\n🎯 Orchestrator started...")
        elif name == "scheduler":  
            print(f"\n📅 Scheduler started...")
        elif name == "communication":
            print(f"\n📱 Communication agent started...")
        elif name == "human_review":
            print(f"\n👤 Human review required...")
            
    elif event_type == "on_chain_end":
        if name == "orchestrator":
            print(f"✅ Orchestrator completed")
        elif name == "scheduler":
            print(f"✅ Scheduler completed")
        elif name == "communication":
            print(f"✅ Communication completed")
        elif name == "human_review":
            print(f"✅ Human review completed")
            
    elif event_type == "on_chain_stream":
        # Handle streaming outputs from agents
        if "messages" in data:
            messages = data["messages"]
            if messages:
                last_msg = messages[-1]
                if isinstance(last_msg, AIMessage) and last_msg.content:
                    print(f"\n� {name.upper()}: {last_msg.content}")
                elif isinstance(last_msg, ToolMessage):
                    print(f"\n🛠️ TOOL RESULT ({last_msg.name}):")
                    print(f"📄 {last_msg.content}")
                    print("-" * 50)
                    
    elif event_type == "on_tool_start":
        tool_name = name
        tool_input = data.get("input", {})

        print(f"\n🔧 Using tool: {tool_name}")

        if not isinstance(tool_input, dict) or not tool_input:
            print(f"   Input: {tool_input}")
            return

        # --- Custom sentence formatting for tool inputs ---
        sentence = ""
        try:
            if tool_name == "finance":
                amount = tool_input.get('amount')
                query = tool_input.get('query', 'a request')
                # Clean up the query for a more natural sentence
                task_description = query.lower().replace('estimate budget for', '').strip()
                if amount:
                    sentence = f"Given amount ${amount}, estimating budget for {task_description}."
                else:
                    sentence = f"Estimating budget for {task_description}."
            
            elif tool_name == "calendar":
                query = tool_input.get('query', 'availability')
                sentence = f"Checking calendar for: \"{query}\"."

            elif tool_name == "health":
                query = tool_input.get('query', 'a health concern')
                sentence = f"Checking health & safety guidelines for: \"{query}\"."
            
            elif tool_name == "weather":
                query = tool_input.get('query', 'a location and date')
                sentence = f"Fetching weather forecast for: \"{query}\"."

            elif tool_name == "traffic":
                query = tool_input.get('query', 'a route')
                sentence = f"Checking traffic conditions for: \"{query}\"."

            elif tool_name == "invite_people":
                query = tool_input.get('query', 'an event')
                sentence = f"Preparing invitations for: \"{query}\"."

            elif tool_name == "whatsapp_message":
                recipient = tool_input.get('recipient', 'a recipient')
                message = tool_input.get('message', '')
                sentence = f"Sending WhatsApp to {recipient}: \"{message[:40]}...\""

            elif tool_name == "email_message":
                recipient = tool_input.get('recipient', 'a recipient')
                subject = tool_input.get('subject', 'a subject')
                sentence = f"Sending email to {recipient} with subject: \"{subject}\"."
        except Exception:
             # If formatting fails, sentence will be empty and it will fall back.
             sentence = ""

        # --- Print the formatted sentence or fall back to dictionary view ---
        if sentence:
            print(f"   Task: {sentence}")
        else:
            print("   Input:")
            try:
                max_key_len = max(len(k) for k in tool_input.keys()) if tool_input else 0
                for key, value in tool_input.items():
                    print(f"     {key:<{max_key_len}} : {value}")
            except Exception:
                 print(f"     {str(tool_input)}")
        
    elif event_type == "on_tool_end":
        tool_name = name
        output = data.get("output", "")
        
        # Extract content from the output if it's a message object
        content = ""
        if hasattr(output, 'content'):
            content = output.content
        elif isinstance(output, dict) and 'content' in output:
            content = output['content']
        elif isinstance(output, str):
            content = output
        else:
            content = str(output)
        
        # Display tool output with beautiful formatting
        print(f"\n✅ Tool completed: {tool_name}")
        
        if content:
            print(f"\n╭{'─' * 60}╮")
            
            # --- HEADER ---
            titles = {
                "finance": " 💰 BUDGET ANALYSIS",
                "calendar": " 📅 CALENDAR AVAILABILITY",
                "health": " 🏥 HEALTH & SAFETY GUIDELINES",
                "weather": " 🌤️  WEATHER FORECAST",
                "traffic": " 🚗 TRAFFIC INFORMATION",
                "invite_people": " 👥 INVITATION DETAILS",
                "whatsapp_message": " 📱 WHATSAPP STATUS",
                "email_message": " 📧 EMAIL STATUS",
            }
            title_text = titles.get(tool_name, f" 🔧 {tool_name.upper()} RESULT")
            
            # Calculate padding based on visual length
            padding = 60 - get_visual_length(title_text)
            print(f"│{title_text}{' ' * max(0, padding)}│")
            
            print(f"├{'─' * 60}┤")
            
            # --- CONTENT ---
            content_lines = content.split('\n')
            for line in content_lines:
                # If line is short enough, print with padding
                if get_visual_length(line) <= 58:
                    padding = 58 - get_visual_length(line)
                    print(f"│ {line}{' ' * max(0, padding)} │")
                else:
                    # Wrap long lines based on visual length
                    words = line.split(' ')
                    current_line = ""
                    current_visual_len = 0
                    for word in words:
                        word_visual_len = get_visual_length(word)
                        
                        # Handle case where a single word is longer than the line
                        if word_visual_len > 58:
                            if current_line: # Print any existing line content first
                                padding = 58 - current_visual_len
                                print(f"│ {current_line}{' ' * max(0, padding)} │")
                                current_line = ""
                                current_visual_len = 0
                            
                            # Break the long word itself character by character
                            temp_word = ""
                            temp_len = 0
                            for char in word:
                                char_len = get_visual_length(char)
                                if temp_len + char_len > 58:
                                    padding = 58 - temp_len
                                    print(f"│ {temp_word}{' ' * max(0, padding)} │")
                                    temp_word = char
                                    temp_len = char_len
                                else:
                                    temp_word += char
                                    temp_len += char_len
                            current_line = temp_word # The remainder becomes the new current_line
                            current_visual_len = temp_len
                            continue

                        space_len = 1 if current_line else 0
                        if current_visual_len + space_len + word_visual_len > 58 and current_line:
                            padding = 58 - current_visual_len
                            print(f"│ {current_line}{' ' * max(0, padding)} │")
                            current_line = word
                            current_visual_len = word_visual_len
                        else:
                            current_line += (' ' if current_line else '') + word
                            current_visual_len += space_len + word_visual_len
                    
                    # Print the last remaining line
                    if current_line:
                        padding = 58 - current_visual_len
                        print(f"│ {current_line}{' ' * max(0, padding)} │")
            
            print(f"╰{'─' * 60}╯")


async def stream_graph_execution(app, initial_state, thread):
    """Stream graph execution using astream_events."""
    print(f"🚀 Starting event stream...")
    
    async for event in app.astream_events(initial_state, thread, version="v1"):
        await handle_stream_event(event)
        
        # Check if we're at an interrupt point
        current_state = app.get_state(thread)
        if current_state.next and current_state.next[0] == 'human_review':
            print(f"\n⏸️ Stream paused for human review")
            break
    
    return app.get_state(thread)

async def continue_after_human_input(app, thread, user_decision):
    """Continue streaming after human input."""
    # Update state with user decision
    app.update_state(thread, {"messages": [HumanMessage(content=user_decision)]})
    
    print(f"🔄 Resuming stream after user input...")
    
    # Continue streaming
    async for event in app.astream_events(None, thread, version="v1"):
        await handle_stream_event(event)

# ============================================================================
# UTILITY & MAIN EXECUTION
# ============================================================================

def print_messages(messages):
    if not messages: return
    for message in messages[-3:]: # Print last few messages for brevity
        if isinstance(message, AIMessage): 
            print(f"\n🤖 AI: {message.content}")
        elif isinstance(message, ToolMessage): 
            print(f"\n🛠️ TOOL RESULT: {message.name} -> {message.content[:100]}...")
        elif isinstance(message, HumanMessage): 
            print(f"\n👤 USER: {message.content}")

def reset_planning_data():
    """Reset the global planning data for a new session."""
    global event_planning_data
    event_planning_data = {
        "user_request": "",
        "calendar_info": "",
        "finance_info": "",
        "health_info": "",
        "weather_info": "",
        "traffic_info": "",
        "invitation_info": "",
        "whatsapp_status": "",
        "email_status": "",
        "current_step": "start"
    }

def display_current_plan():
    """Display the current planning information for user review."""
    print("\n" + "="*60)
    print("📋 CURRENT PLAN SUMMARY")
    print("="*60)
    
    if event_planning_data["calendar_info"]:
        print(f"📅 Calendar: {event_planning_data['calendar_info']}")
    if event_planning_data["finance_info"]:
        print(f"💰 Finance: {event_planning_data['finance_info']}")
    if event_planning_data["health_info"]:
        print(f"🏥 Health: {event_planning_data['health_info']}")
    if event_planning_data["weather_info"]:
        print(f"🌤️ Weather: {event_planning_data['weather_info']}")
    if event_planning_data["traffic_info"]:
        print(f"🚗 Traffic: {event_planning_data['traffic_info']}")
    if event_planning_data["invitation_info"]:
        print(f"👥 Invitations: {event_planning_data['invitation_info']}")
    
    print("="*60)

async def get_user_input_async(prompt):
    """Get user input asynchronously."""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, input, prompt)

async def run_event_planning_system():
    """Main async function to run the multi-agent event planning system."""
    
    print("\n" + "="*80)
    print("🎉 ASYNC MULTI-AGENT EVENT PLANNING SYSTEM (with astream_events) 🎉")
    print("="*80)
    print("Welcome! I can help you plan events with my team of AI agents:")
    print("🎯 Orchestrator: Routes and coordinates requests")
    print("📅 Scheduler: Handles comprehensive event planning")
    print("👤 Human Review: You review and approve the plan")
    print("📱 Communication: Sends invitations via WhatsApp & Email")
    print("="*80)
    
    # Create the graph
    app = create_event_planning_graph()
    
    while True:
        try:
            # Reset data for new planning session
            reset_planning_data()
            
            # Get user input
            user_input = await get_user_input_async("\n👤 Describe the event you'd like to plan (or 'quit' to exit): ")
            print()
            
            if user_input.lower() in ['quit', 'exit', 'done', 'finish']:
                print("👋 Thank you for using the Multi-Agent Event Planning System!")
                break
            
            # Initial state
            initial_state = {
                "messages": [HumanMessage(content=user_input)],
                "current_agent": "orchestrator",
                "next_action": "scheduler"
            }
            
            print(f"🚀 Processing request: '{user_input}'")
            print("-" * 60)
            
            # Run the graph with astream_events
            thread = {"configurable": {"thread_id": "123"}}
            
            # Stream until we hit the interrupt (human_review)
            state = await stream_graph_execution(app, initial_state, thread)
            
            # Handle human review loop
            while app.get_state(thread).next and app.get_state(thread).next[0] == 'human_review':
                # Display current plan for review
                display_current_plan()
                
                print("\n🤔 HUMAN REVIEW REQUIRED")
                print("Please review the plan above and choose your action:")
                print("• Type 'proceed', 'continue', 'yes', or 'approve' to send invitations")
                print("• Type 'modify', 'change', or describe what you want to update")
                print("• Type specific changes you want to make")
                
                user_decision = await get_user_input_async("\n👤 Your decision: ")
                print()
                
                if user_decision.lower().strip() in ['quit', 'exit', 'cancel']:
                    print("❌ Event planning cancelled.")
                    break
                
                # Continue execution with user decision
                await continue_after_human_input(app, thread, user_decision)
                
                # Check if we're still at human review or if execution completed
                current_state = app.get_state(thread)
                if not (current_state.next and current_state.next[0] == 'human_review'):
                    break
            
            # Show final summary
            print("\n" + "="*60)
            print("📋 FINAL EVENT PLANNING SUMMARY")
            print("="*60)
            
            if event_planning_data["calendar_info"]:
                print(f"📅 Calendar: {event_planning_data['calendar_info'][:100]}...")
            if event_planning_data["finance_info"]:
                print(f"💰 Finance: {event_planning_data['finance_info'][:100]}...")
            if event_planning_data["weather_info"]:
                print(f"🌤️ Weather: {event_planning_data['weather_info'][:100]}...")
            if event_planning_data["whatsapp_status"]:
                print(f"📱 WhatsApp: Sent successfully!")
            if event_planning_data["email_status"]:
                print(f"📧 Email: Sent successfully!")
                
            print("\n✅ Event planning completed successfully!")
            print("="*60)
            
        except KeyboardInterrupt:
            print("\n\n👋 Session interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            print("Let's try again...")

def main():
    """Entry point that runs the async event loop."""
    try:
        asyncio.run(run_event_planning_system())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")

if __name__ == "__main__":
    main()
