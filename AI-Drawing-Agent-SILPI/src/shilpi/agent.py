import httpx
import json

from tools import execute_tool, reset_canvas, show_drawing
from tool_definitions import TOOLS

# Load system prompt
with open("system_prompt.txt", "r", encoding="utf-8") as file:
    SYSTEM_PROMPT = file.read()

#Gaurdrails
MAX_ITERATIONS = 5
MAX_TOOL_CALLS = 12

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3:4b"

def agent_silpi(user_request):

    url = "http://localhost:11434/api/chat"

    payload = {
        "model": "qwen3:4b",
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_request
            }
        ],
        "stream": False
    }

    response = httpx.post(url, json=payload, timeout=120)
    response.raise_for_status()

    result = response.json()
    return result["message"]["content"]


def agent_loop(user_request: str):

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_request}
    ]

    tool_count = 0

    for iteration in range(MAX_ITERATIONS):

        payload = {
            "model": MODEL,
            "messages": messages,
            "tools": TOOLS,
            "think": False,
            "stream": False
        }

        response = httpx.post(
            OLLAMA_URL,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        result = response.json()
        assistant_message = result["message"]

        messages.append(assistant_message)

        tool_calls = assistant_message.get("tool_calls", [])

        # No more tool calls: agent has finished
        if not tool_calls:
            print("Silpi:", assistant_message.get("content", ""))
            return

        # Execute requested tools
        for tool_call in tool_calls:

            if tool_count >= MAX_TOOL_CALLS:
                print("Maximum tool calls reached.")
                return

            function_name = tool_call["function"]["name"]

            tool_result = execute_tool(tool_call)

            print(function_name, ":", tool_result)

            messages.append({
                "role": "tool",
                "tool_name": function_name,
                "content": tool_result
            })

            tool_count += 1

    print("Maximum iterations reached.")


if __name__ == "__main__":

    reset_canvas()

    try:
        request = input("What should Silpi draw? ")
        agent_loop(request)

    except KeyboardInterrupt:
        print("Silpi stopped.")

    finally:
        show_drawing()