def match_keywords(message: str, keywords: str) -> bool:
    """
    Checks if any keyword is present in the message.

    :param message: user message (already lowercase)
    :param keywords: comma-separated keywords from DB
    :return: True if match found, else False
    """

    if not keywords:
        return False

    keyword_list = [k.strip().lower() for k in keywords.split(",")]

    for keyword in keyword_list:
        if keyword in message:
            return True

    return False