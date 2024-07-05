import discord
from discord.ext import commands

class SuggestionBox(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.slash_command(name="suggestion", description="Submit a suggestion to the server")
  async def submit_suggestion(self, ctx, *, suggestion):
    suggestion_channel = self.bot.get_channel(1255438842341621851)
    await suggestion_channel.send(f"New suggestion from: {suggestion}")
    await ctx.send("Thank you for your suggestion!")

def setup(bot):
  bot.add_cog(SuggestionBox(bot))
