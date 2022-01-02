import telebot
import config
import logs
import json_functions as json

bot = telebot.TeleBot(config.telebot_token)

def register_users(msg):
    ''' function to write registered users in json file '''
    users = list()

    for user in msg.text.split(' '):
        if '/' in user:
            continue
        elif '@' not in user:
            users.append(f'@{user}')
        else:
            users.append(user)

    data = {
        msg.chat.id : users
    }

    if json.write_to(config.filename, data):
        return config.success_register

    return config.failed_register
    

def to_text(users: list) -> str:
    ''' function to convert from list to string '''
    if users != []:
        return ' '.join(users)
    else:
        return config.sorry_message


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, text = config.greeting)
    bot.send_message(chat_id=config.chat_for_logs, text=logs.start_log(message)) # logs

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(chat_id=message.chat.id, text=config.help)
    bot.send_message(chat_id=config.chat_for_logs, text=logs.help_log(message)) # logs

@bot.message_handler(commands=['register'])
def register_message(message):
    result = register_users(message)
    bot.send_message(chat_id=message.chat.id, text=result)
    bot.send_message(chat_id=config.chat_for_logs, text=logs.register_log(message, result)) # logs


@bot.message_handler(commands=['all'])
def all(message):
    bot.send_message(chat_id=message.chat.id, text=to_text(json.get_by_id(config.filename, str(message.chat.id))))
    if to_text(json.get_by_id(config.filename, str(message.chat.id))) == config.sorry_message: # logs
        bot.send_message(chat_id=config.chat_for_logs, text=logs.all_log(message, 'failed'))



if __name__ == '__main__':
    bot.polling()