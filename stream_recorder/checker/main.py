from stream_recorder.core import common
import stream_recorder.checker.channels
import stream_recorder.checker.timeout
import rich.live


async def render_all() -> None:
    with rich.live.Live(
        auto_refresh=False,
    ) as common.live:
        while True:
            await stream_recorder.checker.channels.render_channels()
            await stream_recorder.checker.timeout.render_timeout()


async def main():
    await render_all()

