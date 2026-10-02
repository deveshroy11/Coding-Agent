import os 

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from agent.state import AgentState   #Check if this is making stateful agents

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash",
    google_api_key= os.environ["GOOGLE_API_KEY"],
)

def planner(state:AgentState) ->AgentState:
    problem=state["problem"]
    prompt = f"""
You are a coding problem planner.

Analyze the following programming problem and create a clear solution plan.

Problem:
{problem}

Include:
1. Main approach
2. Important observations
3. Algorithm steps
4. Time complexity
5. Space complexity
6. Important edge cases

Do NOT write code. Only provide the plan.
"""

    response = llm.invoke(prompt)
    state["plan"] = response.content[0]["text"]
    return state