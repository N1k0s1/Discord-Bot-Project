from discord.ext import commands
import discord

class ChannelManagement(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="createchannel", description="Create a new channel with specified users having access", guild_ids=[1255437522629169285])
    async def createchannel(self, ctx, channelname: str, *users: discord.Member):
        guild = ctx.guild
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True)
        }
        for user in users:
            overwrites[user] = discord.PermissionOverwrite(read_messages=True)
        await guild.create_text_channel(channelname, overwrites=overwrites)
        await ctx.respond("You have created a new channel!")

def setup(bot):
    bot.add_cog(ChannelManagement(bot))