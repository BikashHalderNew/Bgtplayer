FROM python:3.11.6
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir --upgrade --requirement Installer
CMD python3 -m Bikash
