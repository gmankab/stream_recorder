from pathlib import Path


channels_list: list['str'] = [
    'youtube.com/@jolygolf8269/live',
    'youtube.com/@IzzyLaif/live',
    'twitch.tv/jolygames',
    'twitch.tv/jolygolf',
    'twitch.tv/izzylaif',
    'twitch.tv/kalashn1koff47',
]
timeout: int = 10
repo: Path = Path(__file__).parent.parent.parent.resolve()
data: Path = repo / 'data'

