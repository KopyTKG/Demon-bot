import discord
from discord.ext.commands import *
from discord.ext import commands
from discord import *


class main_cog(commands.Cog):
    def __init__(self, bot, activity):
        self.bot = bot
        self.activity = activity

        self.text_channel_list = []

    # some debug info so that we know the bot has started
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)
        print("Ready to play")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, exc):
        author = ctx.author.mention
        if isinstance(exc, commands.CommandNotFound):
            await ctx.send(f"{author} {exc}.")
        elif isinstance(exc, commands.MissingRequiredArgument):
            await ctx.send(f"{author} {exc}")
        else:
            print(exc)
