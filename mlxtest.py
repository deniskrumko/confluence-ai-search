# Make sure mlx-lm is installed
# pip install --upgrade mlx-lm

# Summarize text from file with mlx-lm
from mlx_lm import load, generate

# Load model
model, tokenizer = load("Qwen/Qwen3-8B-MLX-8bit")

# Read text from file
with open("text.txt", "r", encoding="utf-8") as f:
    text_content = f.read()

# Create prompt for summarization
prompt = f"Please provide a concise summary of the following text and made it in RUSSIAN LANGUAGE:\n\n{text_content}"
messages = [{"role": "user", "content": prompt}]
prompt = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    enable_thinking=False,
)

# Generate summary
summary = generate(model, tokenizer, prompt=prompt, verbose=True, max_tokens=512)
print("\n=== SUMMARY ===")
print(summary)
