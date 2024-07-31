# make up starts docker compose
docker_app_dir := /app

status:
		docker-compose ps

stop:
		docker-compose stop

clean:
		docker-compose rm --stop

destroy:
		docker-compose rm --stop
		docker rmi -f $(shell docker-compose images -q)

up:
		docker-compose up --build -d
		docker-compose ps