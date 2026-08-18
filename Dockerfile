FROM python:3.12-slim

RUN useradd -u 10001 -m appuser

WORKDIR /app
COPY app/ /app/app/

USER 10001

ENV APP_VERSION=unknown

EXPOSE 8000
CMD ["python3", "/app/app/main.py"]
