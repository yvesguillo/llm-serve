# llm-serve
2025.05.03 01:42

Generated with Crawlect.

## Files:

### .env.example  
`..\llm-serve\.env.example`

```bash
# Exposed service ports.

OLLAMA_EXPOSED_PORT = 11434
OPENWEBUI_EXPOSED_PORT = 3000


# Facing internal service ports.

OLLAMA_INTERNAL_PORT = 11434
OPENWEBUI_INTERNAL_PORT = 8080
```
### .gitignore  
`..\llm-serve\.gitignore`

```gitignore
# Docker volumes
ollama_models/
openwebui_data/

# Sensitive data
.env
```
### LICENSE  
`..\llm-serve\LICENSE`


### docker-compose.yml  
`..\llm-serve\docker-compose.yml`

```yaml
services:
  ollama:
    env_file: .env
    image: ollama/ollama:latest
    container_name: ollama
    ports:
      - "${OLLAMA_EXPOSED_PORT}:${OLLAMA_INTERNAL_PORT}"
    volumes:
      - ./ollama_models:/root/.ollama
    environment:
      - OLLAMA_HOST=0.0.0.0
    healthcheck:
      test: ["CMD", "ollama", "list"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 10s
    restart: unless-stopped

  openwebui:
    env_file: .env
    image: ghcr.io/open-webui/open-webui:main
    container_name: openwebui
    ports:
      - "${OPENWEBUI_EXPOSED_PORT}:${OPENWEBUI_INTERNAL_PORT}"
    depends_on:
      ollama:
        condition: service_healthy
    environment:
      - "OLLAMA_API_URL=http://ollama:${OLLAMA_EXPOSED_PORT}"
    volumes:
      - ./openwebui_data:/app/backend/data
    restart: unless-stopped
```
