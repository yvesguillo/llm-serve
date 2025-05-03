# LLM-Serve – Chat with your local IA

![LLM-Serve](images/llm-serve.avif)

**A beginner-friendly, ready-to-use local *LLM* Chat server with Open Web UI and Ollama.**

## Purpose

`llm-serve` is a plug-and-play development environment for experimenting with local LLMs using [Ollama](https://ollama.com/) and the excellent [Open Web UI](https://github.com/open-webui/open-webui). It lets you:

- Run a local LLM API (via Ollama).
- Access a friendly interface to chat (via Open Web UI).
- Easily switch models.
- Test LLM calls from Python.
- Learn Dockerized dev flows with minimal effort.

## Advantages

- **Self-hosted**: No API keys, no cloud dependency.
- **Modular**: Just two lightweight containers.
- **Beginner-friendly**: Clear folder structure, `.env` file support, and helpful logs.

## Typical Use Cases

- Learn about local LLMs.
- Experiment with open models.
- Test prompts and completions via CLI, UI or Python.
- Initially built to be used in tandem with [*Crawlect*](https://github.com/yvesguillo/crawlect) or similar developer tools.

## Getting Started

### 1. Clone this repo

```bash
git clone https://github.com/yvesguillo/llm-serve.git
cd llm-serve
```

### 2. (Optional) if using Windows *WSL*

```powershell
wsl -d Ubuntu
cd /mnt/c/path/to/your/local/repo/llm-serve
```

### 3. Start the containers

```bash
docker compose up -d --build
```

### 4. Pull Ollama models manually
To use *Ollama* or *Open WebUi* you need at least one pulled models.  
To do so:

```bash
docker exec -it ollama bash
ollama pull dolphin-phi # Or any model you may prefer. dolphin-phi is quite light, capable and perfect for testing.
```

### 5. Open Web UI
Visit: [http://localhost:3000](http://localhost:3000)

>⚠️ *Open WebUi can take several minutes to be reachable upon container initialization. Be patient.*

> ⚠️ You may need to **refresh Open Web UI** or **restart it** to detect newly pulled models:
> ```bash
> docker-compose restart openwebui
> ```

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

### Monitor usage (`[CTRL] + [C]` to exit)

```bash
docker stats -a
```

### Inspect containers & volumes

```bash
docker ps -a
docker volume ls
```

### Enter container shell (`exit` to… exit)

```bash
docker exec -it ollama bash
```

### Logs (`[CTRL] + [C]` to exit)

```bash
docker compose logs -f openwebui
```

## WSL (if using)

### Exit WSL

```bash
exit
wsl --shutdown
```

## Advanced Docker Cleanup

```bash
docker stop $(docker ps -aq)
docker rm -f $(docker ps -aq)
docker rmi $(docker images -aq)
docker system prune -a --volumes
```

## Status

- Stable for local dev use.
- Model pulls are *manual* for now.
