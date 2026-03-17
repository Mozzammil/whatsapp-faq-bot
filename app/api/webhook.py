from fastapi import APIRouter, HTTPException
from app.schemas.message import IncomingMessage
from app.services.message_processor import process_message

router = APIRouter()


@router.post("/whatsapp")
async def receive_whatsapp_message(payload: IncomingMessage):
    try:
        await process_message(payload)
        return {"status": "received"}
    except Exception as e:
        # Log properly later
        print(f"Error processing message: {e}")
        return {"status": "error"}