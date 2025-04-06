from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, filters, MessageHandler
import asyncio
import re

# Admin IDs list
ADMIN_IDS = [7864315763 , 7109503122]

# Store user IDs who have interacted with the bot
USER_IDS = set()

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

# Admin commands message
ADMIN_COMMANDS_MESSAGE = """Below you'll find a list with the admin commands available in this bot.

ADMIN COMMANDS
/admin - Display this admin commands menu.
/alert_everyone - Send a message to all users who have interacted with the bot.

HOW TO USE ALERT_EVERYONE:
1. For text messages: /alert_everyone "Your message"
   Example: /alert_everyone "Hello everyone! New content available!"

2. For video messages: 
   - First, send a video to the bot
   - Then reply to that video with: /alert_everyone [optional caption]
   - The video and caption will be sent to all users

Note: The command will show you statistics of how many messages were successfully delivered.
"""

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
    # Get user ID
    user_id = update.effective_user.id
    
    # Add user to the list of users who have interacted with the bot
    USER_IDS.add(user_id)
    
    # Display terms agreement message first
    tos_message = "By using Naughty Vibes Nepal(@NaughtyVibessNepal_bot), you agree to be legally bound by the terms listed below.\n\nIf you do not agree then please do not use this bot."
    
    keyboard = [
        [InlineKeyboardButton("Terms of Service", callback_data="view_tos")],
        [InlineKeyboardButton("I Agree", callback_data="agree_tos")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send the terms agreement message with buttons
    await update.message.reply_text(tos_message, reply_markup=reply_markup)

# Terms of Service message
TOS_MESSAGE = """### Welcome to BabesNepal Bot

Welcome to , Naughty Vibes  Nepal's most exclusive community and the only one featured on ThePornDude! Our bot is here to assist you. Please review our Terms of Service for a smooth experience.

### Terms of Service

By using our bot, you agree to the following:

1. Acceptance of Terms

Use of the bot means you agree to these terms. If not, please do not use the bot.

2. User Responsibilities

- Provide accurate information.

- Do not use the bot for illegal activities.

- Respect other community members.

3. Privacy

Your information is handled according to our Privacy Policy.

4. Account Security

You are responsible for your account's security and activities.

5. Prohibited Actions

- No illegal content.

- Do not disrupt services.

- No unauthorized access attempts.

6. Termination

We can terminate or suspend access at any time if terms are breached.

7. Modifications to Terms

Terms can change. Continued use after changes means acceptance.

8. Contact Us

Questions? Contact us through our platform."""

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    
    # Add user to the list of users who have interacted with the bot
    USER_IDS.add(user_id)
    
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
        
    elif query.data == "premium_esewa":
        premium_message = "BabesNepal Premium (esewa): NPR2,000.00 / 30 days\n\nFor eSewa payment, please contact the owner @Aryanlamaa directly for payment information."
        
        keyboard = [
            [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text(premium_message, reply_markup=reply_markup)
        
    elif query.data == "vip_membership":
        vip_message = "MEMBERSHIP VIP: $15.99 / 1 month\n\nPlease select your preferred payment method:"
        
        keyboard = [
            [InlineKeyboardButton("Crypto Payment", callback_data="crypto"),
             InlineKeyboardButton("UPI Payment", callback_data="wallet")],
            [InlineKeyboardButton("eSewa Payment", callback_data="esewa")],
            [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text(vip_message, reply_markup=reply_markup)
        
    elif query.data == "one_day_access":
        day_access_message = "One day access token mutantX: $3.99 / 1 day\n\nPlease select your preferred payment method:"
        
        keyboard = [
            [InlineKeyboardButton("Crypto Payment", callback_data="crypto"),
             InlineKeyboardButton("UPI Payment", callback_data="wallet")],
            [InlineKeyboardButton("eSewa Payment", callback_data="esewa")],
            [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text(day_access_message, reply_markup=reply_markup)
        
    elif query.data == "lifetime_crypto":
        lifetime_message = "LIFETIME CRYPTO: $99 / Lifetime\n\nFor Crypto payment:"
        
        # Send the crypto payment image
        await query.message.reply_photo(photo=open('binance.jpg', 'rb'))
        
        keyboard = [
            [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text(lifetime_message, reply_markup=reply_markup)
        
    elif query.data == "two_month_esewa":
        two_month_message = "2 Month esewa: NPR3,000.00 / 2 month\n\nFor eSewa payment, please contact the owner @Aryanlamaa directly for payment information."
        
        keyboard = [
            [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text(two_month_message, reply_markup=reply_markup)
    
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

    elif query.data == "view_tos":
        # Show Terms of Service
        keyboard = [
            [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text(TOS_MESSAGE, reply_markup=reply_markup)
    
    elif query.data == "agree_tos":
        # User agreed to terms, show welcome message
        welcome_message = """Welcome to Naughty Vibess Nepal!

We provide 4 premium groups filled with exclusive premium contents.

DM @Aryanlamaa to buy from Nepal🇳🇵

https://t.me/+7X24Ow7NrE01Yjg1"""

        keyboard = [
            [InlineKeyboardButton("Donate", callback_data="donate")],
            [InlineKeyboardButton("BabesNepal Premium (esewa): NPR2,000.00 / 30 days", callback_data="premium_esewa")],
            [InlineKeyboardButton("MEMBERSHIP VIP : $15.99 / 1 month", callback_data="vip_membership")],
            [InlineKeyboardButton("One day access token mutantX: $3.99 / 1 day", callback_data="one_day_access")],
            [InlineKeyboardButton("LIFETIME CRYPTO: $2999 / Lifetime", callback_data="lifetime_crypto")],
            [InlineKeyboardButton("2 Month esewa: NPR5,000.00 / 2 month", callback_data="two_month_esewa")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.message.edit_text(welcome_message, reply_markup=reply_markup)
        
    elif query.data == "main_menu":
        # Return to main menu
        welcome_message = """Welcome to Naughty Vibess Nepal!

We provide 4 premium groups filled with exclusive premium contents.

DM @Aryanlamaa to buy from Nepal🇳🇵

https://t.me/+7X24Ow7NrE01Yjg1"""

        keyboard = [
            [InlineKeyboardButton("Donate", callback_data="donate")],
            [InlineKeyboardButton("BabesNepal Premium (esewa): NPR2,000.00 / 30 days", callback_data="premium_esewa")],
            [InlineKeyboardButton("MEMBERSHIP VIP : $15.99 / 1 month", callback_data="vip_membership")],
            [InlineKeyboardButton("One day access token mutantX: $3.99 / 1 day", callback_data="one_day_access")],
            [InlineKeyboardButton("LIFETIME CRYPTO: $99 / Lifetime", callback_data="lifetime_crypto")],
            [InlineKeyboardButton("2 Month esewa: NPR3,000.00 / 2 month", callback_data="two_month_esewa")]
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

async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if user is admin
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("Sorry, you are not authorized to use this command.")
        return
    
    keyboard = [
        [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(ADMIN_COMMANDS_MESSAGE, reply_markup=reply_markup)

async def tos_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(TOS_MESSAGE, reply_markup=reply_markup)

async def subscribe_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Add user to the list of users who have interacted with the bot
    user_id = update.effective_user.id
    USER_IDS.add(user_id)
    
    keyboard = [
        [InlineKeyboardButton("Donate", callback_data="donate")],
        [InlineKeyboardButton("Back to Main Menu", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Please select an option from the list below:", reply_markup=reply_markup)

async def alert_everyone_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if user is admin
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("Sorry, you are not authorized to use this command.")
        return
    
    # Check if there's a video attached to the message
    if update.message.reply_to_message and update.message.reply_to_message.video:
        # User is replying to a video message
        video_file_id = update.message.reply_to_message.video.file_id
        caption = update.message.text.replace("/alert_everyone", "").strip()
        
        # Send video to all users who have interacted with the bot
        sent_count = 0
        failed_count = 0
        
        for recipient_id in USER_IDS:
            try:
                await context.bot.send_video(chat_id=recipient_id, video=video_file_id, caption=caption)
                sent_count += 1
            except Exception as e:
                failed_count += 1
                logging.error(f"Failed to send video to {recipient_id}: {e}")
        
        # Send summary to admin
        await update.message.reply_text(
            f"Video broadcast complete:\n- Video sent to {sent_count} users\n- Failed to send to {failed_count} users"
        )
    else:
        # Extract the message from the command for text-only messages
        message_text = update.message.text
        # Use regex to extract the message part after the command
        match = re.match(r'/alert_everyone\s+"(.+)"', message_text)
        
        if not match:
            await update.message.reply_text(
                "Please use one of these formats:\n" +
                "1. For text messages: /alert_everyone \"Your message\"\n" +
                "2. For video messages: Reply to a video with /alert_everyone [optional caption]"
            )
            return
        
        broadcast_message = match.group(1)
        
        # Send text message to all users who have interacted with the bot
        sent_count = 0
        failed_count = 0
        
        for recipient_id in USER_IDS:
            try:
                await context.bot.send_message(chat_id=recipient_id, text=broadcast_message)
                sent_count += 1
            except Exception as e:
                failed_count += 1
                logging.error(f"Failed to send message to {recipient_id}: {e}")
        
        # Send summary to admin
        await update.message.reply_text(
            f"Text broadcast complete:\n- Message sent to {sent_count} users\n- Failed to send to {failed_count} users"
        )

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
    application.add_handler(CommandHandler("tos", tos_command))
    application.add_handler(CommandHandler("alert_everyone", alert_everyone_command))
    application.add_handler(CommandHandler("admin", admin_command))
    application.add_handler(CallbackQueryHandler(button_callback))
    
    # Add handler for all messages to track users
    application.add_handler(MessageHandler(filters.ALL, lambda update, context: USER_IDS.add(update.effective_user.id)))

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
                ("tos", "View the terms of service"),
                ("admin", "[Admin only] Display admin commands"),
                ("alert_everyone", "[Admin only] Send a message to all users")
            ]
            await app.bot.set_my_commands(commands)
            await app.shutdown()
        
        # Run the setup commands first
        asyncio.run(setup_commands())
        
        # Then start the main bot
        main()
    except KeyboardInterrupt:
        print("Bot stopped by user")
