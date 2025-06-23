# messaging_agent.py

from langchain_core.messages import SystemMessage, AIMessage
from orchestrator import AgentState
from data import event_planning_data

def communication_agent(state: AgentState, communication_model) -> AgentState:
    """
    Enhanced communication agent that intelligently drafts and sends invitations. Uses the 'invite_people' tool for drafting invitations and the 'whatsapp_message' tool for sending informal invitations via WhatsApp. For formal events, it uses the 'email_message' tool.
    """
    messages = state["messages"]
    user_request = event_planning_data.get("user_request", "")
    invitation_content = event_planning_data.get("invitation_info", "No invitation has been drafted yet.")
    
    # Updated system prompt to include the 'invite_people' tool.
    system_prompt = SystemMessage(content=f"""You are the Communication Agent. Your role is to handle all outgoing messages and invitations for the event.

Original user request: "{user_request}"
Current invitation content prepared by the scheduler: "{invitation_content}"

You have 3 tools at your disposal:
1.  **invite_people**: To generate or refine the text and details of an invitation. This should be your first step.
2.  **whatsapp_message**: To send informal invitations or messages (e.g., for casual birthdays).
3.  **email_message**: To send formal invitations or messages (e.g., for business meetings).

Your workflow is as follows:
1.  First, use the `invite_people` tool to generate the perfect invitation text based on the event details.
2.  Once you have the final invitation text, decide on the best channel. Use `whatsapp_message` for casual events and `email_message` for formal ones. For events like weddings, you might use both.
3.  Execute the sending tool(s) with the generated message.

After sending, summarize the communication actions taken. If messages have already been sent, simply state that communication is complete.""")
    
    # Check if communication tasks have already been completed in a previous step.
    if event_planning_data.get("whatsapp_status") or event_planning_data.get("email_status"):
        summary = "📱 COMMUNICATION COMPLETED: Invitations have already been sent."
        return {
            "messages": [AIMessage(content=summary)],
            "current_agent": "communication",
            "next_action": "end"
        }
    
    all_messages = [system_prompt] + list(messages)
    
    # Invoke the model to get the response, which may include tool calls.
    response = communication_model.invoke(all_messages)

    return {
        "messages": [response],
        "current_agent": "communication", 
        # If the model's response includes tool calls, the next action is 'tools', otherwise the process ends.
        "next_action": "tools" if response.tool_calls else "end"
    }
