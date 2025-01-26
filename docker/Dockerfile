FROM python:3.12

WORKDIR /app

COPY ./req.txt .
RUN pip install -r req.txt

COPY . .

CMD ["python", "manage.py", "runserver"]