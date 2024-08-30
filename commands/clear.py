from discord.ext import commands


class ClearCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clear")
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount=None):
        if amount is None:
            await ctx.send("Invalid Arguments! Usage: !clear <amount>")
            return
        await ctx.send("Sorry mate this is broken and I have no clue why, the worst bugs are those without errors or stacktraces...")
        return

        #ctx.channel.id.purge(limit=amount+1)
        #message = await ctx.send(f"Cleared {amount} messages.")
        #await message.delete(delay=3)


async def setup(bot):
    await bot.add_cog(ClearCommand(bot))
