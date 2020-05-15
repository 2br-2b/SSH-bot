import token_manager
import dmlistener
from discord.ext import commands
import discord

#create the bot
bot = commands.Bot(">>>")

#add the cog to listen for commands
dml = dmlistener.dmlistener(bot)
bot.add_cog(dml)

@bot.event
async def on_ready():
    print("Started!")
    #set the bot's status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=" for `>>>`"))

#run the bot
bot.run(token_manager.TOKEN)
