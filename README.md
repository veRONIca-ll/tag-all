# tag-all
a telegram bot which allows you to tag all users of chat at once 

### main file -> bot.py
Computing all the commands: 
* /start - a simple greeting
* /help - a list of all available commands
* /register - to register all users of the chat
* /all - to tag all registered users

All registered users are being written in json file.
All configurations for the bot should be writen in "config.py".
The example of the structure of config.py are "config.example".

### printing logs -> log.py
All logs from commands are in "log.py" file, if you do not want logs from bot just do no use this file and delete (or comment) lines in "bot.py" where "#logs" is writen.

### json_functions
It is a small library for writing users' nicknames or getting ones. 
