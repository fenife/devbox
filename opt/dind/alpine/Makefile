
include ../Makefile.common

ALPINE_IMAGE_FROM=alpine:3.19
ALPINE_IMAGE=dind-alpine-3.19:latest
ALPINE_NAME=alpine3

pull:
	docker pull $(ALPINE_IMAGE_FROM)

build: 
	docker build -t $(ALPINE_IMAGE) .

start: 
	docker run --rm -it \
	--name $(ALPINE_NAME) --hostname $(ALPINE_NAME) \
	$(ALPINE_IMAGE)

stop:
	docker stop $(ALPINE_NAME)
	docker rm $(ALPINE_NAME)

enter:
	docker exec -it $(ALPINE_NAME) bash


