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
FAQ Service (Mock DB)
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
* Pydantic
* httpx (for API calls)

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
WHATSAPP_API_URL = "https://graph.facebook.com/v18.0"
WHATSAPP_ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
WHATSAPP_PHONE_NUMBER_ID = "YOUR_PHONE_NUMBER_ID"
```

---

## 🔁 Message Processing Flow

1. Receive message via webhook
2. Convert message to lowercase
3. Fetch FAQs for the business
4. Match message with keywords
5. If match found → send FAQ answer
6. If no match → send fallback response

---

## 🔍 Keyword Matching Logic

* Split keywords by comma
* Trim and lowercase
* Check if message contains keyword

Example:

```text
Message: "What is the price?"
Keywords: price,cost,charges
Match: ✅ Yes
```

---

## 💬 Example Conversation

**User:**
What is the price?

**Bot:**
Consultation fee is ₹500.

---

**User:**
What are your timings?

**Bot:**
We are open from 10 AM to 8 PM Monday to Saturday.

---

## ⚠️ Fallback Response

```text
Sorry, I couldn't understand your question. Please contact support.
```

---

## 🧪 Mock Data

Currently using in-memory FAQ data:

```text
Business Number: 919111111111
```

FAQs:

* price,cost → ₹500
* timing,hours → 10 AM – 8 PM
* location,address → Park Street, Kolkata

---

## ▶️ Running the Application

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Run server

```bash
uvicorn app.main:app --reload
```

---

### 3. Test health endpoint

```text
http://localhost:8000/health
```

---

### 4. Test webhook (Postman / curl)

```bash
curl -X POST http://localhost:8000/webhook/whatsapp \
-H "Content-Type: application/json" \
-d '{
  "from": "919876543210",
  "to": "919111111111",
  "message": "What is the price?"
}'
```

---

## ⚠️ Notes

* WhatsApp API requires valid access token and phone number ID
* For testing without API, replace sender logic with print statements
* Real WhatsApp webhook payload is more complex (to be handled later)

---

## 🧱 Future Enhancements

* 📦 PostgreSQL integration
* 🏢 Multi-business support
* 🤖 AI fallback (LLM integration)
* 📅 Appointment booking
* 📊 Admin dashboard
* 🌐 Multi-language support
* ⚡ Redis caching

---

## 📈 Business Value

* Saves 2–3 hours daily
* Handles repetitive queries automatically
* Improves response speed
* Scales customer support without hiring

---

## 🤝 Contribution

Feel free to extend:

* Add database layer
* Improve keyword matching
* Add AI integration
* Build frontend dashboard

---

## 💡 Author Note

This project is a **foundation for a WhatsApp automation SaaS** targeting small businesses like clinics, salons, and restaurants.

You can extend this into a full product with recurring revenue.

---
