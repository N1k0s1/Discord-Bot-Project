import discord
from discord.ext import commands
import asyncio

id = [1255437522629169285]

class UserManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="rolesetup", description="Set your cohort and location roles", guild_ids=id)
    async def roletest(self, ctx, member: discord.Member, cohort: str):
        role_id = None
        if cohort == "cohort 1":
            role_id = 1258531898427314237
        elif cohort == "cohort 2":
            role_id = 1258531898427314238
        else:
            await ctx.respond("Invalid cohort")
            return

        guild = ctx.guild
        role = discord.utils.get(guild.roles, id=role_id)
        if role is not None:
            await member.add_roles(role)
            await ctx.respond("Role found")
        else:
            await ctx.respond("Role not found")

def setup(bot):
    bot.add_cog(UserManagement(bot))
