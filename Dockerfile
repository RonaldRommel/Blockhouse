FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

WORKDIR /code/app

RUN pip install pytest && \
    echo "export PATH=\$PATH:/root/.local/bin" >> /root/.bashrc

EXPOSE 8000

CMD ["uvicorn" ,"main:app", "--host", "0.0.0.0", "--port", "8000"]

