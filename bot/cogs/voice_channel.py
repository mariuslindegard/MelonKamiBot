import discord, datetime
from discord.ext import commands, tasks
from bot import utils

def create_embed(title, description: str = None, url: str = None):
    embed = discord.Embed(title=title, description=description)
    embed.set_footer(text='Voice Channel - MelonKami Bot')
    embed.url = url
    embed.timestamp = datetime.datetime.now()
    return embed


class VoiceChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.voice_chat.start()
        print('Voice channel Cog loaded')

    @tasks.loop(seconds=5)
    async def voice_chat(self):
        members = 0
        for guild in self.bot.guilds:
            if utils.config.config["guilds"][str(guild.id)]["voice_channel_active"]:
                for category in guild.categories:
                    if category.name == 'Voice Chats':
                        voice_chats_category = category
                        for channel in category.voice_channels:
                            for member in channel.members:
                                members += 1
                            if len(channel.members) == 0:
                                await channel.delete()
                for channel in guild.voice_channels:
                    if channel.name == 'Duo Chat - Private':
                        for member in channel.members:
                            overwrites = {
                                guild.default_role: discord.PermissionOverwrite(connect=False, view_channel=False),
                                self.bot.user: discord.PermissionOverwrite(connect=True, view_channel=True, manage_channels=True),
                                member: discord.PermissionOverwrite(connect=True, view_channel=True, speak=True, mute_members=True)
                                }
                            private_voice_chat = await guild.create_voice_channel(f'{member.display_name}\'s Private Duo chat!', user_limit=2, overwrites=overwrites, category=voice_chats_category)
                            await member.move_to(private_voice_chat)
                    elif channel.name == 'Trio Chat - Private':
                        for member in channel.members:
                            overwrites = {
                                guild.default_role: discord.PermissionOverwrite(connect=False, view_channel=False),
                                self.bot.user: discord.PermissionOverwrite(connect=True, view_channel=True, manage_channels=True),
                                member: discord.PermissionOverwrite(connect=True, view_channel=True, speak=True, mute_members=True)
                                }
                            private_voice_chat = await guild.create_voice_channel(f'{member.display_name}\'s Private Trio chat!', user_limit=3, overwrites=overwrites, category=voice_chats_category)
                            await member.move_to(private_voice_chat)
                    elif channel.name == 'Four Squad Chat - Private':
                        for member in channel.members:
                            overwrites = {
                                guild.default_role: discord.PermissionOverwrite(connect=False, view_channel=False),
                                self.bot.user: discord.PermissionOverwrite(connect=True, view_channel=True, manage_channels=True),
                                member: discord.PermissionOverwrite(connect=True, view_channel=True, speak=True, mute_members=True)
                                }
                            private_voice_chat = await guild.create_voice_channel(f'{member.display_name}\'s Private Four Squad chat!', user_limit=4, overwrites=overwrites, category=voice_chats_category)
                            await member.move_to(private_voice_chat)
                    elif channel.name == 'Squad Chat - Private':
                        for member in channel.members:
                            overwrites = {
                                guild.default_role: discord.PermissionOverwrite(connect=False, view_channel=False),
                                self.bot.user: discord.PermissionOverwrite(connect=True, view_channel=True, manage_channels=True),
                                member: discord.PermissionOverwrite(connect=True, view_channel=True, speak=True, mute_members=True)
                                }
                            private_voice_chat = await guild.create_voice_channel(f'{member.display_name}\'s Private Squad chat!', user_limit=5, overwrites=overwrites, category=voice_chats_category)
                            await member.move_to(private_voice_chat)
                    elif channel.name == '10 people Chat - Private':
                        for member in channel.members:
                            overwrites = {
                                guild.default_role: discord.PermissionOverwrite(connect=False, view_channel=False),
                                self.bot.user: discord.PermissionOverwrite(connect=True, view_channel=True, manage_channels=True),
                                member: discord.PermissionOverwrite(connect=True, view_channel=True, speak=True, mute_members=True)
                                }
                            private_voice_chat = await guild.create_voice_channel(f'{member.display_name}\'s Private 10 people Chat', user_limit=10, overwrites=overwrites, category=voice_chats_category)
                            await member.move_to(private_voice_chat)
                    elif channel.name == '10+ people Chat - Private':
                        for member in channel.members:
                            overwrites = {
                                guild.default_role: discord.PermissionOverwrite(connect=False, view_channel=False),
                                self.bot.user: discord.PermissionOverwrite(connect=True, view_channel=True, manage_channels=True),
                                member: discord.PermissionOverwrite(connect=True, view_channel=True, speak=True, mute_members=True)
                                }
                            private_voice_chat = await guild.create_voice_channel(f'{member.display_name}\'s Private 10 people Chat', overwrites=overwrites, category=voice_chats_category)
                            await member.move_to(private_voice_chat)

                    #Public Rooms

                    if channel.name == 'Duo Chat - Public':
                        for member in channel.members:
                            overwrites = {
                                guild.default_role: discord.PermissionOverwrite(connect=True, view_channel=True, speak=True),
                                self.bot.user: discord.PermissionOverwrite(connect=True, view_channel=True, manage_channels=True),
                                member: discord.PermissionOverwrite(connect=True, view_channel=True, speak=True, mute_members=True)
                                }
                            private_voice_chat = await guild.create_voice_channel(f'{member.display_name}\'s Public Duo chat!', user_limit=2, overwrites=overwrites, category=voice_chats_category)
                            await member.move_to(private_voice_chat)
                    elif channel.name == 'Trio Chat - Public':
                        for member in channel.members:
                            overwrites = {
                                guild.default_role: discord.PermissionOverwrite(connect=True, view_channel=True, speak=True),
                                self.bot.user: discord.PermissionOverwrite(connect=True, view_channel=True, manage_channels=True),
                                member: discord.PermissionOverwrite(connect=True, view_channel=True, speak=True, mute_members=True)
                                }
                            private_voice_chat = await guild.create_voice_channel(f'{member.display_name}\'s Public Trio chat!', user_limit=3, overwrites=overwrites, category=voice_chats_category)
                            await member.move_to(private_voice_chat)
                    elif channel.name == 'Four Squad Chat - Public':
                        for member in channel.members:
                            overwrites = {
                                guild.default_role: discord.PermissionOverwrite(connect=True, view_channel=True, speak=True),
                                self.bot.user: discord.PermissionOverwrite(connect=True, view_channel=True, manage_channels=True),
                                member: discord.PermissionOverwrite(connect=True, view_channel=True, speak=True, mute_members=True)
                                }
                            private_voice_chat = await guild.create_voice_channel(f'{member.display_name}\'s Public Four Squad chat!', user_limit=4, overwrites=overwrites, category=voice_chats_category)
                            await member.move_to(private_voice_chat)
                    elif channel.name == 'Squad Chat - Public':
                        for member in channel.members:
                            overwrites = {
                                guild.default_role: discord.PermissionOverwrite(connect=True, view_channel=True, speak=True),
                                self.bot.user: discord.PermissionOverwrite(connect=True, view_channel=True, manage_channels=True),
                                member: discord.PermissionOverwrite(connect=True, view_channel=True, speak=True, mute_members=True)
                                }
                            private_voice_chat = await guild.create_voice_channel(f'{member.display_name}\'s Public Squad chat!', user_limit=5, overwrites=overwrites, category=voice_chats_category)
                            await member.move_to(private_voice_chat)
                    elif channel.name == '10 people Chat - Public':
                        for member in channel.members:
                            overwrites = {
                                guild.default_role: discord.PermissionOverwrite(connect=True, view_channel=True, speak=True),
                                self.bot.user: discord.PermissionOverwrite(connect=True, view_channel=True, manage_channels=True),
                                member: discord.PermissionOverwrite(connect=True, view_channel=True, speak=True, mute_members=True)
                                }
                            private_voice_chat = await guild.create_voice_channel(f'{member.display_name}\'s Public 10 people Chat', user_limit=10, overwrites=overwrites, category=voice_chats_category)
                            await member.move_to(private_voice_chat)
                    elif channel.name == '10+ people Chat - Public':
                        for member in channel.members:
                            overwrites = {
                                guild.default_role: discord.PermissionOverwrite(connect=True, view_channel=True, speak=True),
                                self.bot.user: discord.PermissionOverwrite(connect=True, view_channel=True, manage_channels=True),
                                member: discord.PermissionOverwrite(connect=True, view_channel=True, speak=True, mute_members=True)
                                }
                            private_voice_chat = await guild.create_voice_channel(f'{member.display_name}\'s Public 10 people Chat', overwrites=overwrites, category=voice_chats_category)
                            await member.move_to(private_voice_chat)


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def toggle_voice_chat(self, ctx):
        utils.config.config['guilds'][str(ctx.guild.id)]['voice_channel_active'] = not utils.config.config['guilds'][str(ctx.guild.id)]['voice_channel_active']
        voice_chat = utils.config.config['guilds'][str(ctx.guild.id)]['voice_channel_active']

        does_category_exist = False
        if voice_chat:
            await ctx.send('Voice system has been activated \nCreating two categories - Voice Chat Maker - Custom Voice Chats')
            #Searching for 'Ticket' category
            for category in ctx.guild.categories:
                if category.name == 'Voice Chat maker':
                    does_category_exist = True
                    break
            if not does_category_exist:
                overwrites = {
                    ctx.guild.default_role: discord.PermissionOverwrite(connect=True, read_messages=True, send_messages=True),
                    self.bot.user: discord.PermissionOverwrite(connect=True, view_channel=True, manage_channels=True)
                    }
                label_overwrites = {
                    ctx.guild.default_role: discord.PermissionOverwrite(connect=False, view_channel=True),
                    self.bot.user: discord.PermissionOverwrite(connect=True, view_channel=True, manage_channels=True)
                }
                voice_chat_maker = await ctx.guild.create_category('Voice Chat Maker', overwrites=overwrites)
                voice_chat_commands = await ctx.guild.create_text_channel('voice-chat-commands', category=voice_chat_maker )
                await ctx.guild.create_voice_channel('-------Private Rooms--------', category=voice_chat_maker, overwrites=label_overwrites)
                await ctx.guild.create_voice_channel('Duo Chat - Private', category=voice_chat_maker)
                await ctx.guild.create_voice_channel('Trio Chat - Private', category=voice_chat_maker)
                await ctx.guild.create_voice_channel('Four Squad Chat - Private', category=voice_chat_maker)
                await ctx.guild.create_voice_channel('Squad Chat - Private', category=voice_chat_maker)
                await ctx.guild.create_voice_channel('10 people Chat - Private', category=voice_chat_maker)
                await ctx.guild.create_voice_channel('10+ people Chat - Private', category=voice_chat_maker)
                await ctx.guild.create_voice_channel('-------Public Rooms--------', category=voice_chat_maker, overwrites=label_overwrites)
                await ctx.guild.create_voice_channel('Duo Chat - Public', category=voice_chat_maker)
                await ctx.guild.create_voice_channel('Trio Chat - Public', category=voice_chat_maker)
                await ctx.guild.create_voice_channel('Four Squad Chat - Public', category=voice_chat_maker)
                await ctx.guild.create_voice_channel('Squad Chat - Public', category=voice_chat_maker)
                await ctx.guild.create_voice_channel('10 people Chat - Public', category=voice_chat_maker)
                await ctx.guild.create_voice_channel('10+ people Chat - Public', category=voice_chat_maker)            
                await voice_chat_commands.send(embed=create_embed('Voice Chats!', 'Here you can add your friends into your Private rooms, by simply doing __**!add_voice_chat @Friend**__, ' +
                'but if you\'re creating a public room, you don\'t need to invite, because everyone can join it!' +
                '\nSo what are you waiting for, get into a room with your friends!'))

            #Searching for 'Ticket Archieve' catehory
            does_category_exist = False
            for category in ctx.guild.categories:
                if category.name == 'Voice Chats':
                    does_category_exist = True
                    break
            if not does_category_exist:
                overwrites = {
                    ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, view_channel=False),
                    self.bot.user: discord.PermissionOverwrite(connect=True, view_channel=True, manage_channels=True)
                    }
                await ctx.guild.create_category('Voice Chats', overwrites=overwrites)

        else:
            await ctx.send('``Deleting active Voice Chats`` \n``Voice chats has been deactivated``')  
            for category in ctx.guild.categories:
                if category.name == 'Voice Chat Maker':
                    for channel in category.text_channels:
                        await channel.delete()
                    for channel in category.voice_channels:
                        await channel.delete()
                    await category.delete()
                elif category.name == 'Voice Chats':
                    for channel in category.voice_channels:
                        await channel.delete()
                    await category.delete()

        utils.config.save_config()


def setup(bot):
    bot.add_cog(VoiceChannel(bot))
