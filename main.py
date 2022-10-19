import discord
import json
import random
import asyncio
#Python 3.10.8

data = json.load(open('setting.json'))


class MyClient(discord.Client):
    async def on_ready(self):
        print('------')
        print(f'{self.user}上線LOL')
        print('------')

    async def on_message(self, message):
        # 讓他不要一直回自己的訊息
        if message.author.id == self.user.id:
            return
        # 嗨
        if message.content.startswith('!嗨'):
            await message.reply('銃三小 低能兒', mention_author=True)
        # 猜數字
        if message.content.startswith('!猜數字'):
            await message.channel.send('1~10猜個數字')
            def is_correct(m):
                return m.author == message.author and m.content.isdigit()
            answer = random.randint(1, 10)
            try:#如果過5秒沒回答
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:#執行
                return await message.channel.send(f'要不要打字啦 操 答案:{answer}')

            if int(guess.content) == answer:
                await message.channel.send('對了啦 阿不就好棒棒')
            else:
                await message.channel.send(f'笨小孩是{answer}啦幹')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(data['TOKEN'])