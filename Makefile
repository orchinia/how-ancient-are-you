# Project Makefile for Flask + MySQL + Docker Compose

APP_SERVICE = flask-app

start-mysql:
	docker run \
		--name mysql \
		-e MYSQL_ROOT_PASSWORD=rootpass \
		-e MYSQL_DATABASE=mydb \
		-e MYSQL_USER=admin \
		-e MYSQL_PASSWORD=admin \
		-p 3306:3306 \
		-v $(pwd)/data/mysql:/var/lib/mysql \
		--rm \
		mysql:8.0

build-host:
	docker build -t $(APP_SERVICE):latest .

start-host:
	docker run \
		--name host \
		-p 8888:8888 \
		-v ./:/app \
		--rm \
		flask-app:latest

host-shell:
	docker exec -it host /bin/bash
