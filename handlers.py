from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

MENU_KEYBOARD = ReplyKeyboardMarkup(
[
["👋 Hello", "ℹ️ About"],
["🆔 My ID", "❓ Help"],
["🏓 Ping"],
],
resize_keyboard=True
)

async def start(
update: Update,
context: ContextTypes.DEFAULT_TYPE
) -> None:
user = update.effective_user

```
await update.message.reply_text(
    f"Hello {user.first_name}! 👋\n\n"
    "Welcome to my first Telegram bot!\n\n"
    "Use the buttons below or type /help "
    "to see the available commands.",
    reply_markup=MENU_KEYBOARD
)
```

async def help_command(
update: Update,
context: ContextTypes.DEFAULT_TYPE
) -> None:
await update.message.reply_text(
"❓ <b>Available Commands</b>\n\n"
"/start - Start the bot\n"
"/help - Show available commands\n"
"/about - About the bot\n"
"/id - Show your Telegram ID\n"
"/ping - Check if the bot is online\n"
"/echo <text> - Repeat your message\n\n"
"You can also send a normal text message.",
parse_mode="HTML"
)

async def about(
update: Update,
context: ContextTypes.DEFAULT_TYPE
) -> None:
await update.message.reply_text(
"ℹ️ <b>About This Bot</b>\n\n"
"This is my first Telegram bot project built with Python.\n\n"
"Technologies:\n"
"🐍 Python\n"
"🤖 python-telegram-bot"
)

async def user_id(
update: Update,
context: ContextTypes.DEFAULT_TYPE
) -> None:
user = update.effective_user

```
await update.message.reply_text(
    f"🆔 <b>Your Telegram ID:</b>\n\n"
    f"{user.id}",
    parse_mode="HTML"
)
```

async def ping(
update: Update,
context: ContextTypes.DEFAULT_TYPE
) -> None:
await update.message.reply_text(
"🏓 Pong! The bot is online."
)

async def echo(
update: Update,
context: ContextTypes.DEFAULT_TYPE
) -> None:
if not context.args:
await update.message.reply_text(
"❌ Please provide a message.\n\n"
"Example:\n"
"/echo Hello world"
)
return

```
message = " ".join(context.args)

await update.message.reply_text(
    f"🔁 {message}"
)
```

async def handle_text(
update: Update,
context: ContextTypes.DEFAULT_TYPE
) -> None:
text = update.message.text

```
if text == "👋 Hello":
    await update.message.reply_text(
        "👋 Hello!\nNice to meet you."
    )
    return

if text == "ℹ️ About":
    await about(update, context)
    return

if text == "🆔 My ID":
    await user_id(update, context)
    return

if text == "❓ Help":
    await help_command(update, context)
    return

if text == "🏓 Ping":
    await ping(update, context)
    return

await update.message.reply_text(
    f"📩 You said:\n\n{text}"
)
```
