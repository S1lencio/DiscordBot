import discord
from discord.ext import commands


class SayCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="say")
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, channelid=None, asembed=None, *, arg=None):

        if channelid is None or asembed is None or arg is None:
            await ctx.send("Invalid Arguments! Usage: !say <channel id> <as embed: true/false> <message>")
            return

        validchannel = False
        for channel in ctx.guild.channels:
            if channel.id == int(channelid):
                validchannel = True

        if not validchannel:
            await ctx.send("Invalid Channel! Usage: !say <channel id> <as embed: true/false> <message>")
            return

        if asembed != "true" and asembed != "false":
            await ctx.send("Invalid Arguments! Usage: !say <channel id> <as embed: true/false> <message>")
            return

        channelbackup = ctx.channel.id
        ctx.channel.id = channelid
        if asembed == "false":
            message = await ctx.send(arg)
        if asembed == "true":
            embed = discord.Embed(
                description=arg,
                colour=discord.Colour.blue()
            )
            await ctx.send(embed=embed)
        ctx.channel.id = channelbackup


async def setup(bot):
    await bot.add_cog(SayCommand(bot))
