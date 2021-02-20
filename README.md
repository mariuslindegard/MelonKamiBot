# MelonKami Bot

### Feel free to use my bot as your own

MelonKami Bot is a plug and play type off bot, all you need is a working version of Python, the latest version is often the best, and you need to have `pip` on path, this will normally be done in the installation. You can test to see if you have `pip` on path by doing `pip` in console, if no error appears, you have a working pip path and everything is good, now over to the installation. Simply clone it and all you have to do is download the modules it requires ref-[packages you'll need to install](https://github.com/MelonKami/MelonKamiBot#packages-the-bot-uses), and it'll ask you for the token and prefix, and setup itself. I made this so anyone who wants a bot, can have one. 

If you want to use this bot as your own, simply clone the repo or download it. When you launch it first time it has a setup. It will ask you for a token, and after that it will be working, you can change this later (read configuration notes). Hope you enjoy my bot :D

## Features the bot has

| Features      | Description |
| ----------- | ----------- |
| Custom commands  | This bot features a custom command system, you can easily create a command by doing !add_command <Syntaxchoice: Command_name - command_description>      |
| Clear   | You can easily purge messages by doing !clear <amount>        |
| Tickets | You can have a smart ticket system by doing !toggle_tickets. This will then create a ticket category where users can create a ticket for themselves to staff by doing !ticket The ticket system will automatically delete the ticket after a certain time, this can be changed via command- !change_due_time. After a ticket is closed it will end up in a ticket archieve, where a script will determend when it will be deleted. Max time is 30 days, but it will delete it faster if there is a lot of tickets|
| Voice Channel Creator | By doing !toggle_voice_channel the bot will create a category featuring 5 channels, one public and one private, where if you join one of these the bot will create a channel for that person, more instructions is given when you execute the command|

## Packages the bot uses

To install the packages, simply do `pip install .`, and if this for some reason won't work, here is the packages, and the pip installments

> discord.py (`pip install discord.py`)
>
> termcolor (`pip install termcolor`)

## Important Notes

* As of now, there are no important notes, if you have any questions check `Configuration notes`, if you can't find your question answer there, you can create an issue on the repo.

## Configuration notes
  
* Want to change something in the configuration file? The configuration file is the file that stores data for the bot, for example your token and prefix is stored there, now if you inputted the wrong token, you can head over to `config.json` and change what you need there. You should turn off the bot when doing this to:

    * Not generate error.

    * Not overwrite what has been changed: the bot won't recognize a change, and it could potentially overwrite your change if it is running.

* But be careful with what you mess with, because you could end up breaking the bot. If this happens, you can simply delete the `config.json`file (keep in mind that this will delete all data), and next time you start the bot, it will launch in `first launch` mode. It will then ask for token and prefix again!