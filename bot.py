import os
from dotenv import load_dotenv
from langgraph_sdk import get_client
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

from constants import THE_JOY_ENTRY_POINT_AGENT_NAME

# load environment variables
load_dotenv()

langgraph_client = get_client(url=os.getenv("THE_JOY_ENTRY_POINT_AGENT_URL"))


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("The Joy is online and ready.")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    await update.message.reply_chat_action(ChatAction.TYPING)

    inputs = {"messages": [{"role": "user", "content": text}]}

    result = await langgraph_client.runs.wait(
        None, THE_JOY_ENTRY_POINT_AGENT_NAME, input=inputs
    )

    await update.message.reply_text(
        result.get("messages", [])[-1].get("content", "COULD NOT PROCESS MESSAGE")
    )


if __name__ == "__main__":
    # load environment variables
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    # Initialize the application
    app = Application.builder().token(TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start_command))
    # Plain text only, not Telegram slash-commands (~COMMAND), so /start stays with CommandHandler.
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Starting polling...")
    app.run_polling()
