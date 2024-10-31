# Backend-IA

Backend-IA of the backend of Santeactive.
It creates a personalized model of llama3.1 and uses it to generate a rephrased question received on the API.

## Installation

You need to install Ollama first. You can find the installation website [here](https://ollama.com/download).

Then you need to install the requirements of the project.

``` pip install -r requirements.txt ```

## Run

Launch the server with the following command. It will reload the server if you change the code.

```uvicorn app.main:app --reload --host 0.0.0.0 --port 8000```

## Usage

You can use the API with the following command.

```curl -X POST "http://127.0.0.1:8000/api/generate" \ -H "Content-Type: application/json" \ -d "{\"messages\": {\"1\": \"Quelle est la météo aujourd'hui ?\", \"2\": \"Quelle heure est-il ?\"}}"```

## Explaination

The API is a FastAPI server.
The model is based on llama3.1. If you don't have it, it will be downloaded automatically.

The model is then personalized with the modelfile automatically. If the modelfile is modified, you need to delete the personalized model and create it again.
You can delete the personalized model with python delete_perso_model.py.
