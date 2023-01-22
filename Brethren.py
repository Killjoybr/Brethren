import discord
import asyncio
import os
import dotenv

from discord.ext import commands

bot = discord.Bot(debug_guilds=['847998007781359636'])

cogs_list = [
    'boasvindas'
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')


dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))
#This code above is just for the token

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


bot.run(token)