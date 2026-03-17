from pydantic import BaseModel, Field


class IncomingMessage(BaseModel):
    from_: str = Field(..., alias="from", description="Customer phone number")
    to: str = Field(..., description="Business WhatsApp number")
    message: str = Field(..., description="Customer message text")

    class Config:
        populate_by_name = True