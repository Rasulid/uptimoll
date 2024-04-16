FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

#ENV PYTHONPATH "${PYTHONPATH}:/app/"
ENV PYTHONPATH "${PYTHONPATH}:/api"

RUN mkdir -p /api/static/image

COPY ./static/image /api/static/image

CMD alembic upgrade head && uvicorn main:app --host "0.0.0.0" --port 8000 --workers 4 --reload
