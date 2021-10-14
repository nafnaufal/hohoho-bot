import os
import discord
import random
from server_live import keep_alive

client = discord.Client()
hohoho = os.environ['token']

istighfar = ['Astagfirullah', 'astagfirullah', 'astaghfirullah', 'Astaghfirullah', 'istighfar', 'Istighfar']

stop = True

@client.event
async def on_ready():
    print("{0.user} online".format(client))

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    if any(word in message.content for word in istighfar):
        await message.channel.send('Astagfirullah Hanip')

    if 'sabar' in message.content:
        await message.channel.send('Astagfirullah sabar')
    if 'test' in message.content:
        await message.channel.send('Kangen beb rifqi <3 <3 <3 luv luv')
    if message.content.startswith("_welcome"):
        halo = message.content.split("_welcome", 1)[1]
        await message.channel.send(f'Halo{halo} welcome o yeah welcome back :metal:')

    if message.content.startswith("_lc"):
        tipe, name1, name2 = message.content.split(",", 2)
        if "rifqi" in name1 and "rose" in name2:
            await message.channel.send(f'Love Calculator {name1} :heart: {name2} = 100%')
        elif "aufal" in name1 and "IU" in name2:
            await message.channel.send(f'Love Calculator {name1} :heart: {name2} = 999999999999999%')
        else:
            persen = random.randint(0, 101)
            await message.channel.send(f'Love Calculator {name1} :heart: {name2} = {persen}%')

keep_alive()
client.run(hohoho)