import discord
from discord.ext import commands
import asyncio

class UserManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="rolesetup", description="Set your cohort and location roles", guild_ids=id)
    async def role_setup(self, ctx, member: discord.Member):
        cohort_dropdown = discord.ui.Select(
            placeholder="Select your cohort...",
            options=[
                discord.SelectOption(label="Cohort 1", value="cohort_1"),
                discord.SelectOption(label="Cohort 2", value="cohort_2"),
            ],
            custom_id="cohort_dropdown"
        )

        view = discord.ui.View()
        view.add_item(cohort_dropdown)

        message = await ctx.send("Please select your cohort:", view=view)

        def check(interaction):
            return interaction.user == ctx.author and interaction.message == message

        try:
            interaction = await self.bot.wait_for("select_option", check=check, timeout=60)
            await interaction.response.defer()  # Acknowledge the interaction

            cohort = interaction.values[0]

            role_id = None
            if cohort == "cohort_1":
                role_id = 1258531898427314237
            elif cohort == "cohort_2":
                role_id = 1258531898427314238
            else:
                await ctx.respond("Invalid cohort")
                return

            guild = ctx.guild
            role = discord.utils.get(guild.roles, id=role_id)
            if role is not None:
                await member.add_roles(role)
                await ctx.respond("Role assigned successfully.")
            else:
                await ctx.respond("Role not found.")

        except asyncio.TimeoutError:
            await ctx.respond("Selection timed out.")

def setup(bot):
    bot.add_cog(UserManagement(bot))