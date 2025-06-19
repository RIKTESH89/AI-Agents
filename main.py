# main.py

import os
from functools import partial
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
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
GEMINI_API_KEY = "###" # IMPORTANT: Replace with your actual key
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

# model = ChatOllama(
#     base_url=OLLAMA_BASE_URL,
#     model=OLLAMA_MODEL,
#     temperature=0.1
# )

# Bind tools to models
scheduler_model = model.bind_tools(scheduler_tools)
communication_model = model.bind_tools(communication_tools)

# Partial function for agents to pass the model
scheduler_agent_with_model = partial(scheduler_agent, scheduler_model=scheduler_model)
communication_agent_with_model = partial(communication_agent, communication_model=communication_model)


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
    print("\n"+"========================================route afterscheduler agent entry point=======================================", messages)
    if messages and hasattr(messages[-1], 'tool_calls') and messages[-1].tool_calls and isinstance(messages[-1], AIMessage):
        return "scheduler_tools"
    # elif messages and hasattr(messages[-2], 'tool_calls') and messages[-2].tool_calls and isinstance(messages[-2], AIMessage) and isinstance(messages[-1], HumanMessage):
    #     user_input = input("Do you want to proceed with the scheduled plan?")
    #     state["messages"] = state["messages"]+[HumanMessage(content=user_input)]
    #     return "scheduler"
    # print("\n"+"========================================scheduler agent entry point=======================================", messages)
    return "communication"

def route_after_communication(state: AgentState) -> str:
    """Route from communication agent."""
    messages = state["messages"]
    if messages and hasattr(messages[-1], 'tool_calls') and messages[-1].tool_calls:
        return "communication_tools"
    return "end"

def route_after_scheduler_tools(state: AgentState) -> str:
    """Route after scheduler tools execution."""
    # Check if we have sufficient planning information
    tools_used = []
    for msg in state["messages"]:
        if isinstance(msg, ToolMessage):
            tools_used.append(msg.name if hasattr(msg, 'name') else 'unknown')
    
    # If we have at least some planning done, move to communication
    if len(tools_used) >= 2:
        return "communication"
    else:
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
    
    # Add agent nodes
    graph.add_node("orchestrator", orchestrator_agent)
    graph.add_node("scheduler", scheduler_agent_with_model)
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
            "communication": "communication",
            "scheduler": "scheduler"
        }
    )
    
    # graph.add_conditional_edges(
    #     "scheduler_tools",
    #     route_after_scheduler_tools,
    #     {
    #         "scheduler": "scheduler", 
    #         "communication": "communication"
    #     }
    # )
    
    graph.add_edge("scheduler_tools", "scheduler")
    
    graph.add_conditional_edges(
        "communication",
        route_after_communication, 
        {
            "communication_tools": "communication_tools",
            "end": END
        }
    )
    
    # graph.add_conditional_edges(
    #     "communication_tools",
    #     route_after_communication_tools,
    #     {
    #         "end": END
    #     }
    # )
    
    graph.add_edge("communication_tools", "communication")
    
    return graph.compile()

# ============================================================================
# UTILITY & MAIN EXECUTION
# ============================================================================

def print_messages(messages):
    if not messages: return
    for message in messages[-10:]: # Print last few messages for brevity
        if isinstance(message, AIMessage): print(f"\n🤖 AI: {message.content}")
        elif isinstance(message, ToolMessage): print(f"\n🛠️ TOOL RESULT: {message.name} -> {message.content}")
        elif isinstance(message, HumanMessage): print(f"\n👤 USER: {message.content}")

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

def run_event_planning_system():
    """Main function to run the multi-agent event planning system."""
    
    print("\n" + "="*80)
    print("🎉 MULTI-AGENT EVENT PLANNING SYSTEM (Powered by Gemini 2.0 Flash) 🎉")
    print("="*80)
    print("Welcome! I can help you plan events with my team of AI agents:")
    print("🎯 Orchestrator: Routes and coordinates requests")
    print("📅 Scheduler: Handles comprehensive event planning")
    print("📱 Communication: Sends invitations via WhatsApp & Email")
    print("="*80)
    
    # Create the graph
    app = create_event_planning_graph()
    
    while True:
        try:
            # Reset data for new planning session
            reset_planning_data()
            
            # Get user input
            user_input = input("\n👤 Describe the event you'd like to plan (or 'quit' to exit): ")
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
            
            # Run the graph
            final_state = None
            for step in app.stream(initial_state, stream_mode="values"):
                final_state = step
                if "messages" in step:
                    print_messages(step["messages"])
                    
                # Show current agent
                current_agent = step.get("current_agent", "unknown")
                # print(f"\n📍 Current Agent: {current_agent.upper()}")
                # print("-" * 40)
            
            # Show final summary
            print("\n" + "="*60)
            print("📋 EVENT PLANNING SUMMARY")
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

if __name__ == "__main__":
    run_event_planning_system()

