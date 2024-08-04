

ECHO_APP_IMAGE=echo-app:latest
ECHO_APP_NAME=echo-app

build: 
	docker build -t $(ECHO_APP_IMAGE) .

start: 
	docker run --rm -it \
	--name $(ECHO_APP_NAME) --hostname $(ECHO_APP_NAME) \
	-p 6000:6000 \
	$(ECHO_APP_NAME)

stop:
	docker stop $(ECHO_APP_NAME)
	docker rm $(ECHO_APP_NAME)

enter:
	docker exec -it $(ECHO_APP_NAME) bash

