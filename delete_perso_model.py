import ollama
from app.config import MODEL_NAME

models_list = ollama.list()
for model in models_list['models']:
    if model['name'].startswith(MODEL_NAME):
        print(ollama.delete(MODEL_NAME))
        break

