import discord
from discord import embeds

from discord.ext import commands
from discord.ext.commands.core import bot_has_any_role
from Tools.utils import getconfig, updateconfig, get_prefix



class Prefix(commands.Cog):
    """Update Bot Prefix for particular guild"""
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(usage="<new-prefix>")
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def prefix(self, ctx, *args):
        if len(args) > 0:
            new_prefix = args[0]
            data = getconfig(ctx.guild.id, ctx)
            data["prefix"] = new_prefix
            updateconfig(ctx.guild.id, data)

            prefix_update_embed = discord.Embed(
                title = "**Prefix Updated ✅**",
                description = f"👶: New prefix is `{new_prefix}`",
                color = 0x00FF00    # Green
            )

            await ctx.channel.send(embed=prefix_update_embed)
        else:
            prefix_help_embed = discord.Embed(
                title = "**Set Prefix Usage**",
                description = f"👶: Looks like you need help to update prefix.\n\
                    Try this command: `{get_prefix(self.bot, ctx)}prefix` `?`\n\
                    Replace `?` with your desired prefix.",
                color = 0xFF0000    # Red
            )

            await ctx.channel.send(embed=prefix_help_embed)


def setup(bot):
    bot.add_cog(Prefix(bot))