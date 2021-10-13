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
    for i in istighfar:
        if message.content.startswith(i):
            await message.channel.send('Astagfirullah Hanip')
    if message.content.startswith('sabar'):
            await message.channel.send('Astagfirullah sabar')
    
    
client.run(hohoho)