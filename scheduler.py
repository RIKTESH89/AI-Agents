# scheduler.py

from re import A
import time
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage
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
    
    if len(messages) >= 2 and isinstance(messages[-1], ToolMessage ):
        print("\n"+"scheduler_agent() called with state===========================================>>>>>>>>>>>>>>>>>>", messages[-2])
        user_input = input("Do you want to proceed with the scheduled plan?")
        user_prompt = HumanMessage(content=user_input)
        system_prompt = SystemMessage(content=f"""You are the Scheduler Agent for event planning. The user has answered to the question that he is satisfied with the plan. If he is not satisfied and he is giving some inputs, considering user's inputs, please provide the updated plan
                                      using the 6 tools: calendar, finance, health, weather, traffic, invite_people. If the user is satisfied then do not use tool call and just give output as Scheduling already completed.""")  
        all_messages = [system_prompt] + list(messages) + [user_prompt]
        response = scheduler_model.invoke(all_messages)
        print("\n"+"scheduler_agent() called with response===========================================>>>>>>>>>>>>>>>>>>", response)
        return {
            "messages": [response],
            "current_agent": "scheduler", 
            "next_action": "tools" if response.tool_calls else "communication"
        }
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
    event_planning_data["current_step"] = "scheduling_complete"
    print("\n"+"📍 Current Agent: SCHEDULER AGENT")
    print("-" * 40)
    print("\n"+"Planning your event now...")
    time.sleep(1)
    print("\n"+"I'm working on your request and bringing in my specialized tools to create the perfect plan for your event.")
    time.sleep(3)
    print("\n"+"Please hold on for a moment. Your event schedule is being put together!")
    time.sleep(2)
    return {
        "messages": [response],
        "current_agent": "scheduler",
        "next_action": "tools" if response.tool_calls else "communication"
    }
