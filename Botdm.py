from discord.ext import commands
#client = discord.Client()
class CommandEvents(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  @commands.Cog.listener()
  async def on_message(self, message):
    message.content = message.content.lower()

    if message.content.startswith("new command"):
      import random
      Random_number = random.randint(1,1000)
      while True:
        try:
          f = open(f"{Random_number}")
          contents = f.read
          print(contents)
          f.close
          Random_number = random.randint(1,1000)


        except FileNotFoundError:
          from datetime import datetime
          now = datetime.now()
          dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
          dt_list = dt_string.split()
          Date_and_time = dt_list[0]
          dt_list = dt_list[1].split(":")
          Hour_original = dt_list[0]
          dt_list.remove(Hour_original)
          Hour_original = int(Hour_original)
          Hour = (Hour_original-6)
          Hour = str(Hour)
          dt_list.insert(0, Hour)
          dt_list = ":".join(dt_list)


          Date_and_time = [dt_list, Date_and_time]
          Date_and_time = " ".join(Date_and_time)
          message.content = message.content.split()
          message.content = message.content[2:]
          message.content = " ".join(message.content)
          with open(f"{Random_number}", "w+") as Save:
            Save.write(f"{Date_and_time} {message.author} {message.content}")
          break
      await message.author.send(f"You're command has been added! If you ever want to change or update your command, use the command !update command {Random_number} (The number is unique to that command)")



    if message.content.startswith("update command"):
      File_name = message.content.split()
      try:
        f = open(f"{File_name[2]}")
        contents = f.read()
        Command_message = contents.split()
        f.close 
        if Command_message[2] == message.author:
          Command_message = Command_message[3:]
          print(Command_message)
          Command_message = " ".join(Command_message)


          from datetime import datetime
          now = datetime.now()
          dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
          dt_list = dt_string.split()
          Date_and_time = dt_list[0]
          dt_list = dt_list[1].split(":")
          Hour_original = dt_list[0]
          dt_list.remove(Hour_original)
          Hour_original = int(Hour_original)
          Hour = (Hour_original-6)
          Hour = str(Hour)
          dt_list.insert(0, Hour)
          dt_list = ":".join(dt_list)
          Date_and_time = [dt_list, Date_and_time]
          Date_and_time = " ".join(Date_and_time)

          message.content = message.content.split()
          message.content = message.content[3:]
          message.content = " ".join(message.content)
          with open(f"Updated {File_name[2]}", "w+") as Save:
            Save.write(f"{Date_and_time} {message.author} {message.content}")
          await message.author.send(f"your old message was '{Command_message}', your new message is '{message.content}'")
        else:
          await message.author.send("You do not have ownership of this command")
      except FileNotFoundError:
        await message.author.send("That command key does not seem to be valid, please try again.")
def setup(bot):
  bot.add_cog(CommandEvents(bot))

# add a feature that lets users edit commands, this would look something like !change command (Token they were givent) (Change goes here) this would change the file name to UPDATED {File_name} so that I know something has changed. 

#Learn a lot more about discord.ext commands so that I can make my life easier.  
