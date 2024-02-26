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

# Копируем pg_hba.conf и init-script.sh
COPY pg_hba.conf /etc/postgresql/$PG_MAJOR/main/pg_hba.conf
COPY init-script.sh /docker-entrypoint-initdb.d/init-script.sh

# Устанавливаем права на файлы
RUN chmod 0600 /etc/postgresql/$PG_MAJOR/main/pg_hba.conf /docker-entrypoint-initdb.d/init-script.sh

# Экспортируем порт, который будет использоваться в Flask приложении
EXPOSE 5000

# Команда для запуска Flask приложения с использованием Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
