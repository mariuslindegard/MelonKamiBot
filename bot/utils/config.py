import codecs, json
from termcolor import colored
from os import path

class Config():
    def __init__(self):
        if path.exists('config.json') == False:
            print(colored("First Launch mode: \nHello, welcome to the bot's setup. To get started with the bot, you need to input your token, then the prefix you want to be the standard prefix for the bot to use!", "green"))
            print()
            input_token = input("Token: ")
            print()
            input_prefix = input("Prefix: ")
            print()

            guild_template = {
                    "prefix": str(input_prefix),
                    "commands": {},
                    "ticket_active": False,
                    "voice_channel_active": False,
                    "music": {},
                    "reminders": {},
                    "due_time": 3
            }

            with open('config.json', 'x') as File:
                json.dump({"token": input_token, "guild template": guild_template, "guilds": {}}, File, indent=4)

        with codecs.open('config.json','r', encoding='utf-8-sig') as File:
            self.config = json.load(File)
        self.token = self.config["token"]

    def save_config(self):
            with codecs.open('config.json', 'w', encoding='utf8') as File:
                json.dump(self.config, File, sort_keys=True, indent=4, ensure_ascii=False)
