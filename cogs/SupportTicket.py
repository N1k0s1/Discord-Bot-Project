import discord
from discord.ext import commands

class SupportTicket(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.options = {
      1: {"name": "Wellness, Accountability & Attendance", "group": "group1"},
      2: {"name": "Technical Support", "group": "group2"},
      3: {"name": "Project Specific Support", "group": "group3"},
      4: {"name": "Specialisation", "group": "group4"}
    }

  async def create_ticket(self, ctx, option_number: int):
    if option_number in self.options:
      selected_option = self.options[option_number]
      await ctx.send(f"You have selected {selected_option['name']}.")

      group = selected_option['group']
      await ctx.send(f"Pinging {group} for assistance.")

    else:
      await ctx.send("Invalid option number.")

  @discord.slash_command(name="deleteticket", description="Delete  a support ticket (ADMIN ONLY)")
  @commands.has_permissions(administrator=True)
  async def close_ticket(self, ctx):
    await ctx.send("Ticket closed and deleted.")

  @discord.slash_command(name="ticketsetup", description="Ticket setup (ADMIN ONLY)")
  @commands.has_permissions(administrator=True)
  async def ticketsetup(self, ctx):
    await ctx.send("Ticket setup completed.")

def setup(bot):
  bot.add_cog(SupportTicket(bot))
