
# Coding Agent

An LLM-powered coding agent built with Python and Google's Gemini API. The project uses a modular architecture to plan, generate, execute, evaluate, and debug code.

## Overview

The Coding Agent is designed to break programming problems into manageable steps rather than relying on a single LLM response. Different components handle different stages of the problem-solving process.

## Architecture

The project is organized into specialized modules:

- **Planner (`planner.py`)** — Analyzes the programming problem and produces a structured solution plan, including the algorithm, complexity, and edge cases.
- **Coder (`coder.py`)** — Responsible for generating code based on the problem and solution plan.
- **Executor (`executor.py`)** — Handles code execution.
- **Evaluator (`evaluator.py`)** — Evaluates the generated solution.
- **Debugger (`debugger.py`)** — Helps identify and correct errors in generated code.
- **Graph (`graph.py`)** — Defines the workflow connecting the agent components.
- **State (`state.py`)** — Defines the shared state used to pass information between components.

### Workflow

```text
Programming Problem
        |
        v
     Planner
        |
        v
      Coder
        |
        v
     Executor
        |
        v
    Evaluator
        |
        v
  Debugger (if needed)
        |
        v
   Final Solution
```

The exact transitions and retry behavior depend on the workflow configured in `graph.py`.

## Tech Stack

- Python
- Google Gemini API
- LangChain
- LangGraph (if configured in the workflow)
- python-dotenv

## Project Structure

```text
Coding-Agent/
├── agent/
│   ├── coder.py
│   ├── debugger.py
│   ├── evaluator.py
│   ├── executor.py
│   ├── graph.py
│   ├── planner.py
│   └── state.py
├── executor_tester.py
├── test.py
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/deveshroy11/Coding-Agent.git
cd Coding-Agent
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

Install the required packages used by the project:

```bash
pip install langchain-google-genai langgraph python-dotenv
```

Add any additional dependencies required by the other modules.

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
```

Replace `your_google_api_key` with your Google AI API key.

**Security:** Never commit your `.env` file or expose your API key publicly.

### 5. Run the project

Run the appropriate entry-point script for your current implementation. For example, if `test.py` is your current test or demo entry point:

```bash
python test.py
```

## Key Features

- Modular agent architecture
- Structured solution planning
- LLM-based code generation
- Code execution and evaluation
- Debugging support
- Shared state across agent components

## Future Improvements

- Add structured output validation.
- Introduce execution timeouts and resource limits.
- Improve error handling and debugging retries.
- Add automated tests for individual components.
- Track execution traces and evaluation metrics.
- Support additional LLM providers.

## Author

**Devesh Roy**

GitHub: [@deveshroy11](https://github.com/deveshroy11)
