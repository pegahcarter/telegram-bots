from flask import Flask, request
import telegram
from api import bot_token, bot_username, URL


bot = telegram.Bot(token=bot_token)


# Start the flask app
app = Flask(__name__)


# Have bot response to messages
@app.route(f'/{token}', methods=['POST'])
def respond():

    # Retrieve the message in JSON and transform into Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    message = update.message.text.encode('utf-8').decode()
    if message == '/run':
        param = {
            'chat_id': update.message.chat.id,
            'reply_to_message_id': update.message.message_id
        }
        bot.sendMessage(text=f"Can't catch me!", **param)


# 
