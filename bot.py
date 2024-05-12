import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True 

client = commands.Bot(intents=intents, command_prefix='!')

@client.command(name="joke", description="Tells you a random joke")
async def joke(ctx):
    response = requests.get("https://v2.jokeapi.dev/joke/Any?format=json")
    data = response.json()

    if data["type"] == "single":
        joke = data["joke"]
    else:
        joke = f"{data['setup']}\n\n-{data['delivery']}"

    await ctx.send(joke)

@client.command(name="meme", description="Shows you a random meme")
async def meme(ctx):
    response = requests.get("https://meme-api.com/gimme")
    data = response.json()

    meme_url = data["url"]
    title = data["title"]

    embed = discord.Embed(title=title, url=meme_url)
    embed.set_image(url=meme_url)
    await ctx.send(embed=embed)

@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")

client.run("token")
