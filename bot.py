import os

from dotenv import load_dotenv
from discord import *
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = discord.Bot()

# Command Handling Goes Here

bot.run(TOKEN)