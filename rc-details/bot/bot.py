from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import re
import requests
from config import BOT_TOKEN, WELCOME_MESSAGE, HELP_MESSAGE

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(WELCOME_MESSAGE)

def search(update: Update, context: CallbackContext) -> None:
    if len(context.args) < 1:
        update.message.reply_text("Please provide a registration number.\nExample: /search KA01AB1234")
        return
    
    reg_number = context.args[0].upper()
    # Validate registration number
    if not is_valid_registration(reg_number):
        update.message.reply_text("Invalid registration number format.\nExample format: KA01AB1234")
        return
    
    # Simulate RC details fetch (replace with actual API call)
    try:
        rc_details = get_rc_details(reg_number)
        update.message.reply_text(format_rc_details(rc_details))
    except Exception as e:
        update.message.reply_text("Sorry, couldn't fetch RC details. Please try again later.")

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(HELP_MESSAGE)

def is_valid_registration(reg_number: str) -> bool:
    # Example regex for Indian registration numbers
    regEx = re.compile(r'^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$')
    return bool(regEx.match(reg_number))

def get_rc_details(reg_number: str) -> dict:
    # Simulated RC details (replace with actual API call)
    return {
        "regNumber": reg_number,
        "ownerName": "John Doe",
        "vehicleModel": "Toyota Corolla",
        "regDate": "2020-01-15",
        "vehicleClass": "Sedan",
        "fuelType": "Petrol",
        "engineNumber": "EN123456789",
        "chassisNumber": "CH123456789"
    }

def format_rc_details(rc_details: dict) -> str:
    return (
        f"Registration Number: {rc_details['regNumber']}\n"
        f"Owner Name: {rc_details['ownerName']}\n"
        f"Vehicle Model: {rc_details['vehicleModel']}\n"
        f"Registration Date: {rc_details['regDate']}\n"
        f"Vehicle Class: {rc_details['vehicleClass']}\n"
        f"Fuel Type: {rc_details['fuelType']}\n"
        f"Engine Number: {rc_details['engineNumber']}\n"
        f"Chassis Number: {rc_details['chassisNumber']}"
    )

def main() -> None:
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("search", search))
    dispatcher.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
