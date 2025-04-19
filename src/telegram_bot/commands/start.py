from utils.translations import en
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

SELECTION, TRIAL, BUY, CONNECT, END = range(5)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  await start_base(update, context)
  return SELECTION

async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  query = update.callback_query
  await query.answer()
  await start_base(update, context, query=query)
  return SELECTION

async def start_base(update: Update, context: ContextTypes.DEFAULT_TYPE, query=None) -> int:
  keyboard = [
    [InlineKeyboardButton(en.getTrial_button(), callback_data="TRIAL")],
    [InlineKeyboardButton(en.getBuy_button(), callback_data="BUY")],
    [InlineKeyboardButton(en.getConnect_button(), callback_data="CONNECT")],
    [InlineKeyboardButton(en.getSupport_button(), url="https://t.me/iceeburr")],
    [InlineKeyboardButton(en.getChannel_button(), url="https://t.me/frostproject_news")],
  ]
  reply_markup = InlineKeyboardMarkup(keyboard)
  if query != None:
    await query.edit_message_text(
      en.getGreeting(),
      parse_mode=ParseMode.MARKDOWN_V2,
      reply_markup=reply_markup,
    )
  else:
    await update.message.reply_markdown_v2(
      en.getGreeting(),
      reply_markup=reply_markup,
    )
