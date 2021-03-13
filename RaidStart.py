from discord.ext import commands

class CommandEvents(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  @commands.Cog.listener()
  async def on_message(self, message):
    message.content = message.content.lower()
    

#This function allows users to pick any raid, and doing it this way will save some cyclomatic complexity (I hope). 
    def type_of_raid(raid_type):
      global Raid_type
      if File_name[2] == "dsc":
        Raid_type = "dsc"
      if File_name[2] == "lw":
        Raid_type = "lw"
      if File_name[2] == "gos":
        Raid_type = "gos"

    if message.content.startswith("new raid"):
      #this code rotates through all days so that if a day is present in the user's message the bot will find which day it is and then assign it to a variable to then be later used to put in a file
      Days= ["sun", "mon", "tues", "wed", "thurs", "fri", "sat"]
      Full_length_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
      Day =0
      while message.content != Days:
        try:
          if Days[Day] in message.content or Full_length_days in message.content:
            print(Days[Day])
            Correct_day = (Full_length_days[Day])
            break
          Day+=1
        except IndexError:
          Correct_day = "Not Set"
          break


      File_name = message.content.split()
      Date_item_chosen = 0
      for i in File_name:
        Date_item = (File_name[Date_item_chosen])   
        Date_item = str(Date_item)
        if "/" in Date_item:
          Date_location= (File_name.index(Date_item))
        Date_item_chosen += 1
      Date_location_contents = File_name[Date_location]
      print(Date_location_contents)

      import datetime
      Week_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
      Date_location_contents = Date_location_contents.split("/")
      Date = []
      Date_number = 0
      for i in Date_location_contents:
        Date_item = Date_location_contents[Date_number]
        Date_item = int(Date_item)
        Date.append(Date_item)
        Date_number+=1

      Week_num = datetime.date(Date[2],Date[0],Date[1]).weekday()
      Correct_day =(Week_days[Week_num])
















      type_of_raid(File_name[2])
      File_location = File_name.index(Raid_type)
      if Correct_day == "Not Set":
        Raid_info = File_name[3:]
      else:
        Raid_info = File_name[4:]
      Raid_info = " ".join(Raid_info)
      lowercase_name = message.author.name.lower()

      with open(f"{File_name[File_location]}", "w+") as Save:
        Save.write(f"{lowercase_name} empty empty empty empty empty")

      with open(f"{File_name[File_location]} info", "w+") as Save:
        Save.write(f"{Correct_day} {Raid_info}")

      f = open(File_name[File_location])
      contents = f.read()
      Raid_list = contents
      f.close()

      f = open(f"{File_name[File_location]} info")
      contents = f.read()
      Raid_description = contents
      f.close()

      Raid_list = (Raid_list.split())
      spots_available = Raid_list.count("empty")
      Raid_description = (Raid_description.split())
      if Raid_description[0] == "Not":
        Raid_day = "Not set"
        Raid_user_description = Raid_description[2:]
      else:
        Raid_day = Raid_description[0]
        Raid_user_description = Raid_description[1:]
      Raid_user_description = " ".join(Raid_user_description)

      await message.channel.send(f"{lowercase_name} is starting a new {Raid_type} raid!\nRaid day: {Raid_day}\nDescription: {Raid_user_description}\nPlayers-\n{Raid_list[0]}\n{Raid_list[1]}\n{Raid_list[2]}\n{Raid_list[3]}\n{Raid_list[4]}\n{Raid_list[5]}\nTotal spots available:{spots_available}")

def setup(bot):
  bot.add_cog(CommandEvents(bot))
