import discord
import random
import asyncio


class MyClient(discord.Client):
    async def on_ready(self):
        #在PowerShell上print資訊
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):#訊息函式
        # 不要讓他自己回覆自己
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith('!嗨'):
            await message.reply('銃三小 低能兒', mention_author=True)

        if message.content.startswith('!猜數字'):
            await message.channel.send('1~10猜個數字')

            def is_correct(m):
                return m.author == message.author and m.content.isdigit()

            answer = random.randint(1, 10)

            try:
                guess = await self.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send(f'要不要打字啦 操 答案:{answer}.')

            if int(guess.content) == answer:
                await message.channel.send('對了啦 阿不就好棒棒')
            else:
                await message.channel.send(f'笨小孩是{answer}啦幹')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('token')