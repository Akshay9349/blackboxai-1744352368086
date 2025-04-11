import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = "7669055929:AAHmKeGSaV4kbZGwfjeTm0ptQRfnV_N3_aA"

WELCOME_MESSAGE = """
Welcome to Vehicle RC Details Bot! 🚗

Use this bot to check vehicle RC details.
Commands:
/search <registration_number> - Search RC details
/help - Show help message

Example: /search KA01AB1234
"""

HELP_MESSAGE = """
Available commands:
/start - Start the bot
/search <registration_number> - Search RC details
/help - Show this help message

Example usage:
/search KA01AB1234
"""
