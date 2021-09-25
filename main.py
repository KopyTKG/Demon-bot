import discord
from discord import activity
from discord.ext import commands
import json

# import all of the cogs
from main_cog import main_cog
# from image_cog import image_cog
from music_cog import music_cog
from urllib.request import urlopen

main = json.load(urlopen("http://10.25.0.2/config/demon/tokens.json"))

activity = discord.Activity(type=discord.ActivityType.watching, name="d!help")

bot = commands.Bot(command_prefix='d!', activity=activity, status=discord.Status.do_not_disturb)

# remove the default help command so that we can write out own
# bot.remove_command('help')

# register the class with the bot
bot.add_cog(main_cog(bot, activity))
# # bot.add_cog(image_cog(bot))
bot.add_cog(music_cog(bot, activity))

# start the bot with our token
bot.run(main["token"])
