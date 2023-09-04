# # discord-bot
- 친구들과 재밌게 게임하기 위한 디스코드 봇 만들기 


## # 마주친 Error 내용 1
```text
Traceback (most recent call last):
  File "C:\Users\dt100\PycharmProjects\discordbot\bot.py", line 4, in <module>
    app = commands.Bot(command_prefix='/')  # 명령어 접두사
TypeError: __init__() missing 1 required keyword-only argument: 'intents'
```
 해결 방법 
 - error 내용 그대로 "intents"라는 argument를 요구하는 내용이다. 즉, "intents"를 추가해주면 된다.
```text

```

# # 마주친 Error 내용 2
```text
    raise PrivilegedIntentsRequired(exc.shard_id) from None
discord.errors.PrivilegedIntentsRequired: Shard ID None is requesting privileged intents that have not been explicitly enabled in the developer portal. It is recommended to go to https://discord.com/developers/applications/ and explicitly enable the privileged intents within your application's page. If this is not possible, then consider disabling the privileged intents instead.
Exception ignored in: <function _ProactorBasePipeTransport.__del__ at 0x0000022716B8BDC0>
```
```text

```