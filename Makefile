all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build: delete-container ## Build the container
	@[ -f .env ] || cp template.env .env
	@docker-compose up --build -d

test: start ## Run tests
	@docker-compose exec backend pytest

restart: ## Restart the container
	@docker-compose restart

cmd: start ## Access bash
	@docker-compose exec app /bin/bash

up: start ## Start Fastapi dev server
	@docker-compose exec app uvicorn api:app --host 0.0.0.0 --reload

start:
	@docker-compose start

stop: ## Stop container
	@docker-compose stop || true

delete-container: stop
	@docker-compose down || true

remove: delete-container ## Delete containers and images

docs: start
	@docker-compose exec backend pdoc --html backend/app -o docs --force

.DEFAULT_GOAL := help