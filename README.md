# LLM-Serve – Chat with your local AI

![LLM-Serve](images/llm-serve.avif)

**A beginner-friendly, ready-to-use local *LLM* AI Chat server runing *Open WebUI* and *Ollama*.**

## Purpose

`llm-serve` is a plug-and-play development environment for experimenting with local *LLMs* using the both excellent [*Ollama*](https://ollama.com/) and [*Open Web UI*](https://github.com/open-webui/open-webui).  
It lets you:

- Run a local LLM API (via Ollama).
- Access a friendly interface to chat (via Open Web UI).
- Easily switch models.
- Test LLM calls from Python.
- Learn Dockerized dev flows with minimal effort.

## Advantages

- **Self-hosted**: No internet conection or cloud dependency (once installed) and no API keys needed.
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

### 2. If using Windows *WSL* (Optional) 
Check [How to install Linux on Windows with WSL](https://learn.microsoft.com/en-us/windows/wsl/install) for more details.  
Alternatively, you can install [*Docker Desktop*](https://www.docker.com/products/docker-desktop/).

```powershell
wsl -d Ubuntu
cd /mnt/c/path/to/your/local/repo/llm-serve
```

### 3. Start the containers

```bash
docker compose up -d --build
```

### 4. Pull Ollama models manually
To use *Ollama* with *Open WebUI* you need at least one pulled models.  
*This project does not include any*.

- **Enter *Ollama* container and launch the bash**:
  ```bash
  docker exec -it ollama bash
  ```

- **List pulled models** (Optional):
  ```bash
  ollama list
  ```
  Purely informative, you can skip it if you already know what you have pulled. On first launch and since this project does not include models, this will return an empty list.

- **Pull a model**:
  ```bash
  ollama pull <model-name>
  ```
  Pull any model you may like! E.g.: `ollama pull smollm2:1.7b`.  
  ***smollm2*** is ultra light (88MB to 1.8GB!), capable and perfect for testing. Small enough to run on a *Raspberry Pi*!

- **Remove a pulled models** (Optional):
  ```bash
  ollama rm  <model-name>
  ```

- **Clean up unused data** (Optional):
  ```bash
  ollama prune
  ```
  This removes unused models and temporary build and cache files. It might be a good idea to use it time to time, especially if *Ollama* runs without restart during a long period of time.


### 5. Open Web UI
Visit: [http://localhost:3000](http://localhost:3000)

>⚠️ *Open WebUI may not be reachable for several minutes upon container initialization. Be patient.*

> ⚠️ You may need to **refresh Open WebUI** or **restart it** to detect newly pulled models, but usually **hard refreshing the browser** (`[CTRL]` + `[F5]`) do the trick:
> ```bash
> docker-compose restart openwebui
> ```

## Python Usage Example

```python
from ollama import Client
client = Client(host='http://localhost:11434') # By default, Ollama uses port 11434 so does LLM-Serve. Check the .env file.

response = client.chat(
    model='smollm2:1.7b', # Adapt with any of your pulled models.
    messages=[
        {"role": "user", "content": "I'm happy to chat with you! Can you tell me something fun you know about?"}
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

### Monitor usage (`[CTRL]` + `[C]` to exit)

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
docker exec -it <container-name> bash
```

### Display logs (`[CTRL]` + `[C]` to exit)

```bash
docker compose logs -f <container-name>
```

## WSL (if using)

### Exit WSL

```bash
exit
wsl --shutdown
```

## Docker radical Cleanup

```bash
docker stop $(docker ps -aq)
docker rm -f $(docker ps -aq)
docker rmi $(docker images -aq)
docker system prune -a --volumes
```

## Status

- Stable for local dev use.
- Model pulls are *manual* for now.  
  Considering implementing a custom UI container for *Ollam* to automatically pull a set of default or user-defined models on startup, as well as offering the standard *Ollama* command interface.
