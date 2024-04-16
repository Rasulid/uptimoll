FROM python:3.10

WORKDIR /app


COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV PYTHONPATH "/app/:/app/api/:${PYTHONPATH}"



COPY ./static/image /app/api/static/image




WORKDIR /app/api

CMD alembic upgrade head && uvicorn main:app --host "0.0.0.0" --port 8000 --workers 4 --reload
