# messaging_agent.py

from langchain_core.messages import SystemMessage, AIMessage
from orchestrator import AgentState
from data import event_planning_data
import time

def communication_agent(state: AgentState, communication_model) -> AgentState:
    """Enhanced communication agent that intelligently selects communication channels."""
    messages = state["messages"]
    user_request = event_planning_data.get("user_request", "")
    invitation_content = event_planning_data.get("invitation_info", "")
    
    system_prompt = SystemMessage(content=f"""You are the Communication Agent.

Original request: "{user_request}"
Invitation content available: {invitation_content}

You have 2 tools: whatsapp_message (informal events) and email_message (formal events).
Read their docstrings and select the appropriate channel based on the event's formality.
- Casual events (birthdays): Use WhatsApp.
- Formal events (business meetings): Use Email.
- Mixed events (weddings): Use both.

Choose wisely. After sending, summarize the communication strategy.""")
    
    if event_planning_data.get("whatsapp_status") or event_planning_data.get("email_status"):
        summary = "📱 COMMUNICATION COMPLETED!"
        return {
            "messages": [AIMessage(content=summary)],
            "current_agent": "communication",
            "next_action": "end"
        }
    
    all_messages = [system_prompt] + list(messages)
    response = communication_model.invoke(all_messages)
    print("\n"+"📍 Current Agent: COMMUNICATION AGENT")
    print("-" * 40)
    print("\n"+"User wants to communicate messages/invitations. Finding the best tools to use...")
    time.sleep(1)
    print("Initializing tools...")
    time.sleep(1)
    return {
        "messages": [response],
        "current_agent": "communication", 
        "next_action": "tools" if response.tool_calls else "end"
    }
