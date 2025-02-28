from stream_recorder.core import config
import rich.progress
import rich.console
import rich.table
import rich.live
import logging
import typing


channels_dict: dict[str, str] = {}
recording_dict: dict[str, typing.Any] = {}
group: rich.console.Group
table: rich.table.Table
live: rich.live.Live
progress: rich.progress.Progress = rich.progress.Progress(
    rich.progress.TextColumn("[progress.description]{task.description}"),
    rich.progress.BarColumn(),
    rich.progress.MofNCompleteColumn(),
    auto_refresh=False,
)


class tasks:
    channels: rich.progress.TaskID = progress.add_task(
        description='checking channels',
        total=len(config.channels_list),
        visible=False,
    )
    timeout: rich.progress.TaskID = progress.add_task(
        description='timeout',
        total=config.timeout,
        visible=False,
    )


class no_output:
    logger = logging.getLogger('ignore')
    logger.setLevel(logging.CRITICAL)
    params = {
        'logger': logger
    }


