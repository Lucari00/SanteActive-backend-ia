from pydantic import BaseModel
from typing import Dict

class LlamaRequest(BaseModel):
    messages: Dict[str, str]  # Dictionnaire avec des identifiants de questions comme clés et des questions comme valeurs
