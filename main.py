
import asyncio
from contextlib import suppress

from bot.utils.launcher import process

print("Hello, World!")
print("Hello, HamsterKombatBot!")

async def main():
    await process()


if __name__ == '__main__':
    with suppress(KeyboardInterrupt, RuntimeError, RuntimeWarning):
        asyncio.run(main())
