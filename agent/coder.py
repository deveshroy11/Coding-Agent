import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from agent.state import AgentState


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=os.environ["GOOGLE_API_KEY"],
)


def coder(state: AgentState) -> AgentState:
    problem = state["problem"]
    plan = state["plan"]    # Taking from planner

    debug_feedback= state["debug_feedback"] 

    prompt = f"""
You are an expert C++ competitive programmer.

Solve the following programming problem using the provided plan.

Problem:
{problem}

Plan:
{plan}

Debug feedback from a previous failed attempt:
{debug_feedback}

Instructions:
- Write a complete C++17 solution.
- Follow the plan.
- If debug feedback is provided, fix the issues identified in it.
- Carefully follow the input/output format specified by the problem.
- Handle important edge cases.
- Return ONLY the C++ code.
- Do not include markdown code fences.
- Do not include explanations.
"""

    response = llm.invoke(prompt)

    state["code"] = response.content[0]["text"]

    return state