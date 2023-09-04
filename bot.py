import discord
from discord.ext import commands

app = commands.Bot(command_prefix='/', intents=discord.Intents.all())  # 명령어 접두사


@app.event
async def on_ready():
    print(f"{app.user.name} 연결 성공")
    await app.change_presence(status=discord.Status.online, activity=None)


@app.command()
async def hello(ctx):
    await ctx.send("hello, world!")


@app.command(aliases=["따라하기", "f"])
async def follow(ctx, *args):
    for elem in args:
        await ctx.send(f"```{elem}```")


# 메시지를 받을 때마다 생성되는 이벤트 -> add_reaction method를 통해서 이모지를 달아준다.
@app.event
async def on_message(msg):
    await msg.add_reaction("👍")


app.run("")
