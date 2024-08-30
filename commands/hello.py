from discord.ext import commands


class HelloCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hello")
    @commands.has_permissions(administrator=True)
    async def hello(self, ctx, *, arg=None):
        if arg is None:
            await ctx.send("Hello. I am Fluxbot and I want to assist you in your tasks.")
        else:
            await ctx.send(f"Hello. I am Fluxbot and I want to assist you in your tasks. Also, you said {arg}.")


async def setup(bot):
    await bot.add_cog(HelloCommand(bot))
