from sqlalchemy.orm import Session
from app.services.faq_service import get_faqs_by_business
from app.utils.keyword_matcher import find_best_match
from app.services.whatsapp_sender import send_message


async def process_message(payload, db: Session):
    user_message = payload.message.lower()
    business_number = payload.to

    # Fetch FAQs from DB
    faqs = await get_faqs_by_business(db, business_number)

    matched_faq = find_best_match(user_message, faqs)

    if matched_faq:
        response = matched_faq.answer
    else:
        response = "Sorry, I couldn't understand your question."

    await send_message(payload.from_, response)