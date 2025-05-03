# UTF-8 settings.
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
from ollama import Client

# Connect to your local Ollama instance
client = Client(host='http://localhost:11434')  # or use env vars

# Send a simple prompt to the default model (make sure it's pulled)
response = client.chat(
    model='dolphin-phi',  # replace with any model you've pulled
    messages=[
        {"role": "user", "content": "Hello! This is a simple test message sent from *Python* to see if you can receive and respond to me. :-). By answering you are helping me to test my current project. Thank you very much!"}
    ]
)

print(response['message']['content'])

for model in client.list()['models']:
    print(model['name'])