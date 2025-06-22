# scheduler.py

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from orchestrator import AgentState
from data import event_planning_data

def scheduler_agent(state: AgentState, scheduler_model) -> AgentState:
    """Enhanced scheduler agent that intelligently selects appropriate tools based on context."""
    messages = state["messages"]
    user_request = event_planning_data.get("user_request", "")
    
    system_prompt = SystemMessage(content=f"""You are the Scheduler Agent for event planning.

For the user request: "{user_request}"
Create scheduler content for the user request: {user_request}.

You have 6 tools: calendar, finance, health, weather, traffic, invite_people.
Read their docstrings to understand their use. Select ONLY the relevant tools for the specific event.
- Home birthday party: use calendar, finance, health, invite_people.
- Outdoor event: add weather.
- Venue-based event: add traffic.

Make sure to give the arguments for each tool in the correct format and if they are string based query, please elaborate on the query like creating invitation for birthday party.

Be smart and efficient. After using tools, summarize and indicate readiness for communication.""")
    
    if event_planning_data.get("current_step") == "scheduling_complete":
        return {
            "messages": [AIMessage(content="Scheduling already completed.")],
            "current_agent": "communication", 
            "next_action": "communication"
        }
    
    all_messages = [system_prompt] + list(messages)
    if user_request:
        all_messages.append(HumanMessage(content=f"Plan this event using relevant tools: {user_request}"))
    
    response = scheduler_model.invoke(all_messages)
    # event_planning_data["current_step"] = "scheduling_complete"
    
    return {
        "messages": [response],
        "current_agent": "scheduler",
        "next_action": "tools" if response.tool_calls else "communication"
    }
