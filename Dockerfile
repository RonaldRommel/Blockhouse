FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

COPY ./data /code/data


EXPOSE 8000

CMD ["uvicorn" ,"app.main:app", "--host", "0.0.0.0", "--port", "8000"]