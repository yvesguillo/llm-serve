# llm-serve

**A beginner-friendly, ready-to-use local LLM server with Open Web UI and Ollama.**

## Purpose

`llm-serve` is a plug-and-play development environment for experimenting with local LLMs using [Ollama](https://ollama.com/) and the excellent [Open Web UI](https://github.com/open-webui/open-webui). It lets you:

- Run a local LLM API (via Ollama)
- Access a friendly interface to chat (via Open Web UI)
- Easily switch models
- Test LLM calls from Python
- Learn Dockerized dev flows with minimal effort

## Advantages

- **Self-hosted**: No API keys, no cloud dependency
- **Modular**: Just two lightweight containers
- **Beginner-friendly**: Clear folder structure, `.env` file support, and helpful logs
- **Compatible**: Works in WSL (Ubuntu), native Linux, macOS, and Windows

## Typical Use Cases

- Learn about local LLMs
- Experiment with open models before committing to OpenAI costs
- Test prompts and completions via CLI, UI or Python
- Use in tandem with Crawlect or similar developer tools

## Getting Started

### 1. Clone this repo

```bash
git clone https://github.com/your-user/llm-serve.git
cd llm-serve
```

### 2. (Optional) WSL Setup

**If using Windows with WSL:**

```powershell
wsl -d Ubuntu
cd /mnt/c/Users/YOUR_USER/projects/llm-serve
```

### 3. Configure environment

Edit `.env` or copy from the example:

```bash
cp .env.example .env
```

Adjust versions and ports if needed.


## Start the containers

```bash
docker compose up -d --build
```

Check container logs (optional):

```bash
docker compose logs -f
```

## Test and Use

### Open Web UI

Visit:

```
http://localhost:3000
```

> *First load can take up to a minute if models are still initializing.*

### Pull Ollama models manually

In a terminal:

```bash
docker exec -it ollama bash
ollama pull dolphin-phi
ollama pull mistral
```

List pulled models:

```bash
ollama list
```

> You may need to **refresh Open Web UI** or **restart it** to detect new models.

## Python Usage Example

```python
from ollama import Client
client = Client(host='http://localhost:11434')

response = client.chat(
    model='dolphin-phi',
    messages=[
        {"role": "user", "content": "Tell me a fun fact about Montres Jaquet Droz."}
    ]
)

print(response['message']['content'])
```

List installed models:

```python
print([model['name'] for model in client.list()['models']])
```

## Manage Containers

### Stop

```bash
docker compose stop
```

### Stop & remove containers

```bash
docker compose down
```

### Wipe volumes too

```bash
docker compose down -v
```

### Restart

```bash
docker compose restart
```

## Docker Toolbox

### System info

```bash
docker info
```

### Monitor usage

```bash
docker stats -a
```

### Inspect containers & volumes

```bash
docker ps -a
docker volume ls
```

### Enter container shell

```bash
docker exec -it ollama bash
```

### Logs

```bash
docker compose logs -f openwebui
```

## Advanced Cleanup

```bash
docker stop $(docker ps -aq)
docker rm -f $(docker ps -aq)
docker rmi $(docker images -aq)
docker system prune -a --volumes
```

## Status

- Stable for dev use
- Model pulls are *manual* for now
- PRs welcome!

(Yves Guillo)[https://yvesguillo.ch].