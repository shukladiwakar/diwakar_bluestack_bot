import os
import discord
from dotenv import load_dotenv
from searchHandler import query_router

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response = query_router(message)
    if type(response) is str:
        await message.channel.send(response)
    else:
        for url in response:
            await message.channel.send(url)


client.run(TOKEN)
