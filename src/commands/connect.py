from utils.translations import en
from utils.remnawave import User

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

SELECTION, TRIAL, BUY, CONNECT, END = range(5)

async def connect(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  query = update.callback_query
  await query.answer()
  keyboard = [
    [InlineKeyboardButton(en.getBack_button(), callback_data="BACK")]
  ]
  reply_markup=InlineKeyboardMarkup(keyboard)
  user = User(telegramId=update.effective_user.id)
  text = en.getNo_subscription()
  if user.getSubscriptionUrl() != None:
    text = (en.getSubscription_active() % user.getExpireAt()) + (en.getSubscription_link() % user.getSubscriptionUrl())
  await query.edit_message_text(
    text,
    parse_mode=ParseMode.MARKDOWN_V2,
    reply_markup=reply_markup
  )
  return CONNECT
