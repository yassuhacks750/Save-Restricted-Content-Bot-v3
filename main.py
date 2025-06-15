import asyncio
from shared_client import start_client
import importlib, os, sys

async def load_and_run_plugins(client, app, userbot):
    plugins = os.listdir("plugins")
    for file in plugins:
        if not file.endswith(".py") or file.startswith("__"):
            continue
        name = file[:-3]
        module = importlib.import_module(f"plugins.{name}")
        if hasattr(module, "run_plugin"):
            print(f"Running plugin: {name}")
            await module.run_plugin(client, app, userbot)

async def main():
    client, app, userbot = await start_client()
    await load_and_run_plugins(client, app, userbot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped by user.")
