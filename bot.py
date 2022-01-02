import telebot
import datetime as d
import config
import json_functions as json

bot = telebot.TeleBot(config.telebot_token)

def info_of_user(msg):
    return f'\
                user: {msg.from_user.username}\n \
                id: {msg.chat.id}\n \
                date: {d.datetime.now()}\n\n \
                text: {msg.text} \
            '

def register_users(msg):
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
    if users != []:
        return ' '.join(users)
    else:
        return config.sorry_message


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, text = config.greeting)
    bot.send_message(chat_id=config.chat_for_logs, text='--LOG--\n' + f'{info_of_user(message)}')

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(chat_id=message.chat.id, text=config.help)

@bot.message_handler(commands=['register'])
def register_message(message):
    bot.send_message(chat_id=message.chat.id, text=register_users(message))


@bot.message_handler(commands=['all'])
def all(message):
    bot.send_message(chat_id=config.chat_for_logs, text='--LOG--\n' + f'{json.get_by_id(config.filename, str(message.chat.id))}')
    bot.send_message(chat_id=message.chat.id, text=to_text(json.get_by_id(config.filename, str(message.chat.id))))


if __name__ == '__main__':
    bot.polling()