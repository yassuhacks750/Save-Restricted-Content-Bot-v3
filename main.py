import asyncio
import importlib
import os
from shared_client import start_client

async def load_and_run_plugins(client):
    for file in os.listdir("plugins"):
        if file.startswith("__") or not file.endswith(".py"):
            continue
        module = importlib.import_module(f"plugins.{file[:-3]}")
        if hasattr(module, "run_plugin"):
            print(f"Running plugin: {file}")
            await module.run_plugin(client)

async def main():
    bot_token = os.getenv("BOT_TOKEN")
    client = await start_client(bot_token)
    await load_and_run_plugins(client)

if __name__ == "__main__":
    asyncio.run(main())
