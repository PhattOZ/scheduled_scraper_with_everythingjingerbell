FROM python:3.10

WORKDIR /code

COPY ./requirement.txt /code/requirement.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirement.txt

COPY ./main.py /code/

CMD [ "python", "main.py" ]

