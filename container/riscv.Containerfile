FROM docker.io/riscv64/python:3.10-alpine

RUN python -m pip install -U stream_recorder
CMD ["/usr/local/bin/stream_recorder"]

