from agent.state import AgentState


def evaluator(state: AgentState) -> AgentState:
    state["attempt_count"]+=1

    actual = state["execution_result"]
    expected = state["expected_output"]

    if actual.strip() == f"SUCCESS:\n{expected}".strip():
        state["evaluation_result"] = "PASS"
    else:
        state["evaluation_result"] = "FAIL"

    return state