import discord
from discord.ext import commands
id = [1255437522629169285]


class ChannelManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.slash_command(name="createchannel", description="Create a new channel with specified users having access")
async def createchannel(ctx, channelname: str, users: str):
    guild = ctx.guild
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True)
    }
    user_list = users.split()  # Assuming users are provided as space-separated user IDs
    for user_id in user_list:
        user = guild.get_member(int(user_id))
        if user:
            overwrites[user] = discord.PermissionOverwrite(read_messages=True)
    await guild.create_text_channel(channelname, overwrites=overwrites)
    await ctx.respond("You have created a new channel!")

@commands.slash_command(name="invite", description="Invite a user to the channel")
async def invite(ctx, user: discord.Member):
    channel = ctx.channel
    if ctx.author == channel.guild.owner or ctx.author.guild_permissions.administrator:
        await channel.set_permissions(user, read_messages=True)
        await ctx.respond(f"{user.mention} has been invited to the channel!")
    else:
        await ctx.respond("You do not have permission to invite users to this channel.")

@commands.slash_command(name="deletechannel", description="Delete a channel")
async def deletechannel(ctx, channel: discord.TextChannel):
    if ctx.author == channel.guild.owner or ctx.author.guild_permissions.administrator:
        await channel.delete()
        await ctx.respond("Channel deleted successfully!")
    else:
        await ctx.respond("You do not have permission to delete this channel.")


def setup(bot):
    bot.add_cog(ChannelManagement(bot))