import discord
import images
from PIL import Image
import io
from dotenv import dotenv_values

env_vars = dotenv_values()
TOKEN = env_vars['TOKEN']

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)



@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return

    elif msg.attachments:
        for attachement in msg.attachments:
            print("1")
            img_bytes = await attachement.read()
            with open("image.jpg", "wb") as f:
                f.write(img_bytes)
            image = Image.open("image.jpg").convert("L")
            image.save("gray.jpg")
            await msg.channel.send(file=discord.File('gray.jpg', filename='gray_image.png'))
            
            
bot.run(TOKEN)
