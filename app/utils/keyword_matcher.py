def find_best_match(user_message: str, faqs: list):
    """
    Find best matching FAQ based on keyword matching
    """

    user_message = user_message.lower()

    for faq in faqs:
        keywords = faq.keywords.split(",")

        for keyword in keywords:
            keyword = keyword.strip().lower()

            if keyword in user_message:
                return faq

    return None