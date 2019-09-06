import telegram
import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler, CallbackQueryHandler

# Variáveis de ambiente
api_token = os.environ['API_TOKEN'] # Token para acesso http à api
support_chat_id = int(os.environ['SUP_CHAT_ID']) # ID do chat do grupo de suporte
