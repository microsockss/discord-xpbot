import discord
import asyncio
import logging


# Set these variables
message = 'MESSAGE'
email = 'LOGIN EMAIL'
password = 'PASSWORD'
channel = discord.Object(id='CHANNEL ID')


client = discord.Client()
async def run():
    await client.wait_until_ready()
    while not client.is_closed:
        await client.send_message(channel, message)
        await asyncio.sleep(60)
logging.basicConfig(level=logging.INFO)
client.loop.create_task(run())
client.run(email, password)
