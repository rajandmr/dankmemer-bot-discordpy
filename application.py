import discord
import os
client = discord.Client()
token = os.environ.get('discord_bot_token')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello, I AM A PY-BOT!')

client.run(token)
