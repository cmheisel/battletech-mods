SHELL := /bin/bash

.PHONY: build
build:
	docker-compose build
	docker-compose run btmods main.sh

.PHONY: clean
clean:
	docker-compose rm -f --all
	docker rmi -f btmods || true

.PHONY: enter
enter:
	docker-compose build
	docker run -ti --mount type=bind,src=./,dst=/app btmods /bin/bash

.PHONY: test
test:
	docker-compose run btmods test.sh

.PHONY: deepclean
deepclean:
	docker system prune -fa