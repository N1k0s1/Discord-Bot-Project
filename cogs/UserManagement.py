import discord
from discord.ext import commands
import asyncio

class UserManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @discord.slash_command(name="rolesetup", description="Set your cohort and location roles")
        async def roletest(ctx, member: discord.Member, cohort: str):
            options = ["cohort 1", "cohort 2"]

            dropdown_message = await ctx.send("Please select a cohort:", options=options)

            try:
                selected_option = await self.bot.wait_for(
                    "dropdown_select", check=lambda m: m.custom_id == dropdown_message.id and m.user.id == ctx.author.id, timeout=60
                )
            except asyncio.TimeoutError:
                await ctx.send("You took too long to select an option.")
                return

            role_id = None
            if selected_option == "cohort 1":
                role_id = 1258531898427314237
            elif selected_option == "cohort 2":
                role_id = 1258531898427314238
            else:
                await ctx.respond("Invalid cohort")
                return

            role = discord.utils.get(ctx.guild.roles, id=role_id)
            if role is not None:
                await member.add_roles(role)
                await ctx.send("Role found")
            else:
                await ctx.send("Role not found")

    def setup(bot):
        bot.add_cog(UserManagement(bot))
def setup(bot):
    bot.add_cog(UserManagement(bot))
