import ollama
from app.config import BASE_MODEL_NAME, MODEL_NAME
from app.models.modelfile import model_file

class Client:
    def __init__(self, base_model_name=BASE_MODEL_NAME, model_name=MODEL_NAME):
        self.base_model_name = base_model_name
        if not self.is_base_model_downloaded():
            raise Exception(f'Base model {self.base_model_name} is not downloaded.')
        
        self.model_name = model_name
        if not self.is_personalized_model_created():
            raise Exception(f'Personalized model {MODEL_NAME} is not created.')
        self.client = ollama.AsyncClient()

    def is_base_model_downloaded(self):
        """Vérifie si le modèle est déjà téléchargé, sinon le télécharge."""
        models = ollama.list()
        for model in models['models']:
            if model['name'].startswith(self.base_model_name):
                print(f'{self.base_model_name} is already downloaded.')
                return True

        print(f'{self.base_model_name} is not downloaded. Downloading...')
        progress = ollama.pull(self.base_model_name)
        if progress['status'] == 'success':
            print(f'{self.base_model_name} downloaded successfully.')
            return True
        else:
            print(f'Error downloading {self.base_model_name}. Status: {progress["status"]}')
            return False
        
    def is_personalized_model_created(self):
        """Vérifie si le modèle personnalisé est déjà créé, sinon le crée."""
        models = ollama.list()
        for model in models['models']:
            if model['name'].startswith(self.model_name):
                print(f'{self.model_name} is already created.')
                return True

        print(f'{MODEL_NAME} is not created. Creating...')
        progress = ollama.create(MODEL_NAME, modelfile=model_file)
        if progress['status'] == 'success':
            print(f'{MODEL_NAME} created successfully.')
            return True
        
    def is_personalized(self):
        """Vérifie si le modèle est personnalisé."""
        

    async def generate_response(self, message):
        """Utilise Ollama pour générer une réponse basée sur les messages fournis."""
        # formatted_messages = {"role": "user", "content": message}
        # print(formatted_messages)
        # print(type(message))
        response = await self.client.chat(self.model_name, messages=message)
        return response

try:
    client = Client()
except Exception as e:
    # quitter le programme si le modèle n'est pas téléchargé
    print(f'Error: {e}')
    exit(1)