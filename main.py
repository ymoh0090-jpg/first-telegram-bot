from telegram import Update
from telegram.ext import (
Application,
CommandHandler,
MessageHandler,
ContextTypes,
filters,
)

from config import BOT_TOKEN
from handlers import (
start,
help_command,
about,
user_id,
handle_text,
)

def main() -> None:
app = Application.builder().token(BOT_TOKEN).build()

```
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("about", about))
app.add_handler(CommandHandler("id", user_id))

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        handle_text
    )
)

print("🤖 Bot is running...")

app.run_polling()
```

if **name** == "**main**":
main()
