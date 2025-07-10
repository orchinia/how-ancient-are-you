# Project Makefile for Flask + MySQL + Docker Compose

APP_SERVICE = flask-app

build:
	docker-compose build

up:
	docker-compose up

logs:
	docker-compose logs -f $(APP_SERVICE)

shell:
	docker-compose exec $(APP_SERVICE) bash
