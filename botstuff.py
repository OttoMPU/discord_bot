# -*- coding: UTF-8 -*-

import discord
from discord.ext import commands
import requests
from requests_html import HTMLSession
import json
import os
import gtts
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
session = HTMLSession()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="quote", help="inspirational")
async def inspirationquote(ctx):
    response = requests.get("https://api.quotable.io/random")
    json_data = json.loads(response.text)
    jsonlist = json_data
    quote = jsonlist["content"] + "\n -" + jsonlist["author"]
    await ctx.send(quote)
    

@bot.command(name="donation", help="gdq")
async def donationquote(ctx):
    response = session.get("https://taskinoz.com/gdq/api")
    donate = str(response.content)
    donate = donate.strip("b'")
    await ctx.send(donate)
    
"""
@bot.command(name="tts", help="text to speech")
async def ttsfunc(ttsmessage):
    ttsfile = "testing.mp3"
    tts = gTTS(ttsmessage, lang=fi)
    play(ttsfile, after=None)


@bot.command(name="join", help="leave")
async def joinvoice(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
"""

@bot.command(name="quality", help="nostalgic")
async def changequality(ctx):
    try:
        user_channel_id = ctx.message.author.voice.channel.id
        await ctx.send(user_channel_id)
    except:
        await ctx.send("No voice channel found")

    if (user_channel_id==None):
        return
    else:
        user_channel_id = ctx.message.author.voice.channel.id
                
        currchannel = ctx.message.guild.channels.resolve(user_channel_id)
        currchannel.setBitrate(8000)
        #await currchannel.edit(reason="xd", bitrate=8000) 
    
@bot.event
async def on_ready():
    status = " !help for commands"
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status))
    
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return


bot.run(TOKEN)