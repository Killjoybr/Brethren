import discord
import asyncio
import os
import dotenv
import wavelink

from discord.ext import commands

bot = discord.Bot(debug_guilds=['847998007781359636'])

async def connect_nodes():
  """Connect to our Lavalink nodes."""
  await bot.wait_until_ready() # wait until the bot is ready

  await wavelink.NodePool.create_node(
    bot=bot,
    host='127.0.0.1',
    port=2333,
    password='youshallnotpass'
  ) # create a node
@bot.slash_command(name="play")
async def play(ctx, search: str):
  vc = ctx.voice_client # define our voice client

  if not vc: # check if the bot is not in a voice channel
    vc = await ctx.author.voice.channel.connect(cls=wavelink.Player) # connect to the voice channel

  if ctx.author.voice.channel.id != vc.channel.id: # check if the bot is not in the voice channel
    return await ctx.respond("You must be in the same voice channel as the bot.") # return an error message

  song = await wavelink.YouTubeTrack.search(query=search, return_first=True) # search for the song

  if not song: # check if the song is not found
    return await ctx.respond("No song found.") # return an error message

  await vc.play(song) # play the song
  await ctx.respond(f"Now playing: `{vc.source.title}`") # return a message

@bot.event
async def on_ready():
  await connect_nodes() # connect to the server

@bot.event
async def on_wavelink_node_ready(node: wavelink.Node):
  print(f"{node.identifier} is ready.") # print a message

dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))
#Without this our brethren doesn't get to live :(

bot.run(token)