import logging
import json

from commands.convo import conv_handler

from utils.environment import conf
from utils.translations import en
from telegram import ForceReply, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ConversationHandler, ContextTypes, MessageHandler, filters

logging.basicConfig(
  format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

def main() -> None:
  application = Application.builder().token(conf.getToken()).build()
  application.add_handler(conv_handler)
  application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
  main()
