from app.config import settings
from app.services.faq_service import get_faqs_by_business
from app.services.whatsapp_sender import send_message
from app.utils.keyword_matcher import match_keywords


async def process_message(payload):
    try:
        message = payload.message.lower()
        business_number = payload.to
        customer_number = payload.from_

        print(f"Incoming message: {message} from {customer_number}")

        # Step 1: Fetch FAQs for this business
        faqs = await get_faqs_by_business(business_number)

        # Step 2: Match message with FAQs
        for faq in faqs:
            if match_keywords(message, faq.keywords):
                print(f"FAQ match found: {faq.answer}")

                await send_message(customer_number, faq.answer)
                return

        # Step 3: Fallback
        print("No FAQ match found. Sending fallback.")

        await send_message(customer_number, settings.FALLBACK_MESSAGE)

    except Exception as e:
        print(f"Error in processing message: {e}")