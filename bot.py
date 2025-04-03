from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, filters
import asyncio

# Admin IDs list
ADMIN_IDS = [7864315763 , 7109503122]

# Help message
HELP_MESSAGE = """Below you'll find a list with the commands available in this bot.

GENERAL
/help - Open the help menu.
/settings - Change the way you interact with this bot.
/start - Get started - show the initial message.

LEGAL
/tos - The conditions under which you can use this service.

SUBSCRIPTION
/donate - Make a donation to support this project.
/join - Join the channels or groups.
/membershipstatus - Renew or cancel your subscription.
/subscribe - Become a member."""

# Subscription message
SUBSCRIPTION_MESSAGE = "You will need to subscribe to become a member."

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(HELP_MESSAGE, reply_markup=reply_markup)

async def join_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Subscribe", callback_data="subscribe")],
        [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(SUBSCRIPTION_MESSAGE, reply_markup=reply_markup)

async def membershipstatus_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Subscribe", callback_data="subscribe")],
        [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(SUBSCRIPTION_MESSAGE, reply_markup=reply_markup)

async def settings_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("UI Settings", callback_data="ui_settings")],
        [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Settings Menu", reply_markup=reply_markup)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if user is admin
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("Sorry, you are not authorized to use this bot.")
        return

    welcome_message = """Nepal's Most Exclusive Community ⭐️ #1 r/

https://t.me/+XwsrHPxBW5M4ZWVl

Welcome to NAUGHTY VIBES PREMIUM!

DM @Aryanlamaa for any inquiries 🇳🇵"""

    # Create the keyboard with donate button
    keyboard = [
        [InlineKeyboardButton("Donate", callback_data="donate")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the welcome message with the button
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    
    if user_id not in ADMIN_IDS:
        await query.answer("You are not authorized to use this feature.")
        return

    await query.answer()

    if query.data == "donate":
        donation_message = """Donations help keep the project alive. This would not be possible without people like you who take our endeavor to heart.

What is the amount you would like to donate to NAUGHTY VIBES PREMIUM?

Please enter a number. It can be a whole number or a number with up to two decimal places.

Please note, the payment can be done using crypto or UPI."""
        
        keyboard = [
            [InlineKeyboardButton("Crypto Payment", callback_data="crypto"),
             InlineKeyboardButton("UPI Payment", callback_data="wallet")],
            [InlineKeyboardButton("eSewa Payment", callback_data="esewa")],
            [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.message.edit_text(donation_message, reply_markup=reply_markup)
    
    elif query.data == "crypto":
        crypto_message = "Here's our crypto payment address for your donation:"
        # Send the crypto payment image
        await query.message.reply_photo(photo=open('binance.jpg', 'rb'))
        
        keyboard = [
            [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text(crypto_message, reply_markup=reply_markup)
    
    elif query.data == "wallet":
        wallet_message = "Here's our UPI payment QR code for your donation:"
        # Send the UPI payment image
        await query.message.reply_photo(photo=open('upi.jpg', 'rb'))
        
        keyboard = [
            [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text(wallet_message, reply_markup=reply_markup)
    
    elif query.data == "esewa":
        esewa_message = "For eSewa payment, please contact the owner @Aryanlamaa directly for payment information."
        
        keyboard = [
            [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text(esewa_message, reply_markup=reply_markup)
    
    elif query.data == "subscribe":
        donation_message = """Donations help keep the project alive. This would not be possible without people like you who take our endeavor to heart.

What is the amount you would like to donate to NAUGHTY VIBES PREMIUM?

Please enter a number. It can be a whole number or a number with up to two decimal places.

Please note, the payment can be done using crypto or UPI."""
        
        keyboard = [
            [InlineKeyboardButton("Crypto Payment", callback_data="crypto"),
             InlineKeyboardButton("UPI Payment", callback_data="wallet")],
            [InlineKeyboardButton("eSewa Payment", callback_data="esewa")],
            [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.message.edit_text(donation_message, reply_markup=reply_markup)

    elif query.data == "ui_settings":
        keyboard = [
            [InlineKeyboardButton("Language", callback_data="language")],
            [InlineKeyboardButton("🔙 Back", callback_data="settings")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text("Viewing UI Settings", reply_markup=reply_markup)
    
    elif query.data == "language":
        keyboard = [
            [InlineKeyboardButton("Arabic", callback_data="lang_ar"),
             InlineKeyboardButton("Bulgarian", callback_data="lang_bg")],
            [InlineKeyboardButton("Czech", callback_data="lang_cs"),
             InlineKeyboardButton("Danish", callback_data="lang_da")],
            [InlineKeyboardButton("German", callback_data="lang_de"),
             InlineKeyboardButton("Greek", callback_data="lang_el")],
            [InlineKeyboardButton("English ✓", callback_data="lang_en"),
             InlineKeyboardButton("Spanish", callback_data="lang_es")],
            [InlineKeyboardButton("Persian", callback_data="lang_fa"),
             InlineKeyboardButton("French", callback_data="lang_fr")],
            [InlineKeyboardButton("Hebrew", callback_data="lang_he"),
             InlineKeyboardButton("Hungarian", callback_data="lang_hu")],
            [InlineKeyboardButton("Italian", callback_data="lang_it"),
             InlineKeyboardButton("Korean", callback_data="lang_ko")],
            [InlineKeyboardButton("Burmese", callback_data="lang_my"),
             InlineKeyboardButton("Dutch", callback_data="lang_nl")],
            [InlineKeyboardButton("Polish", callback_data="lang_pl"),
             InlineKeyboardButton("Brazilian Portuguese", callback_data="lang_pt")],
            [InlineKeyboardButton("🔙 Back", callback_data="ui_settings")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text("Please select the language you'd like to use from the list below.", reply_markup=reply_markup)
    
    elif query.data == "settings":
        keyboard = [
            [InlineKeyboardButton("UI Settings", callback_data="ui_settings")],
            [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text("Settings Menu", reply_markup=reply_markup)

    elif query.data.startswith("lang_"):
        # Here you can implement the language change logic
        keyboard = [
            [InlineKeyboardButton("🔙 Back", callback_data="language")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text(f"Language changed successfully!", reply_markup=reply_markup)

    elif query.data == "main_menu":
        # Return to main menu
        welcome_message = """Nepal's Most Exclusive Community ⭐️ #1 r/

https://t.me/+XwsrHPxBW5M4ZWVl

Welcome to NAUGHTY VIBES PREMIUM!

DM @Aryanlamaa for any inquiries 🇳🇵"""

        keyboard = [
            [InlineKeyboardButton("Donate", callback_data="donate")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.message.edit_text(welcome_message, reply_markup=reply_markup)

# Add this at the top of your file
import logging

# Add this before the main() function
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def subscribe_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Donate", callback_data="donate")],
        [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Please select an option from the list below:", reply_markup=reply_markup)

def main():
    # Create a new application instance
    application = Application.builder().token("7937120545:AAFc3wfm93IPAQFCZ7ZvBK_S9qKnyMCFd74").build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("join", join_command))
    application.add_handler(CommandHandler("membershipstatus", membershipstatus_command))
    application.add_handler(CommandHandler("settings", settings_command))
    application.add_handler(CommandHandler("subscribe", subscribe_command))
    application.add_handler(CallbackQueryHandler(button_callback))

    print("Bot is starting...")
    
    # Create an event loop and run the bot until the user presses Ctrl-C
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    application.run_polling()

if __name__ == "__main__":
    try:
        # Set up commands asynchronously before starting the bot
        async def setup_commands():
            app = Application.builder().token("7937120545:AAFc3wfm93IPAQFCZ7ZvBK_S9qKnyMCFd74").build()
            commands = [
                ("start", "Get started with the bot and see the welcome message"),
                ("help", "Display the help menu with available commands"),
                ("settings", "Access bot settings and configuration options"),
                ("join", "Join channels or groups"),
                ("membershipstatus", "Check your subscription status"),
                ("subscribe", "Subscribe to become a member"),
                ("donate", "Make a donation to support the project"),
                ("tos", "View the terms of service")
            ]
            await app.bot.set_my_commands(commands)
            await app.shutdown()
        
        # Run the setup commands first
        asyncio.run(setup_commands())
        
        # Then start the main bot
        main()
    except KeyboardInterrupt:
        print("Bot stopped by user")