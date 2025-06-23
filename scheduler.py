# scheduler.py

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from orchestrator import AgentState
from data import event_planning_data

def scheduler_agent(state: AgentState, scheduler_model) -> AgentState:
    """
    Enhanced scheduler agent that intelligently selects appropriate tools based on context.
    This agent focuses on the logistics and planning aspects of the event.
    """
    messages = state["messages"]
    user_request = event_planning_data.get("user_request", "")
    
    # Updated system prompt reflecting the removal of the 'invite_people' tool.
    system_prompt = SystemMessage(content=f"""You are the Scheduler Agent, responsible for the logistical planning of events.

Your current task is to plan for the user's request: "{user_request}".

Your goal is to gather all necessary information to create a comprehensive event plan. You have 5 tools at your disposal:
- calendar: To check availability and schedule dates.
- finance: To manage budgets and estimate costs.
- health: To check for health/safety guidelines and dietary restrictions.
- weather: To get forecasts for outdoor events.
- traffic: To analyze transportation and parking for venues.

Read the docstrings of these tools to understand their specific functions. Select ONLY the relevant tools for the event.
- For a home birthday party, you should use calendar, finance, and health.
- For an outdoor festival, you would add the weather tool.
- For an event at a downtown venue, you must add the traffic tool.

Be smart and efficient. After using your tools, the plan will be passed to a human for review before any invitations are drafted or sent.
Provide arguments for each tool in the correct format. For string-based queries, be descriptive (e.g., "check calendar for weekend availability in late June for a birthday party").""")
    
    # If scheduling is already marked as complete, pass the turn.
    if event_planning_data.get("current_step") == "scheduling_complete":
        return {
            "messages": [AIMessage(content="Scheduling has already been completed and approved. Passing to communication agent.")],
            "current_agent": "communication", 
            "next_action": "communication"
        }
    
    all_messages = [system_prompt] + list(messages)
    if user_request:
        # Append a clear instruction for the model.
        all_messages.append(HumanMessage(content=f"Use your available tools to create a detailed plan for this event: {user_request}"))
    
    # Invoke the model to get the next step (which could be calling tools).
    response = scheduler_model.invoke(all_messages)
    
    return {
        "messages": [response],
        "current_agent": "scheduler",
        # The next action is 'tools' if the model decides to call tools, otherwise it proceeds to the next step in the graph (human_review).
        "next_action": "tools" if response.tool_calls else "human_review"
    }
