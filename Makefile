ENV_PATH?=.env
APP_ENV?=local
APP_NAME?=weather
HOST?=0.0.0.0
PORT?=8000

PYTHONPATH+=$(PWD)/src


.PHONY: env-setup
env-setup:
	@virtualenv -q -p python3 $(ENV_PATH);
	@make env-update


.PHONY: env-update
env-update:
	@. $(ENV_PATH)/bin/activate && pip -q install -r requirements.txt


.PHONY: clean
clean:
	@rm -rf $(ENV_PATH)
	@find . -name "*.pyc" -exec rm -rf {} \; -prune -print
	@find . -name "__pycache__" -exec rm -rf {} \; -prune -print


.PHONY: db-makemigrations
db-makemigrations:
	@. $(ENV_PATH)/bin/activate && APP_ENV=$(APP_ENV) python src/$(APP_NAME)/manage.py makemigrations


.PHONY: db-migrate
db-migrate:
	@. $(ENV_PATH)/bin/activate && APP_ENV=$(APP_ENV) python src/$(APP_NAME)/manage.py migrate


.PHONY: run
run:
	@. $(ENV_PATH)/bin/activate && APP_ENV=$(APP_ENV) python src/$(APP_NAME)/manage.py runserver $(HOST):$(PORT)


.PHONY: createsuperuser
createsuperuser:
	@. $(ENV_PATH)/bin/activate && APP_ENV=$(APP_ENV) python src/$(APP_NAME)/manage.py createsuperuser


.PHONY: test
test:
	@. $(ENV_PATH)/bin/activate && cd src/$(APP_NAME) && ./manage.py test


.PHONY: test-app
test-app:
	@. $(ENV_PATH)/bin/activate && cd src/$(APP_NAME) && ./manage.py test ${APP} $(DJANGO_SETTINGS)


.PHONY: weather-curl
weather-curl:
	curl http://$(HOST):$(PORT)/weather/?city=${CITY}\&format=${FORMAT} -v
