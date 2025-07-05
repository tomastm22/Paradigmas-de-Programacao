FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && pip3 install --no-cache-dir pandas \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY process.py .

CMD ["python3", "process.py"]