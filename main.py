import discord

client = discord.Client()

@client.event
async def on_ready():
    print("we have loggin as {0.user}'.format(client)")

@client.event()
async def on_message(message):
    