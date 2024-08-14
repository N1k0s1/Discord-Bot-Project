import discord
from discord.ext import commands
import asyncio

class UserManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="rolesetup", description="Set your cohort and location roles", guild_ids=[1255437522629169285])
    async def rolesetup(self, ctx, member: discord.Member):
        cohorts = ["Cohort 1", "Cohort 2", "Cohort 3"]
        locations = ["Location X", "Location Y", "Location Z"]

        cohort_dropdown = discord.ui.Select(
            placeholder="Select your cohort...",
            options=[
                discord.SelectOption(label="Cohort 1", value="Cohort 1"),
                discord.SelectOption(label="Cohort 2", value="Cohort 2"),
            ],
            custom_id="cohort_dropdown"
        )

        location_dropdown = discord.ui.Select(
            placeholder="Select your location...",
            options=[
                discord.SelectOption(label="Location 1", value="location_1"),
                discord.SelectOption(label="Location 2", value="location_2"),
            ],
            custom_id="location_dropdown"
        )

        view = discord.ui.View()
        view.add_item(cohort_dropdown)
        view.add_item(location_dropdown)

        message = await ctx.respond("Please select your cohort and location:", view=view)

        try:
            interaction = await self.bot.wait_for(
                "select_option",
                check=lambda i: i.component.custom_id in [cohort_dropdown.custom_id, location_dropdown.custom_id] and i.user.id == member.id,
                timeout=60
            )
        except asyncio.TimeoutError:
            await message.edit(content="Selection timed out.")
            return

        cohort = interaction.component[0].label
        location = interaction.component[1].label

        role_id = None
        if cohort == "Cohort 1":
            role_id = 1258531898427314237
        elif cohort == "Cohort 2":
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

        await interaction.respond(content=f"Roles assigned successfully to {member.mention}.")
def setup(bot):
    bot.add_cog(UserManagement(bot))
