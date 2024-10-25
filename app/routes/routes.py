from fastapi import APIRouter, HTTPException
from app.models.client import client
from app.schemas.request import LlamaRequest
import json

router = APIRouter()

@router.post("/generate")
async def generate_text(request: LlamaRequest):
    try:
        message = [{"role": "user", "content": json.dumps(request.messages)}]
        response = await client.generate_response(message)
        return {"response": json.loads(response['message']['content'])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
