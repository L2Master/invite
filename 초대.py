import discord
imfort os


client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")

@client.event
async def on_message(message):
    if message.content.startswith("초대"):
        await message.channel.send("https://discord.gg/VDQMR8e")

access_token = os.environ["BOT_TOKEN"]
client.run("access_token")
