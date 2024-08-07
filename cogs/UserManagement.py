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
                placeholder="Select a cohort",
                options=[discord.SelectOption(label=cohort) for cohort in cohorts]
            )
            location_dropdown = discord.ui.Select(
                placeholder="Select a location",
                options=[discord.SelectOption(label=location) for location in locations]
            )

            message = await ctx.send(
                f"Please select your cohort and location, {member.mention}",
                components=[cohort_dropdown, location_dropdown]
            )

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

            cohort_role = discord.utils.get(ctx.guild.roles, name=cohort)
            location_role = discord.utils.get(ctx.guild.roles, name=location)
            if cohort_role:
                await member.add_roles(cohort_role)
            if location_role:
                await member.add_roles(location_role)

            await message.edit(content=f"Roles assigned successfully to {member.mention}.")

def setup(bot):
    bot.add_cog(UserManagement(bot))
