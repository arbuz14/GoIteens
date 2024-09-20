import asyncio
import logging
import sys
from telegram_bot.project.project.app.data import main as app_main

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(app_main())

