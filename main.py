import discord
from src import kalibrr
from src import karir
from decouple import config

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user} - BOT: ONLINE'.format(client))

@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
        return

    if message.content.startswith('!kalibr'):
        keyword = msg.replace('!kalibr ', '')
        result = kalibrr.getKalibrr(keyword)
        await message.channel.send("Here is the list of jobs for you <@{0.author.id}>, Source: https://www.kalibrr.id/".format(message))
        for index in result:
            embedMessage = discord.Embed(title="Result from https://www.kalibrr.id/", description="{0}".format(index), color=0x7F7F7F)
            await message.channel.send(embed=embedMessage)

    if message.content.startswith('!karircom'):
        keyword = msg.replace('!karircom ', '')
        result = karir.getKarir(keyword)
        await message.channel.send("Here is the list of jobs for you <@{0.author.id}>, Source: https://www.karir.com/".format(message))
        for index in result:
            embedMessage = discord.Embed(title="Result from https://www.karir.com/", description="{0}".format(index), color=0x7F7F7F)
            await message.channel.send(embed=embedMessage)

client.run(config('TOKEN'))