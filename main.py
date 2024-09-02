id = [1255437522629169285]
import discord
bot = discord.Bot()
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

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




class Cohorts(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='Cohort 1', custom_id='cohort_1', style=discord.ButtonStyle.green)
    async def on_button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        role_id = 1258531898427314237
        role = discord.utils.get(interaction.guild.roles, id=role_id)
        if role is not None:
            member = interaction.user
            await member.add_roles(role)
        else:
            embed = discord.Embed(title="Cohort 1", description="Cohort 1")
            await interaction.response.send_message(embed=embed)

    @discord.ui.button(label='Cohort 2', custom_id='cohort_2', style=discord.ButtonStyle.green)
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        role_id = 1258532294969397350
        role = discord.utils.get(interaction.guild.roles, id=role_id)
        if role is not None:
            member = interaction.user
            await member.add_roles(role)
        else:
            embed = discord.Embed(title="Cohort 2", description="Cohort 2")
            await interaction.response.send_message(embed=embed)

    @discord.ui.button(label='Cohort 3', custom_id='cohort_3', style=discord.ButtonStyle.green)
    async def on_button3(self, button: discord.ui.Button, interaction: discord.Interaction):
        role_id = 1258531898427314237
        role = discord.utils.get(interaction.guild.roles, id=role_id)
        if role is not None:
            member = interaction.user
            await member.add_roles(role)
        else:
            embed = discord.Embed(title="Cohort 3", description="Cohort 3")
            await interaction.response.send_message(embed=embed)

@bot.slash_command(name="cohortselection", description="Cohort Selection", guild_id = id)
async def sellers(ctx,):
        await ctx.respond('Cohorts: Choose an option.', view=Cohorts())


bot.run(TOKEN)
