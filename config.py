import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8121826554:AAGPzWAHNGbsrCQfi4IXIiuWL2UCA5EvY7w")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21201860"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "621b19f6fbc1503b84b9d9fa0b4ffcf8")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6073523936"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
