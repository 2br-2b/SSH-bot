import os
from discord.ext import tasks, commands
import discord
import token_manager

class dmlistener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.prefix = '>>'

    @commands.is_owner()
    @commands.Cog.listener()
    async def on_message(self, message):
        if(message.author.id == token_manager.ACCOUNT_ID and message.content[0:len(self.prefix)] == self.prefix):
            await message.channel.send(os.system(message.content[len(self.prefix):len(message.content)].strip()))
            print('true')
