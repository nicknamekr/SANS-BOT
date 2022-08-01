from discord.ext import commands
import os, discord
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

load_dotenv(verbose=True)
bot = commands.Bot(command_prefix=["ㅅ", "샍", "샌즈!"], intents=intents)

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('ㅅhelp를 입력하샌즈.'))

@bot.command(name = "샌즈", alias=["sans", "SANS"])
async def sans(ctx):
    await ctx.reply('와! 샌즈! 아시는구나!\nhttps://imgur.com/a/gVpTIU8')

@bot.command(name = "와", alias=["와!", "wa!", "wha!", "wa", "wha"])
async def wa(ctx):
  await ctx.reply('와! 샌즈!\nhttps://imgur.com/a/6eVnYAd')
  
@bot.command(name = "핑", alias=["ping"])
async def ping(ctx):
    await ctx.reply(f'{round(bot.latency * 1000)}ms') 

print('커멘드 로딩 완료!')

bot.load_extension('jishaku')
print('Jishaku 로딩 완료!')

bot.run(token = os.getenv('TOKEN'))
