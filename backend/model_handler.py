import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from io import BytesIO
import requests
import base64
from typing import Optional
from PIL import Image



tokenizer = AutoTokenizer.from_pretrained("./causal-llm-tokenizer")
model = AutoModelForCausalLM.from_pretrained("./causal-llm-model", trust_remote_code=True)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


DEFAULT_PROMPT = (
    "First give a brief summary of the image."
    " Imagine you are a senior designer who cares about clear design and give constructive feedback on how to improve the image."
    " Only if there is text, tell me if there enough contrast on the text and background?"
    " Does the design make sense?"
    " Do alignment and padding of elements fit best design practices?"
)
def load_image_from_url(url: str) -> bytes:
    """Download an image from a URL and return as bytes."""
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("Could not retrieve image from the URL.")
    return response.content

def load_image_from_base64(encoded_image: str) -> bytes:
    """Decode a base64-encoded image to bytes."""
    return base64.b64decode(encoded_image)

def generate_image_feedback(image_data: bytes, user_prompt: Optional[str] = None) -> str:
    """
    Generate feedback for an image based on a combined prompt using the BLIP model.
    
    Parameters:
        image_data (bytes): Image data in bytes format.
        user_prompt (str): Optional user-provided prompt text.
    
    Returns:
        str: Generated feedback text.
    """

    image = Image.open(BytesIO(image_data))
    enc_image = model.encode_image(image)
    
    prompt = f"{DEFAULT_PROMPT} {user_prompt}" if user_prompt else DEFAULT_PROMPT


    feedback = model.answer_question(enc_image, prompt, tokenizer, num_beams=4, no_repeat_ngram_size=5, early_stopping=True)
    
    return feedback