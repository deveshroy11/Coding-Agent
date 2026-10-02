from agent.graph import graph


state = {
    "problem": "Given an array of integers, find the maximum element.",
    "plan": "",
    "code": "",
    "test_input": "5\n3 8 2 10 4\n",
    "execution_result": "",
    "expected_output": "10",
    "evaluation_result": "",
    "debug_feedback": "",
    "attempt_count":0
}


final_state = graph.invoke(state)


print("===== FINAL EVALUATION =====")
print(final_state["evaluation_result"])

print("\n===== FINAL CODE =====")
print(final_state["code"])

print("\n===== EXECUTION RESULT =====")
print(final_state["execution_result"])

print("\n===== DEBUG FEEDBACK =====")
print(final_state["debug_feedback"])