import discord
from discord.ext import commands

token = ""

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())  # 명령어 접두사 /


@bot.event
async def on_ready():
    print(f"{bot.user.name} 연결 성공")
    await bot.change_presence(status=discord.Status.online, activity=None)


@bot.command()
async def hello(ctx):
    await ctx.send("Hello ~")


@bot.command()
async def game(ctx):
    embed = discord.Embed(title="무슨 게임할까?", description=" ", color=discord.Color.random())
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/5847/5847894.png")
    embed.add_field(name="1. 피파온라인 4", value="[피파온라인 4 바로가기](https://fifaonline4.nexon.com/main/index)", inline=False)
    embed.add_field(name="2. 서든어택", value="[서든어택 바로가기](https://event.sa.nexon.com/230817/intro)", inline=False)
    embed.add_field(name="3. 배틀그라운드", value="[배틀그라운드 바로가기](https://pubg.game.daum.net/pubg/index.daum)", inline=False)
    embed.set_footer(text="오늘 하루도 즐겜하세요 👍")
    await ctx.send(embed=embed)


@bot.command(aliases=["따라하기", "f"])
async def follow(ctx, *args):
    for elem in args:
        await ctx.send(f"```{elem}```")


# 메시지를 받을 때마다 생성되는 이벤트 -> add_reaction method를 통해서 이모지를 달아준다.
"""
@bot.event
async def on_message(msg):
    await msg.add_reaction("👍")
"""

bot.run(token)
