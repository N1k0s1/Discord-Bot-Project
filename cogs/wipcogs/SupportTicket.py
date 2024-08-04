import discord
from discord.ext import commands

class SupportTicket(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  async def create_ticket(self, ctx, option_number: int):
    options = {
      1: {"name": "Option 1", "group": "group1"},
      2: {"name": "Option 2", "group": "group2"},
      3: {"name": "Option 3", "group": "group3"},
      4: {"name": "Option 4", "group": "group4"},
      5: {"name": "Option 5", "group": "group5"}
    }

    if option_number in options:
      selected_option = options[option_number]
      await ctx.send(f"You have selected {selected_option['name']}.")

      group = selected_option['group']
      await ctx.send(f"Pinging {group} for assistance.")

    else:
      await ctx.send("Invalid option number.")

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def close_ticket(self, ctx):
    await ctx.send("Ticket closed and deleted.")

def setup(bot):
  bot.add_cog(SupportTicket(bot))
