import json
import os
import hashlib

import discord
from discord import RawReactionActionEvent
from discord.ext import commands


class ReactionRoleCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Create Reactions
    @commands.command(name="reactionrole")
    @commands.has_permissions(administrator=True)
    async def reactionrole(self, ctx, channelid=None, messageid=None, emoji=None, giverole=None):

        if channelid is None or messageid is None or emoji is None or giverole is None:
            await ctx.send("Invalid Arguments! Usage: !reactionrole <channel id> <message id> <emoji> <role>")
            return

        validchannel = False
        for channel in ctx.guild.channels:
            if channel.id == int(channelid):
                _channel = channel
                validchannel = True
        if not validchannel:
            await ctx.send("Invalid Channel! Usage: !reactionrole <channel id> <message id> <emoji> <role>")
            return

        validmessage = False
        for message in await channel.history(limit=500).flatten():
            if message.id == int(messageid):
                _message = message
                validmessage = True
        if not validmessage:
            await ctx.send("Invalid Message! Usage: !reactionrole <channel id> <message id> <emoji> <role>")
            return

        await _message.add_reaction(emoji=emoji)

        sendrole = giverole.replace("<@&", "").replace(">", "")
        emojihash = hashlib.md5(emoji.encode()).digest()

        with open(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'config', 'reactionroles.json')),"r") as f:
                file = json.load(f)

        if messageid in file.keys():
            file[messageid][f"{emojihash}"] = sendrole
        else:
            file[messageid] = {
                f"{emojihash}": sendrole
            }

        data = file

        with open(os.path.realpath(
                os.path.join(os.path.dirname(__file__), '..', 'config', 'reactionroles.json'))) as reactions_in:
            reacts = json.load(reactions_in)
            reacts.update(data)

        with open(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'config', 'reactionroles.json')),
                  "w") as f:
            json.dump(reacts, f, sort_keys=True, indent=2)








    # Listener for Reactions
    async def process_reaction(self, payload: RawReactionActionEvent, r_type=None) -> None:

        with open(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'config', 'reactionroles.json')),
                  "r") as f:
            file = json.load(f)

        emojihash = hashlib.md5(payload.emoji.name.encode()).digest()

        for key1 in file.keys():
            if payload.message_id == int(key1):
                for key2 in file[key1]:
                    if str(key2) == str(emojihash):
                        guild = self.bot.get_guild(payload.guild_id)
                        user = await guild.fetch_member(payload.user_id)
                        role = guild.get_role(int(file[key1][key2]))
                        if r_type == "add":
                            try:
                                await user.add_roles(role)
                            except discord.Forbidden:
                                print("I do not have permission to add roles!")
                        elif r_type == "remove":
                            try:
                                await user.remove_roles(role)
                            except discord.Forbidden:
                                print("I do not have permission to remove roles!")
                        break

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: RawReactionActionEvent):
        await self.process_reaction(payload, "add")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: RawReactionActionEvent):
        await self.process_reaction(payload, "remove")


async def setup(bot):
    await bot.add_cog(ReactionRoleCommand(bot))
