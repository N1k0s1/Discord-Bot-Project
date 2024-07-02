import asyncio
import discord
from discord.ext import commands

class UserManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send("Welcome to the server! Please tell us your City, Program, and Cohort.")

        def check(message):
            return message.author == member and message.guild is None

        try:
            response = await self.bot.wait_for('message', check=check, timeout=120)
            data = response.content.split(",")

            if data[2].strip() == "Cohort 6":
                role = discord.utils.get(member.guild.roles, name="Cohort 6")
                await member.add_roles(role)
            elif data[2].strip() == "Cohort 7":
                role = discord.utils.get(member.guild.roles, name="Cohort 7")
                await member.add_roles(role)
            elif data[2].strip() == "Cohort 8":
                role = discord.utils.get(member.guild.roles, name="Cohort 8")
                await member.add_roles(role)
            else:
                await member.send("Invalid Cohort. Please try again.")

        except asyncio.TimeoutError:
            await member.send("Sorry, you took too long to respond. Please try again later.")

def setup(bot):
    bot.add_cog(UserManagement(bot))