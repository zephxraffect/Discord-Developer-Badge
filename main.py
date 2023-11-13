import discord
from discord.ext import commands, tasks
from itertools import cycle

bottoken = input("You bot token: ")

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

print("Your bot is started!")
print("Now you can go and run the /start command!")
print("---------------------------------------------------------------------------")
print("Please wait 10-30 seconds for the slash command to sync to you discord bot!")
print("---------------------------------------------------------------------------")
print("Thanks for using our code!")

bot_status = cycle(["/start"])

@tasks.loop(seconds=12)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

@client.event
async def on_ready():
    print(f"{client.user}")
    await client.tree.sync()  
    change_status.start()

@client.tree.command(name="start", description="start the process for the developer badge")
async def start(interaction: discord.Interaction):

    message = f"Hi there! {interaction.user.mention},\n\nYou will be able to redeem your developer badge in 24 hours on the discord website. Please follow the link below to access the redemption page:\nhttps://discord.com/developers/active-developer \n\nHappy coding!"
 
    await interaction.response.send_message(message)


client.run(bottoken)
