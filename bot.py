import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from config import BOT_TOKEN, CHANNEL_ID, CHECK_INTERVAL
from database import is_post_processed, mark_post_processed
from rss_scraper import get_new_post_links
from scraper import extract_magnet_links

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

async def send_magnet_link(magnet):
    """Send magnet link to Telegram channel in specified format."""
    message = f"/qbleech {magnet}\n<b>Tag:</b> <code>@Mr_official_300</code> <code>2142536515</code>"
    await bot.send_message(CHANNEL_ID, message)

async def process_posts():
    """Check for new posts, scrape magnet links, and send them to Telegram with delay."""
    while True:
        new_posts = get_new_post_links()
        
        for post in new_posts:
            if not is_post_processed(post):
                magnets = extract_magnet_links(post)
                for magnet in magnets:
                    await send_magnet_link(magnet)
                    await asyncio.sleep(300)  # 5-minute delay before sending the next magnet
                
                mark_post_processed(post)

        await asyncio.sleep(CHECK_INTERVAL)  # Wait before checking RSS feed again

async def main():
    """Start the bot and processing loop."""
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(process_posts())
