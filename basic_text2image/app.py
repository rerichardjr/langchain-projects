import requests
import os
from dotenv import load_dotenv

load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
model = "stabilityai/stable-diffusion-3-medium-diffusers"

API_URL = "https://api-inference.huggingface.co/models/"f"{model}"
headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}

def text2image(message):
    response = requests.post(API_URL, headers=headers, json=message)
    return response.content

prompt = input("Enter text2image prompt: ")
filename = input("Save as filename (.jpg): " )

image = text2image({
	"inputs": prompt,
})

with open(f"{filename}.jpg", 'wb') as file:
    file.write(image)
