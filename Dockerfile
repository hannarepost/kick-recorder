FROM python:3.10-slim

RUN apt-get update && apt-get install -y ffmpeg python3-pip && pip install streamlink

WORKDIR /app
COPY record.py .

CMD ["python", "record.py"]
