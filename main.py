id = [1255437522629169285]
import discord
bot = discord.Bot()
from discord.ext import commands

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    bot.load_extension("cogs.UserManagement")
    bot.load_extension("cogs.SuggestionCollection")
    bot.load_extension("cogs.ChannelManagement")
    print(f"Loaded {bot.load_extension} cogs")
    await bot.sync_commands()
    print(f"Succesfully synced commands")



@bot.slash_command(name="roletest", description="Set your cohort and location roles", guild_ids=id)
async def rolesetup(self, ctx, member: discord.Member):
    member.add_roles("Cohort 1")
    await ctx.respond("Role found")

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



bot.run(