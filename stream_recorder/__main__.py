from pathlib import Path
import asyncio
import sys
sys.path.append(str(Path(__file__).parent.parent.resolve()))
import stream_recorder.checker.main
import stream_recorder.recorder.recorder


async def async_main():
    await stream_recorder.checker.main.main()


def main():
    asyncio.run(async_main())


if __name__ == '__main__':
    main()

