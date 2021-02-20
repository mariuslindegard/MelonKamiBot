#Here are all the basic chat commads
from discord.ext import commands
from bot import utils


class ChatCommands(commands.Cog):
    def __init__(self, bot):
        print("Chat commands Cog loaded")
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        for command in utils.config.config["guilds"][str(
                msg.guild.id)]["commands"]:
            if command == msg.content:
                await msg.channel.send(utils.config.config["guilds"][str(
                    msg.guild.id)]["commands"][msg.content])

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def add_command(self, ctx, command_name: str, *, command_desc: str):
        utils.config.config["guilds"][str(
            ctx.message.guild.id)]["commands"][command_name] = command_desc
        utils.config.save_config()
        await ctx.send(f"Added command {command_name}")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, limit=5):
        deleted = await ctx.channel.purge(limit=limit + 1)
        count = len(deleted)
        count -= 1
        if limit != count:
            message = await ctx.send(
                f"Bot tried to delete __**{limit}**__, but could only delete __**{count}**__ messages"
            )
        else:
            message = await ctx.send(f"Bot deleted __**{count}**__ messages")

        await message.delete(delay=5)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Command has been registered")

    @commands.command()
    async def test(self, ctx):
        await ctx.send("test")


def setup(bot):
    bot.add_cog(ChatCommands(bot))
