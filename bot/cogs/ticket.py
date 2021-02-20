import datetime, discord
from discord.ext import commands, tasks
from discord.utils import get
from bot import utils


def create_embed(title, description: str = None, url: str = None):
    embed = discord.Embed(title=title, description=description)
    embed.set_footer(text='Ticket - MelonKami Bot')
    embed.url = url
    embed.timestamp = datetime.datetime.now()
    return embed


class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('Ticket cog has been loaded')

    @commands.command()
    async def ticket(self, ctx):
        await ctx.message.delete(delay=30)

        if utils.config.config["guilds"][str(
                ctx.guild.id)]["ticket_active"] != True:
            message = await ctx.send(
                'Ticket system is currently disabled, please contact owner if this is a problem'
            )
            await message.delete(delay=30)
        else:
            tickets = 0
            tickets_array = []
            ticket_category = discord.utils.get(ctx.guild.categories,
                                                name='Tickets 📩')

            support_message = (
                f'Hello {ctx.message.author.mention}, welcome to Support! ' +
                f'This ticket is now set to archieve in {utils.config.config["guilds"][str(ctx.message.guild.id)]["due_time"]} days after the last message has been sent, keep in mind that this duetime can change anytime, without you being notified. '
                +
                'After it has been archieved it will be stored for up to 30 days before it gets deleted by the bot. \n\n```Please explain your issue to staff, so they can help you as soon as possible.```'
            )

            for channel in ticket_category.text_channels:
                if channel.name == f'ticket-{ctx.message.author.id}':
                    tickets += 1
                    tickets_array.append(channel)
                if tickets > 2:
                    message_embed = create_embed(
                        'Open tickets', 'Please refer to one of these')

                    for ticket in tickets_array:
                        message_embed.add_field(name='Open ticket',
                                                value=ticket.mention)
                    message = await ctx.send(
                        f'{ctx.message.author.mention}: You already have 3 open tickets, please refer to one of these',
                        embed=message_embed)
                    await message.delete(delay=30)
                    break
            else:
                ticket_create_overwrites = {
                    ctx.guild.default_role:
                    discord.PermissionOverwrite(read_messages=False),
                    ctx.message.author:
                    discord.PermissionOverwrite(read_messages=True,
                                                send_messages=False)
                }
                kanal = await ctx.guild.create_text_channel(
                    f'ticket-{ctx.message.author.id}',
                    overwrites=ticket_create_overwrites,
                    category=ticket_category)

                def check(m):
                    return m.channel == kanal and m.author.id == ctx.message.author.id

                def reaction_check(reaction, user):
                    return user == ctx.message.author

                config_message = await kanal.send(embed=create_embed(
                    f'Hello {ctx.message.author.display_name}, welcome to support',
                    support_message))
                message = await ctx.send(
                    f'Your ticket was created  {ctx.message.author.mention}!')
                await message.delete(delay=30)
                issue = await self.bot.wait_for('message', check=check)
                await config_message.delete()
                await issue.delete()
                await kanal.send(embed=create_embed(
                    ctx.message.author.display_name,
                    f'Issue to be resolved: \n{issue.content}'))


def setup(bot):
    bot.add_cog(Ticket(bot))
