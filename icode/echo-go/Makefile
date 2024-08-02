

ECHO_SRV_IMAGE=echo-srv:latest
ECHO_SRV_NAME=echo-srv

build: 
	docker build -t $(ECHO_SRV_IMAGE) .

start: 
	docker run --rm -it \
	--name $(ECHO_SRV_NAME) --hostname $(ECHO_SRV_NAME) \
	-p 6000:6000 \
	$(ECHO_SRV_NAME)

stop:
	docker stop $(ECHO_SRV_NAME)
	docker rm $(ECHO_SRV_NAME)

enter:
	docker exec -it $(ECHO_SRV_NAME) bash

