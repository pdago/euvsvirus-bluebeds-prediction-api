FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

COPY requirements/requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV PYTHONPATH=":/"
COPY ./app /app