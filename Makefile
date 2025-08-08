.PHONY: build
build:
	docker-compose build
	docker-compose run --remove-orphans battletechmods main.py

.PHONY: clean
clean:
	docker-compose rm -f --all
	docker rmi -f battletechmods || true

.PHONY: enter
enter:
	docker run -ti --mount type=bind,src=./,dst=/app battletechmods /bin/bash

.PHONY: test
test:
	docker-compose run --remove-orphans battletechmods py.test