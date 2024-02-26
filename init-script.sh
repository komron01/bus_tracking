#!/bin/bash

# Скрипт инициализации для создания таблицы bus_data
psql -U postgres -d bus -c 'CREATE TABLE IF NOT EXISTS bus_data (data JSONB);'
