from utils.translations import en
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

SELECTION, TRIAL, BUY, CONNECT, END = range(5)

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  query = update.callback_query
  await query.answer()
  keyboard = [
    [InlineKeyboardButton(en.getMonth_1(), callback_data="MONTH_1"), InlineKeyboardButton(en.getMonth_3(), callback_data="MONTH_3"), InlineKeyboardButton(en.getMonth_6(), callback_data="MONTH_6")],
    [InlineKeyboardButton(en.getBack_button(), callback_data="BACK")]
  ]
  reply_markup=InlineKeyboardMarkup(keyboard)
  await query.edit_message_text(
    en.getPricing_info(),
    parse_mode=ParseMode.MARKDOWN_V2,
    reply_markup=reply_markup
  )
  return BUY
