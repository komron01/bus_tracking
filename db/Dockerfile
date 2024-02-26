# Dockerfile для веб-приложения

FROM python:3.8

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем Gunicorn
RUN pip install gunicorn

# Копируем код в контейнер
COPY . .

# Экспортируем порт, который будет использоваться в Flask приложении
EXPOSE 5000

# Команда для запуска Flask приложения с использованием Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
