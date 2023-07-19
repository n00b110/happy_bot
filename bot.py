import discord
from discord.ext import commands
from PIL import Image
from dotenv import dotenv_values


env_vars = dotenv_values()
TOKEN = env_vars['TOKEN']

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

class SimpleView(discord.ui.View):

    foo: bool = None

    
    @discord.ui.button(label="Hello", style=discord.ButtonStyle.success)
    async def hello(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("World")







@bot.command(help='Run this command to get the server\'s ping')
async def ping(ctx):
    latency = round(bot.latency, 3)
    embed = discord.Embed(
        color=discord.Color.green(),
        title="Ping",
        description=f"Latency is {latency}s"
    )
    await ctx.send(embed=embed)


@bot.command(help='Run this command to get a list of all the commands for the server')
async def commands(ctx):
    embed = discord.Embed(title="Command List", color=discord.Color.blue())

    # Iterate through all the bot's commands
    for command in bot.commands:
        embed.add_field(name=command.name, value=command.help, inline=False)
    
    await ctx.send(embed=embed)


@bot.command()
async def edit(ctx):
    edit_embed = discord.Embed(title="Image Editor", color=discord.Color.green())
    attachments = ctx.message.attachments
    if len(attachments) > 1:
        await ctx.send("Only one image a time!")
    
    elif len(attachments) == 1:
        edit_embed.set_image(url=attachments[0].url)

        await ctx.send(embed=edit_embed)
    
@bot.command()
async def test(ctx):
    view = SimpleView()
    button = discord.ui.Button(label="Click me")
    view.add_item(button)
    await ctx.send(view=view)


bot.run(TOKEN)
