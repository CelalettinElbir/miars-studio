#!/bin/sh

# PostgreSQL'in hazır olmasını bekleyelim
echo "PostgreSQL başlatılıyor..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done
echo "PostgreSQL başlatıldı"

# Migrasyonları uygula
python manage.py migrate

# Statik dosyaları topla
python manage.py collectstatic --noinput

exec "$@"