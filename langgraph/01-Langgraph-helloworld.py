from langgraph.graph import StateGraph
from langgraph.graph import START, END
from typing import TypedDict

class State(TypedDict):
    n: int
    
def is_even(state: State):
    print(state["n"])
    if state["n"] % 2 == 0:
        tstr = f"{state['n']} is Even number"
    else:
        tstr = f"{state['n']} is Odd number"
        
    print(tstr)
    return state

builder = StateGraph(State)

builder.add_node("EVEN_OR_ODD", is_even)
builder.add_edge(START, "EVEN_OR_ODD")
builder.add_edge("EVEN_OR_ODD", END)

graph = builder.compile()

response = graph.invoke({"n": 10})
print(f"Response :{response}")
