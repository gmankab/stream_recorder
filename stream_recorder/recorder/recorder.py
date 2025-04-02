from stream_recorder.core import config, common
from pathlib import Path
import yt_dlp.utils
import datetime
import logging
import yt_dlp
import asyncio


class Recorder:
    def __init__(
        self,
        url: str,
    ) -> None:
        self.url: str = url
        now: str = datetime.datetime.now().strftime('%Y.%m.%d_%H-%M-%S')
        url_replaced = url.replace('/', '_')
        name: str = f'{now}_{url_replaced}'
        self.dir: Path = config.data / name
        self.log: Path = self.dir / 'log.txt'
        self.dir.mkdir(
            parents=True,
            exist_ok=True,
        )
        self.msg: str = f'[green]recording {self.dir}'
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(logging.FileHandler(self.log))
        self.params: dict = {
            'logger': self.logger,
            'paths': {'home': str(self.dir)},
            'quiet': True,
            'keepvideo': True,
        }
        self.task: asyncio.Task

    def recodrd_in_background(self) -> None:
        self.task = asyncio.create_task(
            coro=self.record_async(),
        )

    async def record_async(self) -> None:
        await asyncio.to_thread(
            self.record_sync
        )
        common.recording_dict.pop(self.url)
        del self

    def record_sync(self) -> None:
        try:
            self.live_from_start()
        except yt_dlp.utils.DownloadError:
            self.no_live_from_start()

    def live_from_start(self) -> None:
        params = self.params.copy()
        params['live_from_start'] = True
        with yt_dlp.YoutubeDL(params) as ydl:
            ydl.download(self.url)

    def no_live_from_start(self) -> None:
        params = self.params.copy()
        params['no_live_from_start'] = True
        with yt_dlp.YoutubeDL(params) as ydl:
            ydl.download(self.url)

