#!/bin/bash

# Apply database migrations
echo "Applying database migrations"
docker-compose exec web python manage.py migrate

# Create superuser if needed
echo "Do you want to create a superuser? (y/n)"
read create_superuser
if [ "$create_superuser" = "y" ]; then
    docker-compose exec web python manage.py createsuperuser
fi

# Restart all services
echo "Restarting all services"
docker-compose restart

echo "Deployment complete!"
