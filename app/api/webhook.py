from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.message import IncomingMessage
from app.services.message_processor import process_message
from app.db.session import get_db

router = APIRouter()


@router.post("/whatsapp")
async def receive_whatsapp_message(
    payload: IncomingMessage,
    db: Session = Depends(get_db)
):
    await process_message(payload, db)
    return {"status": "received"}