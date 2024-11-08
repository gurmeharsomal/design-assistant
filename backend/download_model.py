import os
from transformers import AutoModelForCausalLM, AutoTokenizer

def download_model():
    print("Checking model...")
    model_dir = "./causal-llm-model"
    tokenizer_dir = "./causal-llm-tokenizer"
    if not os.path.exists(model_dir) or not os.path.exists(tokenizer_dir) :
        print("Downloading model...")

        model = AutoModelForCausalLM.from_pretrained("gurmeharkaursomal/finetuned-moondream-model-for-design-feedback", trust_remote_code=True)
        tokenizer = AutoTokenizer.from_pretrained("gurmeharkaursomal/finetuned-moondream-model-for-design-feedback", trust_remote_code=True)
        tokenizer.save_pretrained("./causal-llm-tokenizer")
        model.save_pretrained("./causal-llm-model")
        print("Model downloaded.")
    else:
        print("Model already downloaded.")

