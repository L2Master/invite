import discord


client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")

@client.event
async def on_message(message):
    if message.content.startswith("초대"):
        await message.channel.send("https://discord.gg/VDQMR8e")

client.run("Nzc0NDc0NjgxNTcwNjg5MDQ0.X6YTwQ.d-cbg9BRspqofs6RbqiKTMrXVeI")