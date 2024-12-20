import os
import base64
from dotenv import load_dotenv

load_dotenv()

WAZZUP_API_KEY = os.getenv("WAZZUP_API_KEY")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
OMNIDESK_API_KEY=os.getenv("OMNIDESK_API_KEY")
OMNIDESK_STAFF_EMAIL=os.getenv("OMNIDESK_STAFF_EMAIL")
OMNIDESK_URL=os.getenv("OMNIDESK_URL")
DB_HOST=os.getenv("DB_HOST")
DB_NAME=os.getenv("DB_NAME")
DB_USER=os.getenv("DB_USER")
DB_PORT=os.getenv("DB_PORT")
DB_PASSWORD=os.getenv("DB_PASSWORD")
AI_TOKEN=os.getenv("AI_TOKEN")

auth_str= f"{OMNIDESK_STAFF_EMAIL}:{OMNIDESK_API_KEY}"
auth_header = base64.b64encode(auth_str.encode()).decode()

HEADERS = {
    "Authorization": f"Basic {auth_header}",
    "Content-Type": "application/json",
}