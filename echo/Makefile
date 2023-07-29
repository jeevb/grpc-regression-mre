.venv: requirements.in
	python -m venv .venv
	source .venv/bin/activate; \
	pip install -r requirements.in

.PHONY: protoc
protoc: echo_service.proto
	source .venv/bin/activate; \
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. echo_service.proto

.PHONY: build
build:
	docker build -t grpc-service .
