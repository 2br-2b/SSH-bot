import token_manager
import dmlistener
from discord.ext import commands
import discord

bot = commands.Bot(">>>")

dml = dmlistener.dmlistener(bot)
bot.add_cog(dml)

@bot.event
async def on_ready():
    print("Started!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=" for `>>>`"))

bot.run(token_manager.TOKEN)
