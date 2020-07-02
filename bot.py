import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = "INSERT TOKEN HERE"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hey {member.name}, Welcome to the Lucky Brand Team'
    )

# @client.event
# async def on_message(message):
#     if '!help' in message.content.lower():
#         await message.channel.send('Here are a lists of commands: !*help : displays a list of commands, !*report [description of bug]')

@client.event
async def on_message(message):
    id = random.randint(1,100000)
    desc = message.content.lower()
    desc2 = desc.replace("!report", "")
    if '!report' in message.content.lower():
        await message.channel.send("bug #"+ str(id) +" has been added to the list of bugs " + "The bug description is: "+desc2)
    else:
        if '!fix '+str(id) in message.content.lower():
            await message.channel.send("bug #"+str(id)+"has been fixed move on !")

client.run(TOKEN)