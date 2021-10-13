import os
import discord

client = discord.Client()
hohoho = os.environ['token']

istighfar = ['Astagfirullah', 'astagfirullah', 'astaghfirullah', 'Astaghfirullah', 'istighfar', 'Istighfar']

@client.event
async def on_ready():
    print("we have loggin as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if any(word in message.content for word in istighfar):
            await message.channel.send('Astagfirullah Hanip')

    if 'sabar' in message.content:
            await message.channel.send('Astagfirullah sabar')

client.run(hohoho)