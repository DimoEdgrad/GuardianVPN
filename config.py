import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_TOKEN = os.environ.get("6489239711:AAHdUIHNoBj2az2azuLXfnPM_KV3t_2MDrs")
PAYMENT_PROVIDER_TOKEN = os.environ.get("PAYMENT_PROVIDER_TOKEN")
OVPN_FILE_PATH = os.environ.get("OVPN_FILE_PATH")
WG_FILE_PATH = os.environ.get("WG_FILE_PATH")
QR_CODE_PATH = os.environ.get("QR_CODE_PATH")
LINKS_PATH = os.environ.get("LINKS_PATH")
