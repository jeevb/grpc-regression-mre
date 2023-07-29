cert:
	mkdir -p cert
	openssl req -newkey rsa:2048 -nodes -keyout cert/server.key -x509 -days 365 -out cert/server.crt -subj '/CN=localhost'

.PHONY: up
up:
	docker compose up --build --detach --remove-orphans --wait

.PHONY: restart
restart:
	docker compose restart

.PHONY: down
down:
	docker compose down --volumes
