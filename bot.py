import os
import discord
from discord import Intents
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
from rich import console
from rich.console import Console

from Tools.utils import get_prefix

console = Console()
load_dotenv()

intents = Intents.default()

bot = commands.Bot(command_prefix = get_prefix,
                   intents = intents,
                   case_insensitivity = True,
                   strip_after_prefix = True)


# Loading Cogs
for cog in os.listdir("cogs"):
    if cog.startswith("__pycache__"):
        console.log("Skipping __pycache__ folder")
    else:
        try:
            bot.load_extension(f"cogs.{cog[:-3]}")
            console.log(f"Loaded {cog[:-3]} ✅")
        except Exception as e:
            console.log(f"Failed to load {cog[:-3]}, error: {e}")

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        prefix = get_prefix(bot, message)
        await message.channel.send(prefix)
    await bot.process_commands(message)


@bot.event
async def on_ready():
    console.log(f"{bot.user} is active now ✅")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name="music 🎶🎧🤘"))

# Running the Bot
TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
