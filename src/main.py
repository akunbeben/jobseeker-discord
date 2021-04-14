import kalibrr
import karir
import discord
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
        await message.channel.send("Here is the list of jobs for you <@{0.author.id}>, Source: https://www.kalibrr.id/".format(message))
        keyword = msg.replace('!kalibr ', '')
        result = kalibrr.getKalibrr(keyword)
        for index in result:
            await message.channel.send(index)

    if message.content.startswith('!karircom'):
        await message.channel.send("Here is the list of jobs for you <@{0.author.id}>, Source: https://www.karir.com/".format(message))
        keyword = msg.replace('!karircom ', '')
        result = karir.getKarir(keyword)

    for index in result:
        await message.channel.send(index)

client.run(config('TOKEN'))
