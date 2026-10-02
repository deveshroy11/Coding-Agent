# define the workflow

from langgraph.graph import StateGraph,START,END

from agent.state import AgentState
from agent.planner import planner
from agent.coder import coder
from agent.executor import execute_cpp
from agent.evaluator import evaluator
from agent.debugger import debugger

MAX_ATTEMPTS = 3

def executor_node(state:AgentState)-> AgentState:
    result = execute_cpp.invoke({
        "code": state["code"],
        "test_input":state["test_input"]
    })

    state["execution_result"] = result
    return state

def route_after_evaluation(state:AgentState):
    if state["evaluation_result"]== "PASS":
        return "end"

    if state["attempt_count"]>=MAX_ATTEMPTS:
        return "end"

    return "debugger"

graph_builder = StateGraph(AgentState)


# adding Node
graph_builder.add_node("planner", planner)
graph_builder.add_node("coder", coder)
graph_builder.add_node("executor", executor_node)
graph_builder.add_node("evaluator", evaluator)
graph_builder.add_node("debugger", debugger)

# Edges
graph_builder.add_edge(START,"planner")
graph_builder.add_edge("planner","coder")
graph_builder.add_edge("coder", "executor")
graph_builder.add_edge("executor", "evaluator")

graph_builder.add_conditional_edges(
    "evaluator",
    route_after_evaluation,
    {
        "end":END,
        "debugger":"debugger"
    }
)

graph_builder.add_edge("debugger","coder")

graph = graph_builder.compile()