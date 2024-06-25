import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Load cogs
initial_extensions = ['usermanagement.UserManagement']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run('bottoken')