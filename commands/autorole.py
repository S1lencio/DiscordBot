import os

from discord.ext import commands
import yaml


class AutoroleCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="autorole")
    @commands.has_permissions(administrator=True)
    async def autorole(self, ctx, role=None):
        if role is None:
            await ctx.send("Invalid Arguments! Usage: !autorole <role id>")
            return

        with open(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yml')), "r") as f:
            config = yaml.safe_load(f)

        data = {'autorole': role.replace("<@&", "").replace(">", "")}

        with open(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yml')), "w") as f:
            yaml.dump(data, f)

        print("autorole set")
        await ctx.send(f"Autorole set to {role}.")
        print("autorole set x2")


async def setup(bot):
    await bot.add_cog(AutoroleCommand(bot))
