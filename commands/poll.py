from discord.ext import commands
from discord.enums import ChannelType


class PollCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="poll")
    @commands.has_permissions(administrator=True)
    async def poll(self, ctx, channelid=None, createthread=None,  *, poll=None):

        if channelid is None or poll is None or createthread is None:
            await ctx.send("Invalid Arguments! Usage: !poll <channel id> <create thread: true/false> <poll text>")
            return

        if createthread != "true" and createthread != "false":
            await ctx.send("Invalid Arguments! Usage: !poll <channel id> <create thread: true/false> <poll text>")
            return

        validchannel = False
        for channel in ctx.guild.channels:
            if channel.id == int(channelid):
                validchannel = True

        if not validchannel:
            await ctx.send("Invalid Channel! Usage: !poll <channel id> <create thread: true/false> <poll text>")
            return

        channelbackup = ctx.channel.id
        ctx.channel.id = channelid

        message = await ctx.send(poll)
        message.channel = ctx.channel

        await message.add_reaction('\N{THUMBS UP SIGN}')
        await message.add_reaction('\N{THUMBS DOWN SIGN}')
        if createthread == "true":
            thread = await message.channel.create_thread(name="Discuss!", type=ChannelType.public_thread, auto_archive_duration=1440)
            await thread.send(poll)
        ctx.channel.id = channelbackup


async def setup(bot):
    await bot.add_cog(PollCommand(bot))
