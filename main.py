id = [1255437522629169285]
import discord
bot = discord.Bot()
from discord.ext import commands
import asyncio

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    extensions = ["cogs.ChannelManagement", "cogs.SupportTicket", "cogs.SuggestionCollection"]
    for extension in extensions:
        bot.load_extension(extension)
    print(f"Loaded {len(extensions)} cogs")
    await bot.sync_commands()
    print(f"Succesfully synced commands")

@bot.slash_command(name="loadcog", description= "Loads a cog of the users choosing", guild_id = id)
async def cogs(ctx, cogs):
    if cogs in cogs:
        bot.load_extension(f'cogs.{cogs}')
        await ctx.respond(f"Successfully loaded {cogs}")
    else:
        await ctx.respond("Cog not found")
#    elif:
        
@bot.slash_command(name="unloadcog", description= "Unloads a cog of the users choosing", guild_id = id)
async def cogs(ctx, cogs):
    if cogs in cogs:
        bot.unload_extension(f'cogs.{cogs}')
        await ctx.respond(f"Successfully unloaded {cogs}")
    else:
        await ctx.respond("Cog not found")
#    elif:

@bot.slash_command(guild_id = id)
async def ping(ctx):
    await ctx.respond(f"Pong! ({bot.latency*1000}ms)")

@bot.slash_command(guild_id = id)
async def sync(ctx): 
    await bot.sync_commands()
    await ctx.respond(f"Succesfully synced commands")



async def role_setup(ctx, member: discord.Member):
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

    message = await ctx.respond("Please select your cohort:", view=view)

    def check(interaction):
        return interaction.user == ctx.author and interaction.message == message

    try:
        interaction = await bot.wait_for("select_option", check=check, timeout=60)
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

class Cohorts(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='Cohort 1', custom_id='cohort_1', style=discord.ButtonStyle.green)
    async def on_button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        role_id = 1258531898427314237
        role = discord.utils.get(interaction.guild.roles, id=role_id)
        if role is not None:
            await member.add_roles(role)
        else:
            embed = discord.Embed(title="Cohort 1", description="Cohort 1")
            await interaction.response.send_message(embed=embed)

