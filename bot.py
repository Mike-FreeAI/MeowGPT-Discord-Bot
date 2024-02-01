import os
os.system("pip install splitticapi")
os.system("pip install discord")
os.system("pip install asyncio")
from SplitticAPI.meowgpt import ChatModule
import discord
import config
import asyncio

class Client(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.messages = True
        intents.message_content = True
        super().__init__(intents=intents, activity=discord.CustomActivity(config.activity),
                         allowed_mentions=discord.AllowedMentions(everyone=False, users=False, roles=False, replied_user=True))

    async def update_activity(self):
        await self.wait_until_ready()
        while not self.is_closed():
            guild_count = len(self.guilds)
            user_count = len(chats)
            new_activity = discord.CustomActivity(config.activity.format(s=guild_count, u=user_count))
            await self.change_presence(activity=new_activity)
            await asyncio.sleep(10)

client = Client()
ChatModule.initialize(config.api_key)
prompt = open('prompt.txt', 'r').read()
chats = {}

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    client.loop.create_task(client.update_activity())

@client.event
async def on_message(message):
    if message.channel.id in config.channel_ids and not message.author.bot:
        if not str(message.channel.id) + '-' + str(message.author.id) in chats:
            chat_instance = ChatModule.create_chat(config.api_key)
            chats[str(message.channel.id) + '-' + str(message.author.id)] = chat_instance
            if prompt != "":
                await chat_instance.async_reply(prompt)
        chat_instance = chats[str(message.channel.id) + '-' + str(message.author.id)]
        async with message.channel.typing():
            response = await chat_instance.async_reply(message.content)
        for i in range(0, len(response), 2000):
            chunk = response[i:i+2000]
            await message.reply(chunk)

client.run(config.token)
