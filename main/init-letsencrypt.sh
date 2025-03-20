#!/bin/bash

domains=(miarsmimarlik.com www.miarsmimarlik.com)
rsa_key_size=4096
data_path="./nginx/certbot"
email="info@miarsmimarlik.com" # SSL sertifikası için e-posta adresinizi buraya yazın
staging=0 # Let's Encrypt üretim ortamı için 0, test ortamı için 1 kullanın

# Gerekli dizinleri oluşturalım
if [ ! -e "$data_path/conf/options-ssl-nginx.conf" ] || [ ! -e "$data_path/conf/ssl-dhparams.pem" ]; then
  echo "SSL yapılandırma dosyaları oluşturuluyor..."
  mkdir -p "$data_path/conf"
  
  # ssl-dhparams.pem oluştur
  openssl dhparam -out "$data_path/conf/ssl-dhparams.pem" 2048
  
  # SSL yapılandırma dosyası oluştur
  curl -s https://raw.githubusercontent.com/certbot/certbot/master/certbot-nginx/certbot_nginx/_internal/tls_configs/options-ssl-nginx.conf > "$data_path/conf/options-ssl-nginx.conf"
fi

echo "Nginx için geçici sertifikalar oluşturuluyor..."
mkdir -p "$data_path/conf/live/$domains"

# SSL sertifikaları oluşturmak için Let's Encrypt ayarları
echo "Let's Encrypt sertifikaları alınıyor..."
domain_args=""
for domain in "${domains[@]}"; do
  domain_args="$domain_args -d $domain"
done

# Dizinleri oluştur
mkdir -p "$data_path/www"

# Docker Compose ile Nginx'i başlat
echo "Nginx başlatılıyor..."
docker-compose up -d nginx

# Let's Encrypt sertifikalarını al
echo "SSL sertifikaları alınıyor..."
docker-compose run --rm --entrypoint "\
  certbot certonly --webroot \
    --webroot-path=/var/www/certbot \
    --email $email \
    --agree-tos \
    --no-eff-email \
    --force-renewal \
    $([ $staging = 1 ] && echo "--staging") \
    $domain_args" certbot

# Nginx'i yeniden yükle
echo "Nginx yapılandırmasını yeniden yüklüyor..."
docker-compose exec nginx nginx -s reload
