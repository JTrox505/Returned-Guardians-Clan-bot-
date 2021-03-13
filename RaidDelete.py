from discord.ext import commands
import os
class CommandEvents(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  @commands.Cog.listener()
  async def on_message(self, message):
    message.content = message.content.lower()
    def type_of_raid(raid_type):
      global Raid_type
      #Raid_type = "gos"
      if File_name[2] == "dsc":
        Raid_type = "dsc"
      if File_name[2] == "lw":
        Raid_type = "lw"
      if File_name[2] == "gos":
        Raid_type = "gos"
    if message.content.startswith ("delete raid"):
      File_name = message.content.split()
      type_of_raid(File_name[2])
      try:
        os.remove(f"{Raid_type}")
        os.remove(f"{Raid_type} info")
      except FileNotFoundError:
        await message.channel.send(f"There is no {Raid_type} raid that exists to delete at the moment")
      await message.channel.send("The raid has been deleted")



def setup(bot):
  bot.add_cog(CommandEvents(bot))
