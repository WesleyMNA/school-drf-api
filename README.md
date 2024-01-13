# School DRF API

Simple API built with Django Rest Framework (DRF).

### Dependencies

| Dependency            | Description          | Version |
|-----------------------|----------------------|---------|
| Python                | Programming language | 3.11    |
| Django Rest Framework | Framework            | 3.14.0  |
| PostgreSQL            | Database             | 15      |


## Running the project

1. Clone this repository and open it with an IDE as a Maven project, set up a PostgreSQL database, run the command `python manage.py migrate` and then `python manage.py runserver`;

OR

2. If you have Docker installed, chose one of the ways described bellow:

```bash
docker-compose pull
docker-compose up -d --build
docker-compose run school-api python manage.py migrate
```

If you have [make](https://makefiletutorial.com/) installed.

```bash
make install-api
```
