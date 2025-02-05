import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")  # Private Telegram channel ID
RSS_FEED_URL = "https://www.1tamilmv.pm/index.php?/discover/all.xml"
BASE_URL = "https://www.1tamilmv.pm"
CHECK_INTERVAL = 300  # Time in seconds (5 minutes)
