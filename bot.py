import discord
import re
from PIL import Image
from dotenv import dotenv_values

env_vars = dotenv_values()
TOKEN = env_vars['TOKEN']

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)


def run_bot():
    @bot.event
    async def on_message(msg):
        if msg.author == bot.user:
            return

        elif msg.attachments:
            for attachment in msg.attachments:
                # img_bytes = await attachement.read()
                # with open("image.jg", "wb") as f:
                #     f.write(img_bytes)
                # image = Image.open("image.jpg").convert("L")
                # image.save("gray.jpg")
                # await msg.channel.send(file=discord.File('gray.jpg', filename='gray_image.png'))
                print(attachment.content_type)
                if attachment.content_type.startswith('image/'):
                    filename = re.search(r'[^/]+$', attachment.url).group()
                    img_bytes = await attachment.read()
                    new_filename = f"{filename + '_gray.jpeg'}"
                    with open(new_filename, "wb") as f:
                        f.write(img_bytes)
                    image = Image.open(new_filename).convert("L")
                    image.save(new_filename)
                    await msg.channel.send(file=discord.File(new_filename, filename='gray_image.png'))
                
                
    bot.run(TOKEN)


run_bot()
