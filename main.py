import telegram
import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler, CallbackQueryHandler

# Variáveis de ambiente
api_token = os.environ['API_TOKEN'] # Token para acesso http à api
support_chat_id = int(os.environ['SUP_CHAT_ID']) # ID do chat do grupo de suporte

# Inicialização do logger
logging.basicConfig(format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                    datefmt='%d/%m/%Y, %H:%M:%S', level=logging.DEBUG)

updater = Updater(token=token) # Conecta à API do Telegram
dispatcher = updater.dispatcher # O Updater recupera informações e o Dispatcher conecta comandos às funções

def start(bot, update):
	bot = bot.get_me()
	msg = "Olá!\n"
    msg += "Meu nome é {0}!\n".format(me.first_name)
    msg += "Estou aqui para ajudar com os negócios.\n"
    msg += "Use o comando /ajuda para exibir a lista de comandos."
    bot.send_message(chat_id=update.message.chat_id, text=msg) #Envia a mensagem para o mesmo chat de onde foi contatado. 
