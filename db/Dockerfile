# Dockerfile для базы данных PostgreSQL

FROM postgres

# Копируем pg_hba.conf и init-script.sh
COPY pg_hba.conf /etc/postgresql/$PG_MAJOR/main/pg_hba.conf
COPY init-script.sh /docker-entrypoint-initdb.d/init-script.sh

# Устанавливаем права на файлы
RUN chmod 0600 /etc/postgresql/$PG_MAJOR/main/pg_hba.conf /docker-entrypoint-initdb.d/init-script.sh
