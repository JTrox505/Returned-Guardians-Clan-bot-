from discord.ext import commands

class CommandEvents(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  @commands.Cog.listener()
  async def on_message(self, message):
    message.content = message.content.lower()
    #This is the removal function, which lets users leave the raid party if something comes up. 
    if message.content.startswith("out"):
      File_name = message.content.split()
      f = open(File_name[1])
      contents = f.read()
      Raid_list = contents
      f.close()
      Raid_list = (Raid_list.split())
      lowercase_name = message.author.name.lower()
      First_available_slot = Raid_list.index(lowercase_name)
      Raid_list.remove(lowercase_name)
      Raid_list.insert(First_available_slot, "empty")
      space = " "
      Raid_party = Raid_list[0]+space+Raid_list[1]+space+Raid_list[2]+space+Raid_list[3]+space+Raid_list[4]+space+Raid_list[5]
      print(Raid_party)
      with open(f"{File_name[1]}", "w+") as Save:
        Save.write(Raid_party)
      spots_available = Raid_list.count("empty")
      #This organizes the raid list so that the empties are alaways at the end
      Rearrange_count = Raid_list.count("empty")
      for i in range(Rearrange_count):
        Raid_list.insert(-1, "empty")
        Raid_list.remove("empty")
      await message.channel.send(f"{lowercase_name} is leaving the raid!\nPlayers-\n{Raid_list[0]}\n{Raid_list[1]}\n{Raid_list[2]}\n{Raid_list[3]}\n{Raid_list[4]}\n{Raid_list[5]}\nTotal spots available:{spots_available}")



      #This function lets users remove players to the raid party that are not themselves, so that the person leaving doesn't always have to do it. 
    if message.content.startswith("remove player"):
      File_name = message.content.split()
      f = open(File_name[2])
      contents = f.read()
      Raid_list = contents
      f.close()
      Raid_list = (Raid_list.split())
      Custom_name = File_name[3]
      Custom_name = Custom_name.lower()
      print(Raid_list)
      print(Custom_name)
      First_available_slot = Raid_list.index(Custom_name)
      Raid_list.remove(Custom_name)
      Raid_list.insert(First_available_slot, "empty")
      space = " "
      Raid_party = Raid_list[0]+space+Raid_list[1]+space+Raid_list[2]+space+Raid_list[3]+space+Raid_list[4]+space+Raid_list[5]
      print(Raid_party)
      with open(f"{File_name[2]}", "w+") as Save:
        Save.write(Raid_party)
      spots_available = Raid_list.count("empty")
      #This organizes the raid list so that the empties are alaways at the end
      Rearrange_count = Raid_list.count("empty")
      for i in range(Rearrange_count):
        Raid_list.insert(-1, "empty")
        Raid_list.remove("empty")
      await message.channel.send(f"{Custom_name} is leaving the raid!\nPlayers-\n{Raid_list[0]}\n{Raid_list[1]}\n{Raid_list[2]}\n{Raid_list[3]}\n{Raid_list[4]}\n{Raid_list[5]}\nTotal spots available:{spots_available}")


def setup(bot):
  bot.add_cog(CommandEvents(bot))
