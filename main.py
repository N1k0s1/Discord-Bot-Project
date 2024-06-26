import discord
import json
from discord.ext import commands
from discord import app_commands
import logging

TOKEN = '' 
intents = discord.Intents.default()
intents.members = True 
intents.message_content = True  
intents.presences = True 

bot = commands.Bot(command_prefix='/', case_insensitive=True, intents=intents)


tree = bot._connection._command_tree 

# Load cogs
initial_extensions = ['cogs.AutomatedMessaging', 'cogs.ChannelManagement', 'cogs.CoachingSessionCheckIn', 'cogs.CohortManagement', 'cogs.FeedbackCollection', 'cogs.LearnerNudges', 'cogs.SuggestionCollection', 'cogs.SupportTicket', 'cogs.UserManagement', 'cogs.WeeklyCheckIn', 'cogs.Greetings']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.command(name='sync', description='Owner only')
async def sync(interaction: discord.Interaction):
        print('Command tree synced.')
        await tree.sync(guild=discord.Object(id=1255437522629169285))
        print('Command tree synced.')

@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1255437522629169285))
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    await bot.change_presence(activity=discord.Activity(name='Working on REA', type=0, url='https://rea.coach'))
    print(f'Successfully logged in and booted...!')



bot.run(TOKEN) 