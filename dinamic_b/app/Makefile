#!/usr/bin/make


help:
	@echo "make"
	@echo "	hello"
	@echo "		print hello world"

hello:
	echo "Hello, World"
run:
	python3 main.py
alembic-init:
	alembic init migrations
alembic-gen:
	alembic revision --autogenerate -m "$(ARGS)"
alembic-head:
	alembic upgrade head