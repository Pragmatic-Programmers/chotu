from discord import Intents
from discord.ext import commands


intents = intents.default()

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

