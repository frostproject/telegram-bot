from .start import start, start_over
from .trial import trial
from .buy import buy
from .connect import connect

from telegram.ext import ConversationHandler, CommandHandler, CallbackQueryHandler

SELECTION, TRIAL, BUY, CONNECT, END = range(5)

conv_handler = ConversationHandler(
  entry_points=[CommandHandler("start", start)],
  states={
    SELECTION: [
      CallbackQueryHandler(trial, pattern="^TRIAL$"),
      CallbackQueryHandler(buy, pattern="^BUY$"),
      CallbackQueryHandler(connect, pattern="^CONNECT$")
    ],
    TRIAL: [
      CallbackQueryHandler(start_over, pattern="^BACK$")
    ],
    BUY: [
      CallbackQueryHandler(start_over, pattern="^BACK$")
    ],
    CONNECT: [
      CallbackQueryHandler(start_over, pattern="^BACK$")
    ],
    END: [CallbackQueryHandler(start_over, pattern="^BACK$")],
  },
  fallbacks=[CommandHandler("start", start)],
)
