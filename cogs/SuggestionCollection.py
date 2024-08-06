import discord
from discord.ext import commands
id = [1255437522629169285]

class SuggestionCollection(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.slash_command(name="suggestion", description="Submit a suggestion to the server", guild_ids=[1255437522629169285])
  async def submit_suggestion(self, ctx, *, suggestion):
    suggestion_channel = self.bot.get_channel(1267667592060076084)
    if suggestion_channel:
      username = ctx.author.name
      await suggestion_channel.send(f"New suggestion from {username}: {suggestion}")
      await ctx.respond("Thank you for your suggestion!", ephemeral=True)
    else:
      await ctx.respond("Suggestion channel not found.")

def setup(bot):
  bot.add_cog(SuggestionCollection(bot))
