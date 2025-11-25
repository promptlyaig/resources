from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class State(TypedDict):
    n: int
    is_even: bool
    output: str

def initialize_state_defaults(state: dict):
    ret_state = {
        "n": state.get("n", 0),
        "is_even": False,
        "output": None
    }
    
    return ret_state

def is_even(state: State):
    if state["n"] % 2 == 0:
        state["is_even"] = True
    else:
        state["is_even"] = False
        
    return state

def build_output(state: State):
    if state['is_even']:
        tstr = f"{state['n']} is Even number"
    else:
        tstr = f"{state['n']} is Odd number"
        
    state["output"] = tstr
    return state


def build_graph():
    builder = StateGraph(State)
    
    builder.add_node("INITIALIZER", initialize_state_defaults)
    builder.add_node("EVEN_OR_ODD", is_even)
    builder.add_node("OUTPUT", build_output)

    builder.add_edge(START, "INITIALIZER")
    builder.add_edge("INITIALIZER", "EVEN_OR_ODD")
    builder.add_edge("EVEN_OR_ODD", "OUTPUT")
    builder.add_edge("OUTPUT", END)

    graph = builder.compile()

    return graph

graph = build_graph()


def main():
    data = {"n": 10}
    response = graph.invoke(data)
    print(f"Response :{response}")
    print(f"Output   :{response['output']}")
    print()
    
if __name__ == "__main__":
    main()
