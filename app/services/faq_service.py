from dataclasses import dataclass
from typing import List


@dataclass
class FAQ:
    keywords: str
    answer: str


# Mock data (temporary)
FAKE_FAQ_DB = {
    "919111111111": [
        FAQ(
            keywords="price,cost,charges",
            answer="Consultation fee is ₹500."
        ),
        FAQ(
            keywords="timing,hours,open",
            answer="We are open from 10 AM to 8 PM Monday to Saturday."
        ),
        FAQ(
            keywords="location,address",
            answer="We are located at Park Street, Kolkata."
        ),
    ]
}


async def get_faqs_by_business(business_number: str) -> List[FAQ]:
    """
    Fetch FAQs for a given business number.
    Currently using mock data.
    """

    return FAKE_FAQ_DB.get(business_number, [])
