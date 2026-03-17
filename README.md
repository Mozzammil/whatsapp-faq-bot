# 📲 WhatsApp FAQ Bot (FastAPI)

An automated **FAQ response system for WhatsApp** built using **FastAPI (Python)**.
This project helps small businesses automatically reply to repetitive customer queries like pricing, timings, and location.

---

## 🚀 Overview

Small businesses receive many repetitive WhatsApp messages such as:

* "What is the price?"
* "What are your timings?"
* "Where are you located?"

This system automates responses using predefined FAQs, reducing manual effort and saving time.

---

## 🧠 Features (MVP)

* ✅ WhatsApp webhook integration
* ✅ FAQ-based auto replies
* ✅ Keyword matching engine
* ✅ Fallback response for unknown queries
* ✅ Clean modular architecture
* ✅ Async processing with FastAPI

---

## 🏗️ Architecture

```text
Customer
   ↓
WhatsApp Message
   ↓
WhatsApp Cloud API
   ↓
FastAPI Webhook
   ↓
Message Processor
   ↓
FAQ Service (PostgreSQL)
   ↓
Keyword Matcher
   ↓
WhatsApp Sender
   ↓
Response to Customer
```

---

## 🛠️ Tech Stack

* Python 3.10+
* FastAPI
* Uvicorn
* SQLAlchemy
* PostgreSQL
* Pydantic v2
* httpx

---

## 📁 Project Structure

```text
whatsapp_faq_bot/
│
├── app/
│   ├── main.py
│   ├── config.py
│   │
│   ├── api/
│   │   └── webhook.py
│   │
│   ├── db/
│   │   ├── session.py
│   │   └── base.py
│   │
│   ├── models/
│   │   ├── business.py
│   │   └── faq.py
│   │
│   ├── services/
│   │   ├── message_processor.py
│   │   ├── faq_service.py
│   │   └── whatsapp_sender.py
│   │
│   ├── schemas/
│   │   └── message.py
│   │
│   ├── utils/
│   │   └── keyword_matcher.py
│
├── requirements.txt
└── README.md
```

---

## 🔌 API Endpoint

### Webhook

```http
POST /webhook/whatsapp
```

### Sample Request

```json
{
  "from": "919876543210",
  "to": "919111111111",
  "message": "What is the price?"
}
```

---

## ⚙️ Configuration

Edit `app/config.py`:

```python
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/whatsappbot"

WHATSAPP_API_URL = "https://graph.facebook.com/v18.0"
WHATSAPP_ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
WHATSAPP_PHONE_NUMBER_ID = "YOUR_PHONE_NUMBER_ID"
```

---

# ▶️ Running the Application

## 1️⃣ Create Virtual Environment (if not created)

```bash
python -m venv .venv
```

---

## 2️⃣ Activate Virtual Environment

### Windows (PowerShell)

```bash
.venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run Server (Recommended)

```bash
python -m uvicorn app.main:app --reload
```

---

## 5️⃣ Open API Docs

```text
http://127.0.0.1:8000/docs
```

---

## 6️⃣ Test Health Endpoint

```text
http://127.0.0.1:8000/health
```

---

## 7️⃣ Test Webhook

```bash
curl -X POST http://127.0.0.1:8000/webhook/whatsapp \
-H "Content-Type: application/json" \
-d '{
  "from": "919876543210",
  "to": "919111111111",
  "message": "What is the price?"
}'
```

---

# 🧪 Insert Test Data

## Insert Business

```sql
INSERT INTO businesses (id, name, whatsapp_phone_number)
VALUES (
    gen_random_uuid(),
    'ABC Clinic',
    '919111111111'
);
```

---

## Insert FAQ

```sql
INSERT INTO faqs (id, business_id, keywords, answer)
VALUES (
    gen_random_uuid(),
    (SELECT id FROM businesses WHERE whatsapp_phone_number='919111111111'),
    'price,cost,charges',
    'Consultation fee is ₹500'
);
```

---

# 🐞 Debugging & Common Fixes

## ❌ Uvicorn Not Found

```bash
pip install uvicorn
```

Run using:

```bash
python -m uvicorn app.main:app --reload
```

---

## ❌ Virtual Environment Not Activated

```bash
.venv\Scripts\activate
```

---

## ❌ Pydantic BaseSettings Error

```bash
pip install pydantic-settings
```

Update import:

```python
from pydantic_settings import BaseSettings
```

---

## ❌ Import Errors

```bash
pip install -r requirements.txt
```

Check:

* File names
* Function names
* Correct imports

---

## ❌ PostgreSQL Connection Issues

```bash
psql -U postgres
```

```sql
\l
```

---

## ❌ Tables Not Created

Ensure in `main.py`:

```python
from app.models import business, faq
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)
```

---

## ❌ No Response from Bot

Add debug logs:

```python
print("Incoming message:", user_message)
print("FAQs fetched:", faqs)
print("Matched FAQ:", matched_faq)
```

---

## ❌ WhatsApp API 401 Error

Temporary fix:

```python
async def send_message(to: str, message: str):
    print(f"Sending message to {to}: {message}")
```

---

## ❌ Port Already in Use

```bash
netstat -ano | findstr :8000
```

```bash
taskkill /PID <PID> /F
```

---

## ❌ Restart Server

```bash
CTRL + C
python -m uvicorn app.main:app --reload
```

---

# 🔁 Message Processing Flow

1. Receive message via webhook
2. Convert message to lowercase
3. Fetch FAQs from DB
4. Match keywords
5. Send response

---

# 💬 Example

**User:**
What is the price?

**Bot:**
Consultation fee is ₹500.

---

# ⚠️ Notes

* WhatsApp API requires valid token
* Replace sender logic with print for local testing
* Real webhook payload is more complex

---

# 🚀 Future Enhancements

* Admin APIs (Add/Edit FAQs)
* AI fallback (LLM integration)
* Multi-business SaaS
* Dashboard UI
* Appointment booking
* Analytics

---

# 📈 Business Value

* Saves 2–3 hours daily
* Automates repetitive queries
* Improves response speed
* Scales support easily

---

# 🤝 Contribution

Feel free to extend:

* Add database layer
* Improve matching logic
* Add AI integration
* Build frontend

---

# 💡 Author Note

This project is a **foundation for a WhatsApp automation SaaS**.
---
