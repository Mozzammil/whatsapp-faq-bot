from pydantic_settings  import BaseSettings


class Settings(BaseSettings):
    # App
    APP_NAME: str = "WhatsApp FAQ Bot"

    # Database
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/whatsappbot"

    # WhatsApp API
    WHATSAPP_API_URL: str = "https://graph.facebook.com/v18.0"
    WHATSAPP_ACCESS_TOKEN: str = "YOUR_ACCESS_TOKEN"
    WHATSAPP_PHONE_NUMBER_ID: str = "YOUR_PHONE_NUMBER_ID"

    # Fallback message
    FALLBACK_MESSAGE: str = (
        "Sorry, I couldn't understand your question. Please contact support."
    )

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()