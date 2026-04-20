import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

# Load values from .env file
load_dotenv()

# --- Telegram API Credentials ---
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# --- General Config ---
LOG_FILE_NAME = "bot.log"
PORT = os.getenv("PORT", "8080")
OWNER_ID = int(os.getenv("OWNER_ID", "1234567890"))
MSG_EFFECT = int(os.getenv("MSG_EFFECT", "5046509860389126442"))

# --- VPLink URL Shortener Configuration ---
VPLINK_API_TOKEN = os.getenv("VPLINK_API_TOKEN", "")
VPLINK_API_URL = "https://vplink.in/api"

# --- URL Shortener Providers Configuration ---
URL_SHORTENERS = {
    'vplink': {
        'name': 'VPLink',
        'api_url': VPLINK_API_URL,
        'api_token': VPLINK_API_TOKEN,
        'format': 'text',
        'active': True
    }
}

# --- Logger Setup ---
def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger
