#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
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


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject4.settings')
    client.run(TOKEN)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
