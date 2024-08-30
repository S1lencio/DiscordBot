import os

import yaml
from discord.ext import commands


class MemberJoinEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yml')), "r") as f:
            config = yaml.safe_load(f)

        if config['autorole'] is not None:
            role = member.guild.get_role(int(config['autorole']))
            await member.add_roles(role)
        print(f"{member.name} has joined the server.")

async def setup(bot):
    await bot.add_cog(MemberJoinEvent(bot))
