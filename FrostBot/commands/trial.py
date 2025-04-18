from utils.translations import en
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

SELECTION, TRIAL, BUY, CONNECT, END = range(5)

async def trial(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  query = update.callback_query
  await query.answer()
  keyboard = [
    [InlineKeyboardButton(en.getActivate_trial_button(), callback_data="ACTIVATE_TRIAL")],
    [InlineKeyboardButton(en.getBack_button(), callback_data="BACK")]
  ]
  reply_markup=InlineKeyboardMarkup(keyboard)
  await query.edit_message_text(
    text=en.getTrial_text(),
    parse_mode=ParseMode.MARKDOWN_V2,
    reply_markup=reply_markup
  )
  return TRIAL
