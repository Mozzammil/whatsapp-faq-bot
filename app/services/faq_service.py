from sqlalchemy.orm import Session
from app.models.faq import FAQ
from app.models.business import Business


async def get_faqs_by_business(db: Session, business_number: str):
    """
    Fetch FAQs from DB using business phone number
    """

    faqs = (
        db.query(FAQ)
        .join(Business, FAQ.business_id == Business.id)
        .filter(Business.whatsapp_phone_number == business_number)
        .all()
    )

    return faqs