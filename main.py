import json
import os
import discord
import dotenv
import yaml
from discord.ext import commands
from dotenv import load_dotenv, get_key

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

load_dotenv()

bot = commands.Bot(command_prefix='!', intents=intents)


# Boot
@bot.event
async def on_ready():
    print(f'{bot.user.name} is now online.')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over the server..."))

    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'commands.{filename[:-3]}')
            print(f"Command '{filename[:-3]}' has loaded.")

    for filename in os.listdir('./listeners'):
        if filename.endswith('.py'):
            await bot.load_extension(f'listeners.{filename[:-3]}')
            print(f"Listener '{filename[:-3]}' has loaded.")


bot.remove_command('help')


# Error Catching
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.send("Command now found!")

bot.run(os.getenv("BOT_TOKEN"))
