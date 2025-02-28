from stream_recorder.core import common, config
import stream_recorder.recorder.recorder
import stream_recorder.checker.etc
import rich.table
import rich.box
import asyncio
import typing


async def render_channels() -> None:
    common.progress.update(
        task_id=common.tasks.channels,
        visible=True,
    )
    tasks: list[typing.Coroutine] = []
    for url in config.channels_list:
        if url in common.recording_dict:
            recorder: stream_recorder.recorder.recorder.Recorder = common.recording_dict[url]
            common.channels_dict[url] = recorder.msg
        else:
            common.channels_dict[url] = '[yellow]checking...'
            tasks.append(check_and_update(url))
    update_table()
    stream_recorder.checker.etc.render()
    await asyncio.gather(*tasks)
    common.progress.update(
        task_id=common.tasks.channels,
        visible=False,
    )


async def check_and_update(
    url: str,
) -> None:
    if await stream_recorder.checker.etc.is_live(url):
        recorder = stream_recorder.recorder.recorder.Recorder(url)
        common.recording_dict[url] = recorder
        common.channels_dict[url] = recorder.msg
        recorder.recodrd_in_background()
    else:
        common.channels_dict[url] = '[orange1]no stream'
    update_table()


def update_table() -> None:
    common.table = rich.table.Table(
        show_header=False,
        box=rich.box.MINIMAL,
    )
    completed: int = 0
    for channel, status in common.channels_dict.items():
        if status != '[yellow]checking...':
            completed += 1
        common.table.add_row(channel, status)
    common.progress.update(
        task_id=common.tasks.channels,
        completed=completed,
        refresh=True,
    )
    stream_recorder.checker.etc.render()

