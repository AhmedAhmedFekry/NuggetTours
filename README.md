# NuggetTours
# to run this project using docker 
--- sudo docker-compose -f docker-compose-local.yml build
--- sudo docker-compose -f docker-compose-local.yml up -d
---sudo docker-compose -f docker-compose-local.yml run nugget_django python manage.py makemigrations
--- sudo docker-compose -f docker-compose-local.yml run nugget_django python manage.py migrate 
