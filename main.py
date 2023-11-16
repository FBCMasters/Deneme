import discord
import os
from discord.ext import commands
from commands import *

intents = discord.Intents.default()
intents.message_content = True
import discord
import os
from discord.ext import commands
from commands import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged as FBC')

@bot.command()
async def Hello(ctx):
    await ctx.send(f'Hello FBC! I hack you!')

@bot.command()
async def He(ctx, count_he = 3):
    await ctx.send("He" * count_he)

@bot.command()
async def Bye(ctx):
    await ctx.send(f'Bye FBC:wave:! I hack you!')

@bot.command()
async def Commands(ctx):
    await ctx.send(f'Say /Help to see commands FBC!')

@bot.command()
async def Emoji(ctx):
    await ctx.send(RandomEmoji())

@bot.command()
async def Bruh(ctx):
    with open('Images/Bruh/MUGBRUH.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def AmongUs(ctx):
    RNameA = random.choice(os.listdir('Images/AmongUs'))
    with open(f'Images/AmongUs/{RNameA}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def Joke(ctx):
    RNameM = random.choice(os.listdir('Images/Funny'))
    with open(f'Images/Funny/{RNameM}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send("Sakın virüs indirme şaka değil tüm bilgisayarın çöker")
        await ctx.send("https://random-d.uk")


@bot.command()
async def YazıTura(ctx, count_Yazı = "Yazı"):
    await ctx.send(YazıTura(count_Yazı))

#@bot.command()
#async def MakePassword(ctx, count_password = 23):
#    await ctx.send(MakePassword(count_password))

@bot.command()
async def Secret(ctx, count_secret = "1, 2"):
    SecretWord = double(count_secret)
    await ctx.send(SecretWord)

@bot.command()
async def Help(ctx):
    await ctx.send(f'/Hello')
    await ctx.send(f'/He 4')
    await ctx.send(f'/Bye')
    await ctx.send(f'/Emoji')
    await ctx.send(f'/YazıTura Yazı')
#    await ctx.send(f'/MakePassword 30')
    await ctx.send(f'/Secret 1, 2')
    await ctx.send(f'/Bruh')
    await ctx.send(f'/AmongUs')
    await ctx.send(f'/Joke')
    await ctx.send(f'/Commands')
    await ctx.send(f'/Help')

bot.run("Token")
