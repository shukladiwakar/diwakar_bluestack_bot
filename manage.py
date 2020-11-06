#!/usr/bin/env python
import os
import sys
import discord
from dotenv import load_dotenv
from searchHandler import query_router

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_message(message):
    print("Application has started")
    if message.author == client.user:
        return

    response = query_router(message)
    if type(response) is str:
        await message.channel.send(response)
    else:
        for url in response:
            await message.channel.send(url)



if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

    from django.core.management import execute_from_command_line
    client.run(TOKEN)
    execute_from_command_line(sys.argv)
