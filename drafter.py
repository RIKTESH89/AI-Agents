from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage, SystemMessage
from langchain_core.tools import tool
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
import os
from typing import TypedDict, Annotated, List, Dict, Any, Sequence
# Changed from OllamaLLM to ChatOllama
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import json
import requests
from datetime import datetime

OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MODEL = "qwen3:8b"
OLLAMA_API_KEY = "your-ollama-key"

# Global variable to store document content
document_content = ""

class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

@tool
def update(content: str) -> str:
    """Updates the document with the provided content."""
    global document_content
    document_content = content
    return f"Document has been updated successfully! The current content is:\n{document_content}"

@tool
def save(filename: str) -> str:
    """Save the current document to a text file and finish the process.
    
    Args:
        filename: Name for the text file.
    """
    global document_content

    if not filename.endswith('.txt'):
        filename = f"{filename}.txt"

    try:
        with open(filename, 'w') as file:
            file.write(document_content)
        print(f"\n💾 Document has been saved to: {filename}")
        return f"Document has been saved successfully to '{filename}'."
    
    except Exception as e:
        return f"Error saving document: {str(e)}"

tools = [update, save]
tool_node = ToolNode(tools)

# Initialize the model with ChatOllama (supports tool binding)
model = ChatOllama(
    base_url=OLLAMA_BASE_URL,
    model=OLLAMA_MODEL,
)

# Bind tools to the model
model_with_tools = model.bind_tools(tools)

def our_agent(state: AgentState) -> AgentState:
    system_prompt = SystemMessage(content=f"""
    You are Drafter, a helpful writing assistant. You are going to help the user update and modify documents.
    
    - If the user wants to update or modify content, use the 'update' tool with the complete updated content.
    - If the user wants to save and finish, you need to use the 'save' tool.
    - Make sure to always show the current document state after modifications.
    
    The current document content is:{document_content}
    """)

    if not state["messages"]:
        user_input = "I'm ready to help you update a document. What would you like to create?"
        user_message = HumanMessage(content=user_input)

    else:
        user_input = input("\nWhat would you like to do with the document? ")
        print(f"\n👤 USER: {user_input}")
        user_message = HumanMessage(content=user_input)

    all_messages = [system_prompt] + list(state["messages"]) + [user_message]

    response = model.invoke(all_messages)

    print(f"\n🤖 AI: {response.content}")
    if hasattr(response, "tool_calls") and response.tool_calls:
        print(f"🔧 USING TOOLS: {[tc['name'] for tc in response.tool_calls]}")

    return {"messages": list(state["messages"]) + [user_message, response]}

    # return {"messages": [response]}

def should_continue(state: AgentState) -> str:
    """Determine if we should continue or end the conversation."""
    messages = state["messages"]
    
    if not messages:
        return "continue"
    
    # Check the most recent messages for save completion
    for message in reversed(messages):
        if (isinstance(message, ToolMessage) and 
            "saved" in message.content.lower() and
            "document" in message.content.lower()):
            return "end" # goes to the end edge which leads to the endpoint
    
    return "continue"

def print_messages(messages):
    """Function I made to print the messages in a more readable format"""
    if not messages:
        return
    
    for message in messages[-3:]:
        if isinstance(message, ToolMessage):
            print(f"\n🛠️ TOOL RESULT: {message.content}")

# Create the graph
graph = StateGraph(AgentState)

graph.add_node("agent", our_agent)
graph.add_node("tools", tool_node)

graph.set_entry_point("agent")

graph.add_edge("agent", "tools")

graph.add_conditional_edges(
    "tools",
    should_continue,
    {
        "continue": "agent",
        "end": END,
    },
)

app = graph.compile()

from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))

def run_document_agent():
    print("\n===== DRAFTER =====")
    print("Welcome! I'm Drafter, your document writing assistant.")
    print("I can help you create, update, and save documents.")
    print("Type 'quit', 'exit', 'done', or 'finish' to end the session.\n")
    
    state = {"messages": []}
    
    while True:
        try:
            # Get user input
            # user_input = input("👤 What would you like to do with the document? ")
            # print()  # Add spacing
            
            # if user_input.lower() in ['quit', 'exit', 'done', 'finish']:
            #     print("👋 Goodbye! Thanks for using Drafter!")
            #     break
            
            # # Add user message to state
            # user_message = HumanMessage(content=user_input)
            # state["messages"].append(user_message)
            
            # Run the graph with current state
            final_state = None
            for step in app.stream(state, stream_mode="values"):
                final_state = step
                if "messages" in step:
                    print_messages(step["messages"])
            
            # Update state with final results
            if final_state:
                state = final_state
            
            # Check if we should end (if save was called)
            should_end = should_continue(state)
            if should_end == "end":
                print("\n📝 Document processing completed!")
                break
                
        except KeyboardInterrupt:
            print("\n\n👋 Session interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            print("Let's try again...")
    
    print("\n===== DRAFTER FINISHED =====")

if __name__ == "__main__":
    run_document_agent()
