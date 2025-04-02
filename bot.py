from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Admin IDs list
ADMIN_IDS = [7864315763, 7109503122]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if user is admin
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("Sorry, you are not authorized to use this bot.")
        return

    welcome_message = """Nepal's Most Exclusive Community ⭐️ #1 r/

https://t.me/+XwsrHPxBW5M4ZWVl

Get your membership from Esewa , Litewallet ,Upi ,TonCoin !!

LiteWallet  : 0xf663870211c015c48929e11c4c6689fe1df76a8d  (BNB Smart Chain Bep20)
Website     :

DM @Aryanlamaa to buy from Nepal 🇳🇵"""

    # Create the keyboard with two buttons
    keyboard = [
        [
            InlineKeyboardButton("UPI", callback_data="upi"),
            InlineKeyboardButton("Binance", callback_data="binance")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the welcome message with the buttons
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    
    if user_id not in ADMIN_IDS:
        await query.answer("You are not authorized to use this feature.")
        return

    await query.answer()

    if query.data == "upi":
        # Send UPI image with enhanced message
        caption = """🇮🇳 UPI Payment Details 💳

Contact @Aryanlamaa if you have any issues ✨

⚠️ Please save the screenshot of payment"""
        await query.message.reply_photo(
            photo=open("upi.jpg", "rb"),
            caption=caption
        )
    
    elif query.data == "binance":
        # Send Binance image with enhanced message
        caption = """🌟 Binance Payment Details 💰

Contact @Aryanlamaa if you have any issues ✨

⚠️ Please save the screenshot of payment"""
        await query.message.reply_photo(
            photo=open("binance.jpg", "rb"),
            caption=caption
        )

# Add this at the top of your file
import logging

# Add this before the main() function
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    try:
        application = Application.builder().token("7656138656:AAFa5gCBCGBsfXK4nhxWrloHNv0g36F1Aac").build()

        application.add_handler(CommandHandler("start", start))
        application.add_handler(CallbackQueryHandler(button_callback))

        print("Bot is starting...")
        application.run_polling()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()