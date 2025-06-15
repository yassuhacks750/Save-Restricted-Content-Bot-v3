import os
import asyncio
from telethon import TelegramClient
from telethon.errors import FloodWaitError

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

async def start_client(bot_token):
    client = TelegramClient("bot", api_id, api_hash)
    try:
        await client.start(bot_token=bot_token)
    except FloodWaitError as e:
        print(f"[Telethon] Flood wait: {e.seconds} seconds. Waiting...")
        await asyncio.sleep(e.seconds)
        await client.start(bot_token=bot_token)
    return client
