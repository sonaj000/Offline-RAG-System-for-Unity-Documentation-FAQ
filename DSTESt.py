from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch
import os
# Model path or name
model_name = "mistralai/Mistral-7B-v0.1"

# Define quantization configuration
quantization_config = BitsAndBytesConfig(
    load_in_8bit=True,  # Use 8-bit quantization
)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

# Load model with quantization
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",              # Automatically map to available devices
    quantization_config=quantization_config,  # Use BitsAndBytesConfig for quantization
    max_memory={0: "10GiB"}         # Optional: Limit memory usage on GPU
)
print("Running on device:", model.device)
# Retrieve cache directory
cache_dir = os.getenv("HF_HOME", os.path.expanduser("~/.cache/huggingface/transformers"))
print("Default cache directory:", cache_dir)
# Define input prompt
prompt = "Explain how Unity GameObjects work in game development."

# Tokenize input
inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=100).to("cuda")

# Generate output
output = model.generate(
    input_ids=inputs["input_ids"],
    attention_mask=inputs["attention_mask"],
    max_length=100,  # Shorter outputs save memory
    temperature=0.7,
    top_k=50,
    top_p=0.9,
    do_sample=True
)

# Decode output
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print("Generated Text:")
print(generated_text)
