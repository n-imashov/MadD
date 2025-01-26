FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем только файл с зависимостями
COPY ./req.txt /app/req.txt

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r req.txt

# Копируем остальной код
COPY . /app

# Команда по умолчанию
CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
