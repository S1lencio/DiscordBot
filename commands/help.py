import discord
from discord.ext import commands


class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    @commands.has_permissions(administrator=True)
    async def help(self, ctx,):
        embed = discord.Embed(
            title="Help page for Fluxbot",
            colour=discord.Colour.blue(),
        )
        embed.add_field(name="!Hello", value="Ping command to test the bots' connection.", inline=True)
        embed.add_field(name="!say", value="Make the bot say something, in a provided channel. Has the option to be sent in an embed.", inline=True)
        embed.add_field(name="!poll", value="Create a poll in a provided channel. Can be created with a discussion thread.", inline=True)
        embed.add_field(name="!reactionrole", value="Add a reaction role to a message. Requires a channel ID, message ID, emoji and role.", inline=True)
        embed.add_field(name="!autorole", value="Set the autorole for a server. Requires a role ID.", inline=True)
        embed.add_field(name="!clear", value="Clear a certain amount of messages in a channel. Will clear 100 Messages by default, but this value can be changed by adding an argument.", inline=True)

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(HelpCommand(bot))
