import os
from discord.ext import tasks, commands
import discord
import token_manager

class dmlistener(commands.Cog):
    def __init__(self, bot):
        #initialize the bot
        self.bot = bot
        self.prefix = '>>'

    @commands.is_owner()
    @commands.Cog.listener()
    async def on_message(self, message):
        # If the sender is the correct user and the message starts with the prefix
        if(message.author.id == token_manager.ACCOUNT_ID and message.content[0:len(self.prefix)] == self.prefix):
            #send the result of the command after stripping off whitespace and removing the prefix
            await message.channel.send(os.system(message.content[len(self.prefix):len(message.content)].strip()))
            print('true')
            #TODO: right now, the output for the command prints in the terminal rather than being returned in the message
