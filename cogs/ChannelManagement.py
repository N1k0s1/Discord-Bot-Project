import discord
from discord.ext import commands

class ChannelManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="createchannel", description="Create a new channel with specified users having access", guild_id=id)
    async def createchannel(self, ctx, channelname: str, users: discord.Member):
        guild = ctx.guild
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True)
        }
        overwrites[users] = discord.PermissionOverwrite(read_messages=True)
        await guild.create_text_channel(channelname, overwrites=overwrites)
        await ctx.respond("You have created a new channel!")
        
    @commands.slash_command(name="deletechannel", description="Delete a channel", guild_id=id)
    async def deletechannel(self, ctx, channel: discord.TextChannel):
        if ctx.author == channel.creator or ctx.author.guild_permissions.administrator:
            await channel.delete()
            await ctx.respond("Channel deleted successfully!")
        else:
            await ctx.respond("You do not have permission to delete this channel.")
def setup(bot):
    bot.add_cog(ChannelManagement(bot))