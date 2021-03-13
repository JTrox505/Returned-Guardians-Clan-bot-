from discord.ext import commands

class CommandEvents(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  @commands.Cog.listener()
  async def on_message(self, message):
    message.content = message.content.lower()
    #This is the join function, which lets users join an already existing raid. 
    if message.content.startswith("in"):
      File_name = message.content.split()
      f = open(File_name[1])
      contents = f.read()
      Raid_list = contents
      f.close()
      Raid_list = (Raid_list.split())
      First_available_slot = Raid_list.index("empty")
      lowercase_name = message.author.name.lower()
      Raid_list.insert(First_available_slot, lowercase_name)
      First_available_slot+=1
      Raid_list.remove("empty")
      space = " "
      Raid_party = Raid_list[0]+space+Raid_list[1]+space+Raid_list[2]+space+Raid_list[3]+space+Raid_list[4]+space+Raid_list[5]
      print(Raid_party)
      with open(f"{File_name[1]}", "w+") as Save:
        Save.write(Raid_party)
      spots_available = Raid_list.count("empty")
      await message.channel.send(f"{lowercase_name} is joining the raid!\nPlayers-\n{Raid_list[0]}\n{Raid_list[1]}\n{Raid_list[2]}\n{Raid_list[3]}\n{Raid_list[4]}\n{Raid_list[5]}\nTotal spots available:{spots_available}")

    #This function lets users add players to the raid party that are not themselves, so that the person joining doesn't always have to do it. 
    if message.content.startswith("add player"):
      File_name = message.content.split()
      f = open(File_name[2])
      contents = f.read()
      Raid_list = contents
      f.close()
      Raid_list = (Raid_list.split())
      First_available_slot = Raid_list.index("empty")
      Custom_name = File_name[3]
      Custom_name = Custom_name.lower()
      Raid_list.insert(First_available_slot, Custom_name)
      First_available_slot+=1
      Raid_list.remove("empty")
      space = " "
      Raid_party = Raid_list[0]+space+Raid_list[1]+space+Raid_list[2]+space+Raid_list[3]+space+Raid_list[4]+space+Raid_list[5]
      print(Raid_party)
      with open(f"{File_name[2]}", "w+") as Save:
        Save.write(Raid_party)
      spots_available = Raid_list.count("empty")
      await message.channel.send(f"{Custom_name} is joining the raid!\nPlayers-\n{Raid_list[0]}\n{Raid_list[1]}\n{Raid_list[2]}\n{Raid_list[3]}\n{Raid_list[4]}\n{Raid_list[5]}\nTotal spots available:{spots_available}")

def setup(bot):
  bot.add_cog(CommandEvents(bot))
