import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from agent.state import AgentState


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=os.environ["GOOGLE_API_KEY"],
)


def debugger(state: AgentState) -> AgentState:
    problem = state["problem"]
    code = state["code"]
    execution_result = state["execution_result"]
    expected_output = state["expected_output"]

    prompt = f"""
You are an expert C++ debugging agent.

Analyze the failed solution below and identify the reason it failed.

Problem:
{problem}

Current C++ code:
{code}

Execution result:
{execution_result}

Expected output:
{expected_output}

Your task:
1. Identify the bug or reason for failure.
2. Explain why it causes the incorrect result.
3. Explain what needs to be changed.

Do NOT write the corrected C++ code.
Do NOT provide a complete solution.
Only provide clear debugging feedback that another coding agent can use
to fix the code.
"""

    response = llm.invoke(prompt)

    state["debug_feedback"] = response.content[0]["text"]

    return state