import datetime as d

def info_of_user(msg) -> str:
    return f'\
        user: {msg.from_user.username}\n \
        id: {msg.chat.id}\n \
        date: {d.datetime.now()}\n\n \
        text: {msg.text} \
    '


def start_log(msg)  -> str:
    return '--START LOG--\n' + f'{info_of_user(msg)}'

def help_log(msg) -> str:
    return '--HELP LOG--\n' + f'{info_of_user(msg)}'

def register_log(msg, result: str) -> str:
    return '--REGISTER LOG--\n' + f'{info_of_user(msg)}\n\n' + f'{result}'

def all_log(msg, result):
    return '--ALL LOG--\n' + f'{info_of_user(msg)}\n\n' + f'{result}'


