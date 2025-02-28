from stream_recorder.core import common
import rich.console
import asyncio
import yt_dlp


async def is_live(url: str) -> bool:
    with yt_dlp.YoutubeDL(params=common.no_output.params) as ydl:
        try:
            await asyncio.to_thread(
                ydl.extract_info,
                url,
                False,
            )
        except yt_dlp.utils.YoutubeDLError:
            return False
        else:
            return True


def render() -> None:
    common.group = rich.console.Group(common.table, common.progress)
    common.live.update(
        renderable=common.group,
        refresh=True,
    )

