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
                discord.SelectOption(label="Cohort 6", value="Cohort 6"),
                discord.SelectOption(label="Cohort 7", value="Cohort 7"),
                discord.SelectOption(label="Cohort 8", value="Cohort 8")
            ]

            select = discord.ui.Select(placeholder="Choose your cohort", options=options, custom_id="select_cohort")

            view = discord.ui.View()
            view.add_item(select)

            message = await ctx.send(content="Please select your cohort:", view=view)

            def interaction_check(interaction):
                return interaction.user == member and interaction.message.id == message.id

            interaction = await self.bot.wait_for("interaction", check=interaction_check, timeout=120)

            cohort = interaction.data['values'][0]

            role = discord.utils.get(member.guild.roles, name=cohort)
            if role:
                await member.add_roles(role)
                await interaction.response.send_message(f"You have been assigned the {cohort} role.", ephemeral=True)
            else:
                await interaction.response.send_message("Invalid Cohort. Please try again.", ephemeral=True)

        except asyncio.TimeoutError:
            await ctx.send("Sorry, you took too long to respond. Please try again later.", ephemeral=True)
def setup(bot):
    bot.add_cog(UserManagement(bot))