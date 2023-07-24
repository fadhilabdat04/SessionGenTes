import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "12857763").strip()
API_HASH = os.getenv("API_HASH", "7b71e8bca0d5e1c6d8383ae818d9ec8d").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6375262996:AAFZBXDHSjs6Yn5M_1CbV_XS-tWQqG_wYX4").strip()
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://Arab01:fadhil123@cluster0.ul5qaif.mongodb.net/").strip()
AUTH_CHANNEL = os.getenv("AUTH_CHANNEL", "SiArab_Store").strip()
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY", None).strip()
BOT_USERNAME = os.getenv("BOT_USERNAME", "StringArabRobot").strip()
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", None).strip()
AUTH_USERS = os.getenv("AUTH_USERS", "1345594412").strip()
