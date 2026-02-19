# confluence-ai-search

Proof of concept for searching Confluence using vector db + RAG

## How to run

**NOTE**: No Docker or `docker-compose.yml` for more performance on my old Macbook M1 Pro.

```bash
# start ollama
ollama serve

# 8.9GB download, 100% GPU load
ollama run gemma3:12b-it-qat

# 4.7GB download, 100% GPU load
ollama run qwen2.5:7b

# Check what's loaded
ollama ps

# REST API (OpenAI-compatible)
curl http://localhost:11434/api/chat -d '{
  "model": "gemma3:12b-it-qat",
  "messages": [{"role": "user", "content": "Hello"}]
}'
```

```bash
pip install mlx-lm

# Start the server
mlx_lm.server --model "Qwen/Qwen3-8B-MLX-8bit"

# Calling the OpenAI-compatible server with curl
curl -X POST "http://localhost:8080/v1/chat/completions" \
   -H "Content-Type: application/json" \
   --data '{
     "model": "Qwen/Qwen3-8B-MLX-8bit",
     "messages": [
       {"role": "user", "content": "Hello"}
     ]
   }'
```
