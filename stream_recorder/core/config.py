from pathlib import Path
import json


default_channels_list: list['str'] = [
    'youtube.com/@jolygolf8269/live',
    'youtube.com/@IzzyLaif/live',
    'twitch.tv/jolygames',
    'twitch.tv/jolygolf',
    'twitch.tv/izzylaif',
]
timeout: int = 10
repo: Path = Path(__file__).parent.parent.parent.resolve()
app_data: Path = Path('/app/data')
data: Path
if app_data.exists():
    data: Path = app_data
else:
    data: Path = repo / 'data'
data.mkdir(
    parents=True,
    exist_ok=True,
)
config_json: Path = data / 'config.json'
if not config_json.exists():
    config_json.write_text(json.dumps(default_channels_list))
channels_list: list['str'] = json.loads(config_json.read_text())
assert isinstance(channels_list, list)

