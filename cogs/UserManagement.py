import discord
from discord.ext import commands
import asyncio

class UserManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="rolesetup", description="Set up roles for new members", guild_ids=[1255437522629169285])
    async def role_setup(self, ctx: discord.ApplicationContext, member: discord.Member):
        await ctx.respond(f"Welcome to the server, {member.mention}! Please tell us your City, Program, and Cohort.", ephemeral=True)

        def check(message):
            return message.author == member and message.guild is None

        try:
            options = [
                discord.SelectOption(label="Cohort 1", value="Cohort 1"),
                discord.SelectOption(label="Cohort 2", value="Cohort 2"),
                discord.SelectOption(label="Cohort 3", value="Cohort 3"),
                discord.SelectOption(label="Cohort 4", value="Cohort 4"),
                discord.SelectOption(label="Cohort 5", value="Cohort 5"),
                discord.SelectOption(label="Cohort 6", value="Cohort 6"),
                discord.SelectOption(label="Cohort 7", value="Cohort 7"),
                discord.SelectOption(label="Cohort 8", value="Cohort 8")
            ]

            locations = [
                discord.SelectOption(label="Location 1", value="Location 1"),
                discord.SelectOption(label="Location 2", value="Location 2"),
                discord.SelectOption(label="Location 3", value="Location 3"),
                discord.SelectOption(label="Location 4", value="Location 4"),
                discord.SelectOption(label="Location 5", value="Location 5"),
                discord.SelectOption(label="Location 6", value="Location 6"),
                discord.SelectOption(label="Location 7", value="Location 7"),
                discord.SelectOption(label="Location 8", value="Location 8")
            ]
            select_cohort = discord.ui.Select(placeholder="Choose your cohort", options=options, custom_id="select_cohort")
            select_location = discord.ui.Select(placeholder="Choose your location", options=locations, custom_id="select_location")

            view = discord.ui.View()
            view.add_item(select_cohort)
            view.add_item(select_location)

            message = await ctx.send(content="Please select your cohort and location:", view=view)

            def interaction_check(interaction):
                return interaction.user == member and interaction.message.id == message.id

            interaction = await self.bot.wait_for("interaction", check=interaction_check, timeout=120)

            cohort = interaction.data['values'][0]
            location = interaction.data['values'][1]

            cohort_role = discord.utils.get(member.guild.roles, name=cohort)
            location_role = discord.utils.get(member.guild.roles, name=location)

            if cohort_role and location_role:
                await member.add_roles(cohort_role, location_role)
                await interaction.response.send_message(f"You have been assigned the {cohort} cohort role and the {location} location role.", ephemeral=True)
            else:
                await interaction.response.send_message("Invalid cohort or location. Please try again.", ephemeral=True)

        except asyncio.TimeoutError:
            await ctx.send("Sorry, you took too long to respond. Please try again later.", ephemeral=True)

def setup(bot):
    bot.add_cog(UserManagement(bot))
