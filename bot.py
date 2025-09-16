from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Data dari kamu
GROUP_ID = -1003076566846
BOT_TOKEN = "TOKEN_BOT_KAMU"  # Ganti dengan token botmu
CONTENT_LINK = "https://example.com/contoh-video-atau-gambar.jpg"  # Ganti sesuai kontenmu

def start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id

    try:
        member = context.bot.get_chat_member(GROUP_ID, user_id)
        status = member.status
    except Exception as e:
        status = None

    if status in ['member', 'administrator', 'creator']:
        keyboard = [
            [InlineKeyboardButton("Coba Lagi", callback_data='check_join')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            f"Kamu sudah join grup!\nIni kontennya:\n{CONTENT_LINK}",
            reply_markup=reply_markup
        )
    else:
        keyboard = [
            [InlineKeyboardButton("Join dulu", url="https://t.me/anisaaaaabot")],
            [InlineKeyboardButton("Coba Lagi", callback_data='check_join')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            "Kamu belum join grup, silakan join dulu grup berikut:",
            reply_markup=reply_markup
        )

def check_join_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id

    try:
        member = context.bot.get_chat_member(GROUP_ID, user_id)
        status = member.status
    except Exception as e:
        status = None

    if status in ['member', 'administrator', 'creator']:
        keyboard = [
            [InlineKeyboardButton("Coba Lagi", callback_data='check_join')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(
            f"Kamu sudah join grup!\nIni kontennya:\n{CONTENT_LINK}",
            reply_markup=reply_markup
        )
    else:
        keyboard = [
            [InlineKeyboardButton("Join dulu", url="https://t.me/anisaaaaabot")],
            [InlineKeyboardButton("Coba Lagi", callback_data='check_join')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(
            "Kamu belum join grup, silakan join dulu grup berikut:",
            reply_markup=reply_markup
        )

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(check_join_callback, pattern='^check_join$'))

    print("Bot started...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
