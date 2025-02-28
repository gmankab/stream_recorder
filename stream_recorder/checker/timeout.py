from stream_recorder.core import common, config
import stream_recorder.checker.etc
import datetime
import asyncio


async def render_timeout() -> None:
    common.progress.update(
        task_id=common.tasks.timeout,
        visible=True,
    )
    now = datetime.datetime.now()
    end = now + datetime.timedelta(seconds=config.timeout)
    while True:
        now = datetime.datetime.now()
        if now > end:
            break
        delta = end - now
        completed = 10 - delta.total_seconds()
        common.progress.update(
            task_id=common.tasks.timeout,
            completed=completed,
            refresh=True,
        )
        stream_recorder.checker.etc.render()
        await asyncio.sleep(0.1)
    common.progress.update(
        task_id=common.tasks.timeout,
        completed=config.timeout,
        visible=False,
    )

