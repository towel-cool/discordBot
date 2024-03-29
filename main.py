import os
import discord
from keepRunning import keepLive
from botFuncs import getLyrics
from botFuncs import getImage

#Creates variable for hiden value bot token
my_secret = os.environ['discordBotToken']
client = discord.Client()

#Runs when bot starts
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


#Runs when a message is recieved
@client.event
async def on_message(message):
    #Checks if message is sent by the bot (if it is do nothing)
    if message.author == client.user:
        return

    #/////////////
    #Bot commands
    #/////////////

    #Help Command
    if message.content.startswith(".help"):
        await message.channel.send("``` Commands: \n .lyrics 'Song Name' -> Provides the lyrics to a given song \n \
.image -> Sends a random image```")

    #Lyrics Printer Command
    if message.content.startswith(".lyrics"):
      try:
        songInfo = getLyrics(message.content[8:])
        if (len(songInfo) > 1):
            if (len(songInfo[1]) < 2000):
                await message.channel.send("Title: " + songInfo[0] + "\n" +
                                           "Artist: " + songInfo[2] + "\n" +
                                           "```" + songInfo[1] + "```")
            else:
                await message.channel.send(
                    "This song's lyrics exceeds 2000 characters")
        else:
            await message.channel.send(
                "Sorry, I couldn't find that song's lyrics")
      except:
        await message.channel.send("Error getting lyrics")

    #Random images command
    if message.content.startswith(".image"):
      try:
        image = getImage()
        await message.channel.send(image)
      except:
        await message.channel.send("Error getting image")


keepLive()
client.run(my_secret)
