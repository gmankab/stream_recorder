FROM docker.io/python:3.12

RUN python -m pip install -U stream_recorder
CMD ["/usr/local/bin/stream_recorder"]

