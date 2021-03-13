import discord
import os
from discord.ext import commands
client = commands.Bot(command_prefix='-', help_command=None)
intents = discord.Intents.default()
intents.members = True
intents.presences = True

#this just lets the user know that the bot is ready
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

#the code below makes sure the bot doesn't reply to itself
@client.event
async def on_message(message):
  if message.author == client.user:
    return   


#The next thing to do is implement test number 28 into the RaidStart file so that the bot can recognize dates as well, instead of just days of the week.


#Desctiption can be any length at all so I need to find a way to isolate it.   
#use the .count method to see what raids the user picked. 


client.load_extension("cogs.RaidStart")
client.load_extension("cogs.RaidJoin")
client.load_extension("cogs.RaidLeave")
client.load_extension("cogs.RaidDelete")


client.run(os.getenv("TOKEN"))

# make a function that allows for multiple types of the same raid, but when someone uses a join or leave function the bot will pull up all 
#raids that share the same name and ask the user which one they want to join or leave. To do this I will have to implement an automatic deletion 
#of a raid so that users aren't bombarded with 16 different options every time they want to join a raid. I'm thinking thirty minutes after the original 
#start time should suffice. 
