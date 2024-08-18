import discord
from discord.ext import commands
import asyncio

class UserManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="rolesetup", description="Set your cohort and location roles", guild_ids=id)
    async def roletest(ctx, member: discord.Member, cohort: str):
        role_id = None
        if cohort == "cohort 1":
            role_id = 1258531898427314237
        elif cohort == "cohort 2":
            role_id = 1258531898427314238
        else:
            await ctx.respond("Invalid cohort")
            return

        role = discord.utils.get(ctx.guild.roles, id=role_id)
        if role is not None:
            await member.add_roles(role)
            await ctx.respond("Role found")
        else:
            await ctx.respond("Role not found")

def setup(bot):
    bot.add_cog(UserManagement(bot))
