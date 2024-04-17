FROM python:3.10

WORKDIR /app


COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV PYTHONPATH "/app/:/app/api/:${PYTHONPATH}"

COPY ./static/image /app/api/static/image

WORKDIR /app

CMD alembic upgrade head && python3 main.py
