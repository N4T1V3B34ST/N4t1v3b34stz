"""
Telegram bot handler for sending messages and receiving commands
"""
import asyncio
import logging
from telegram import Bot
from config import config

logger = logging.getLogger(__name__)


async def send_telegram_message(message: str) -> bool:
    """
    Send a message to Telegram
    
    Args:
        message: Message to send
        
    Returns:
        True if successful, False otherwise
    """
    if not config.TELEGRAM_BOT_TOKEN or not config.TELEGRAM_CHAT_ID:
        logger.warning("Telegram credentials not configured")
        return False
    
    try:
        bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
        await bot.send_message(
            chat_id=config.TELEGRAM_CHAT_ID,
            text=message,
            parse_mode="Markdown"
        )
        logger.info("Message sent to Telegram successfully")
        return True
    except Exception as e:
        logger.error(f"Error sending Telegram message: {str(e)}")
        return False


def send_telegram_message_sync(message: str) -> bool:
    """
    Synchronous wrapper for sending Telegram messages
    
    Args:
        message: Message to send
        
    Returns:
        True if successful, False otherwise
    """
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    return loop.run_until_complete(send_telegram_message(message))