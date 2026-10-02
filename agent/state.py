
# like Shared Notebook
from typing import TypedDict


class AgentState(TypedDict):
    problem: str
    plan: str
    code: str
    test_input:str
    execution_result: str
    expected_output: str
    evaluation_result: str
    debug_feedback: str
    attempt_count: int