import discord
from discord.ext import commands

class UserLogging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        @commands.Cog.listener()
        async def on_member_join(self, member):
            channel = self.bot.get_channel(1270169494538682419)
            await channel.send(f"{member} has joined the server.")

        @commands.Cog.listener()
        async def on_member_remove(self, member):
            channel = self.bot.get_channel(1270169494538682419)
            await channel.send(f"{member} has left the server.")

        @commands.Cog.listener()
        async def on_message(self, message):
            channel = self.bot.get_channel(1270169494538682419)
            await channel.send(f"{message.author} sent a message: {message.content}")

def setup(bot):
    bot.add_cog(UserLogging(bot))