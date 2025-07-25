
from models import load_text_model, generate_text
from fastapi import FastAPI

app = FastAPI()



@app.get("/generate/text")
def serve_language_model_controller(prompt: str) -> str:
    pipe = load_text_model()
    output = generate_text(pipe, prompt)
    return output



