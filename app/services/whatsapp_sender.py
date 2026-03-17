import httpx
from app.config import settings


async def send_message(to: str, message: str):
    """
    Sends a WhatsApp message using WhatsApp Cloud API
    """

    url = f"{settings.WHATSAPP_API_URL}/{settings.WHATSAPP_PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {settings.WHATSAPP_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {
            "body": message
        }
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload, headers=headers)

        print(f"WhatsApp API response: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"Error sending WhatsApp message: {e}")