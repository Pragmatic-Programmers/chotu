import wavelink
from discord.ext import commands



class Music(commands.Cog, wavelink.WavelinkMixin):
    def __init__(self, bot):
        self.bot = bot
        self.wavelink = wavelink.Client(bot = bot)
        self.bot.loop.create_task(self.start_nodes())
    

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        # Bot Disconnects cuz no one is there in channel
        if not member.bot and after.channel is None:
            if not [member for member in before.channel.members if not member.bot]:
                pass
    

    @wavelink.WavelinkMixin.listener()
    async def on_node_ready(self, node):
        print(f"{node.identifier} Wavelink node is active ✅")
    

    async def cog_check(self, ctx):
        if isinstance(ctx.channel, discord.DMChannel):
            # Respond to message in DM
            await ctx.send("Can't play music here you dumb!")
            return False

        return True
