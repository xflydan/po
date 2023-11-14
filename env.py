import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "27192333").strip()
API_HASH = os.getenv("API_HASH", "f5e17d3232f7e1ac576befaf319665b8").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6973703883:AAEjVwr5QdTx9pPzXlXXtvpRof9yYdH2yzk").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://rmttmknp:aZVxuRQ7E6HCfPS_4J6PwpclmY5SzRaV@trumpet.db.elephantsql.com/rmttmknp").strip() # Not a necessary variable anymore but you can add to get stats
MUST_JOIN = os.getenv("MUST_JOIN", "DanteSupportss")

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")
'''
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit
'''

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("API_ID is not a valid integer. Exiting...")

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
