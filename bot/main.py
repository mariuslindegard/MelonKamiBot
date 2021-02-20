#This is the experimental version of the bot!
import discord, datetime, os
from discord.ext import commands, tasks
from bot import utils
from termcolor import colored
#utils.config.hello_world()

#This need to stay on top of the code after the imports
print(colored('----STARTING DISCORD BOT----', 'green'))
startup_time = datetime.datetime.now()
print(startup_time.strftime("Time: %H:%M:%S"))
print()
#-----------------------------------------

prefix = "!"

def prefix(bot, message):
    return(utils.config.config['guilds'][str(message.guild.id)]['prefix'])

def format_filename(name):
    pretty_name = f"{name}"
    return pretty_name.replace('.py', '')


def space(spaces):
    for x in range(spaces):
        print()

token = utils.config.token

intents = discord.Intents.default()
bot = commands.Bot(
    command_prefix=prefix, case_insensitive=True, intents=intents)
bot.remove_command("help")


@bot.command()
async def refresh(ctx):
    for extension in os.listdir("bot/cogs"):
        if extension != "__pycache__":
            try:
                bot.reload_extension(f"bot.cogs.{format_filename(extension)}")
            except:
                bot.load_extension(f"bot.cogs.{format_filename(extension)}")


@bot.command()
async def extensions(ctx):
    await ctx.send("Extensions: \nchat_commands")
    for extension in os.listdir("bot/cogs"):
        if extension != "__pycache__":
            await ctx.send(f"bot.cogs.{format_filename(extension)}")


@bot.command()
async def unload_all_extensions(ctx):
    for extension in os.listdir("bot/cogs"):
        if extension != "__pycache__":
            bot.unload_extension(f"bot.cogs.{format_filename(extension)}")


@bot.command()
async def load_extension(ctx, extension):
    if extension in os.listdir("bot/cogs"):
        if extension != "__pycache__":
            try:
                bot.load_extension(f"bot.cogs.{format_filename(extension)}")
                await ctx.send("Extension has been successfully loaded")
            except:
                await ctx.send("This extension was already loaded")
        else:
            await ctx.send("This extension does not exist")


@bot.command()
async def unload_extension(ctx, extension):
    if extension in os.listdir("bot/cogs"):
        if extension != "__pycache__":
            try:
                bot.unload_extension(f"bot.cogs.{format_filename(extension)}")
                await ctx.send("Successfully unloaded extension")
            except:
                await ctx.send(
                    "Extension could either not be loaded, or something else went wrong"
                )
        else:
            await ctx.send("This extension does not exist")


@tasks.loop(hours=3)
async def reload_extensions():
    print("Loading/Reloading cogs")
    for extension in os.listdir("bot/cogs"):
        if extension != "__pycache__":
            try:
                bot.reload_extension(f"bot.cogs.{format_filename(extension)}")
            except:
                bot.load_extension(f"bot.cogs.{format_filename(extension)}")


@bot.event
async def on_ready():
    print(colored('----BOT HAS STARTED----', 'green'))
    bot_ready_time = datetime.datetime.now()
    print(bot_ready_time.strftime("Time: %H:%M:%S"))
    time = bot_ready_time - startup_time
    if time > datetime.timedelta(seconds=10):
        color = "red"
    else:
        color = "green"

    print(colored("Start up time:", "green"), colored(time, color))
    space(2)
    print('Logged in as {0.user}'.format(bot))
    print()
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name="Author MelonKami#6089"))

    for guild in bot.guilds:
        if str(guild.id) not in utils.config.config["guilds"]:
            utils.config.config["guilds"][str(guild.id)] = utils.config.config["guild template"]
        else:
            guild_entries = utils.config.config["guilds"][str(guild.id)].keys()
            guild_template_entries = utils.config.config["guild template"].keys()
            for entry in guild_template_entries:
                if entry not in guild_entries:
                    utils.config.config["guilds"][str(guild.id)][entry] = utils.config.config["guild template"][entry]

    utils.config.save_config()
    reload_extensions.start()


@bot.command()
async def prefix(ctx):
    await ctx.send(utils.config.config["guilds"][str(ctx.message.guild.id)]["prefix"])


def run():
    bot.run(token)
