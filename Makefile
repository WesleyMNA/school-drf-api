install-api:
	docker-compose pull
	docker-compose up -d --build
	docker-compose run school-api python manage.py migrate
