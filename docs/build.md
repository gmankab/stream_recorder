### build python wheel

```shell
export build_dir=/tmp/stream_recorder
rm -rf $build_dir
git clone https://github.com/gmankab/stream_recorder $build_dir
python -m ensurepip
python -m pip install -U uv
python -m uv venv $build_dir/.venv
python -m uv pip install -Ur $build_dir/pyproject.toml --extra=build --python=$build_dir/.venv/bin/python
$build_dir/.venv/bin/python -m build --installer=uv $build_dir
```

