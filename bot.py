import os
import discord
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = Intents.default()

bot = commands.Bot(command_prefix = "chotu",
                   intents = intents,
                   case_insensitivity = True,
                   strip_after_prefix = True)


cogs = {

}


def load_cogs(cogs: dict) -> None:
    """ Function to load cogs from dict """
    for key, value in cogs.item():
        try:
            bot.load_extension(value)
            print(f"Loaded {key}!")
        except Exception as e:
            print(f"Some error occured while loading {key}")
            print(f"Error: {e}")

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send('My Prefix is : `chotu`')


@bot.event
async def on_ready():
    print(f"{bot.user} is active now ✅")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name="music 🎶🎧🤘"))

# Running the Bot
TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
