# 🎨 Agent Silpi – AI Drawing Agent

**Build your own AI Drawing Agent from scratch using Python and Qwen3!**

Meet Silpi, a simple AI-powered drawing agent that converts natural-language instructions into actual drawings.

Just ask Silpi, *"Draw me a house"* — and watch it understand your request, select the right drawing tools, and create the drawing using Python.

This project is part of the **A for Agents** series on [Data Science With Keerthi](https://www.youtube.com/playlist?list=PLJ6x_qtPwLNU).

## 🚀 Features

- Understands natural-language drawing requests.
- Uses Qwen3:4B as the LLM brain.
- Supports tool calling through Ollama.
- Draws rectangles, circles, triangles and lines.
- Uses Pydantic for argument validation.
- Implements a simple agent loop using Python.
- Includes execution limits as guardrails.
- Uses conversation messages to maintain context during an agent run.

## 🧠 Agent Architecture

Silpi demonstrates six key components of an AI agent:

| Component | Implementation |
|---|---|
| Trigger | User's drawing request |
| Brain | Qwen3:4B |
| Memory | Messages list |
| Orchestration | Python agent loop |
| Guardrails | Pydantic validation and execution limits |
| Tools | Python drawing functions |

## 🛠️ Tech Stack

- Python
- Qwen3:4B
- Ollama
- HTTPX
- Pydantic
- Matplotlib
- uv

## 📁 Project Structure

```text
silpi/
│
├── src/
│   └── silpi/
│       ├── __init__.py
│       ├── agent.py
│       ├── tools.py
│       ├── tool_definitions.py
│       ├── schemas.py
│       └── system_prompt.txt
│
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
└── README.md
```

### File Responsibilities

- `agent.py` – Main agent loop, Ollama communication and orchestration.
- `tools.py` – Drawing functions, tool registry and execution.
- `tool_definitions.py` – Tool descriptions and JSON schemas provided to the LLM.
- `schemas.py` – Pydantic models for validating tool arguments.
- `system_prompt.txt` – Instructions that define Silpi's behaviour.

## ⚙️ Getting Started

### Prerequisites

Make sure you have installed:

- [Python](https://www.python.org/)
- [uv](https://docs.astral.sh/uv/)
- [Ollama](https://ollama.com/)

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd a-for-agents/episode-04-agent-silpi
```

### 2. Install dependencies using uv

Install all project dependencies and create the virtual environment automatically:

```bash
uv sync
```

This uses `pyproject.toml` and `uv.lock` to install the required packages.

### 3. Download the Qwen3 model

Pull Qwen3:4B using Ollama:

```bash
ollama pull qwen3:4b
```

Make sure Ollama is running locally before executing Silpi.

### 4. Run Silpi

From the project root directory:

```bash
uv run python src/silpi/agent.py
```

Enter your drawing request when prompted!

## 🏡 Example Prompts

Try asking Silpi:

- Draw me a house.
- Draw a blue circle.
- Draw a red triangle.
- Draw a house with a circular sun and a rectangular door.

## 🎯 Learning Outcomes

By building this project, you'll understand:

- How an LLM interacts with external tools.
- How tool calling works.
- How to build a simple agent loop.
- How to validate LLM-generated arguments.
- How the core components of an AI agent work together.

## 📺 YouTube Tutorial

Watch the complete hands-on tutorial on **Data Science With Keerthi**.

🎬 [Build Agent Silpi – Drawing Agent from Scratch](https://youtu.be/U6asXqaeuGc)

## ❤️ About the Project

Silpi is a beginner-friendly project designed to demonstrate how to build an AI agent without relying on agent frameworks like LangChain or LangGraph.

**Understand the fundamentals. Build from scratch. Learn by doing!**

If you find this project useful, consider giving the repository a ⭐.