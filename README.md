# LLM-Serve

**Chat Locally with Your AI Sidekick.**

![LLM-Serve](images/llm-serve.avif)

**Fire up your own local AI chat server in minutes – powered by [Ollama](https://ollama.com/) + [Open WebUI](https://github.com/open-webui/open-webui)**

`llm-serve` is a beginner-friendly, zero-API-keys-required playground for local LLMs. It sets up a private, Dockerized environment where you can:

- Run a local AI model (via Ollama)
- Chat with it through a sleek web interface (Open WebUI)
- Switch models like socks
- Test your prompts with Python
- Learn real-world Docker dev flows with no stress

## Why LLM-Serve?

- **No API keys. No cloud. No limits.** Just you and your local LLMs.
- **Runs anywhere.** Your laptop, dev server, or even a Raspberry Pi.
- **Super lightweight.** Just two containers: Ollama and Open WebUI.
- **Totally beginner-friendly.** Clean structure, `.env` support, clear logs, and cheat sheets galore.

## Use Cases

- Experiment with open-source LLMs offline.
- Explore local inference performance.
- Build LLM tools, agents, or workflows.
- Use it with [Crawlect](https://github.com/yvesguillo/crawlect) or similar dev projects.
- Just… play with cool AI stuff!

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yvesguillo/llm-serve.git
cd llm-serve
```

### 2. On Windows? Using **WSL**? Great! (Optional)

```powershell
wsl -d Ubuntu
cd /mnt/c/path/to/llm-serve
```

Or skip WSL and just use [Docker Desktop](https://www.docker.com/products/docker-desktop). Your choice.

### 3. Launch it

```bash
docker compose up -d --build
```

This spins up (`--build`) both containers in the background (`-d`).

### 4. Pull your first model manually

This project doesn’t include any models by default. You’ll need to pull one using `ollama`.

- Enter the Ollama container:

  ```bash
  docker exec -it ollama bash
  ```

- Pull a model (example: a tiny but mighty one):

  ```bash
  ollama pull smollm2:1.7b
  ```

  `smollm2` is fast, small (88MB to 1.8GB!), and even runs on a Raspberry Pi. Perfect for testing.

- Check what you’ve got (optional):

  ```bash
  ollama list
  ```

- Clean up the attic (optional):

  ```bash
  ollama prune
  ```

  Removes unused models and temp junk.

### 5. Open the UI

Fire up your browser and head to:

[http://localhost:3000](http://localhost:3000)

> ⚠️ *Open WebUI might take a minute or two to boot up. Be patient!*

If your newly pulled models aren’t showing up:

- Try a hard refresh *Open WebUI* page: `CTRL + F5`
- Or restart the UI service:

  ```bash
  docker compose restart openwebui
  ```

## Python Integration

Test your local LLM directly from Python:

```python
from ollama import Client
client = Client(host='http://localhost:11434')

response = client.chat(
    model='smollm2:1.7b',
    messages=[
        {"role": "user", "content": "Hello there! Got a fun fact for me?"}
    ]
)

print(response['message']['content'])
```

## Docker Quick Commands

### Start, stop, and restart containers

```bash
docker compose stop       # Pause
docker compose down       # Stop & remove
docker compose down -v    # Also nuke volumes
docker compose restart    # Refresh like a pro
```

## Docker Cheat Sheet

### System Info

```bash
docker info
```

### Real-time usage dashboard

```bash
docker stats -a
```

### Containers & volumes

```bash
docker ps -a
docker volume ls
```

### Shell access (to any container)

```bash
docker exec -it <container-name> bash
```

### Logs

```bash
docker compose logs -f <container-name>
```

### Nuclear Option (Cleanup All the Things)

Use at your own risk. This wipes containers, images, volumes — everything.

```bash
docker stop $(docker ps -aq)
docker rm -f $(docker ps -aq)
docker rmi $(docker images -aq)
docker system prune -a --volumes
```

## Exit WSL (if you're using it)

```bash
exit
wsl --shutdown
```

## Project Status

- Solid and stable for local LLM tinkering
- Model pulls are still manual for now

## Roadmap & Crazy Ideas

- Add a custom UI container to preload models and expose Ollama’s CLI via web
- Make it safe for remote use

Got ideas? Spot a bug? Wanna make this thing even cooler? Open an issue or shoot a PR — we’d love to hear from you!
