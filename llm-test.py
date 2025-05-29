#! /usr/bin/env python3

"""
Example usage of Ollama Client for interacting with a local LLM.
Creates an instance of Ollama Client, sends a chat message,
and prints the response content.
"""

# Load Ollama utilities (run `pip install ollama` if not done yet).
from ollama import Client

# If The model returns special characters or emojis (believe me, it might), you may want to set *Python* to handle this with UTF-8.
import sys
import io

# UTF-8 settings.
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')


client = Client(host = 'http://localhost:11434')

try:
    response = client.chat(
        model = "smollm2:1.7b",
        messages = [
            {"role": "user", "content": "Hello there! Got a fun fact for me?"}
        ]
    )

    print(response.get("message", {}).get("content", "No response content"))

except Exception as error:
    print(f"Error during chat: {error}")