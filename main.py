id = [1255437522629169285]
import discord
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")



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

@bot.slash_command(name="createchannel", description="Create a new channel with specified users having access", guild_ids=[1255437522629169285])
async def createchannel(ctx, channelname: str, users: discord.Member):
    guild = ctx.guild
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True)
    }
    overwrites[users] = discord.PermissionOverwrite(read_messages=True)
    await guild.create_text_channel(channelname, overwrites=overwrites)
    await ctx.respond("You have created a new channel!")

bot.run()