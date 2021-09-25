import discord
from discord.ext import commands


class main_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.text_channel_list = []

    # some debug info so that we know the bot has started
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)

    @commands.command(name="clear", help="Clears a specified amount of messages")
    async def clear(self, ctx, arg):
        # extract the amount to clear
        amount = 5
        try:
            amount = int(arg)
        except Exception:
            pass

        await ctx.channel.purge(limit=amount)
