
include ../include/Makefile.common

ALPINE_IMAGE_FROM=alpine:3.20
ALPINE_IMAGE=alpine-base:3.20
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

# 保存镜像
ALPINE_IMAGE_TAR=../dinh/vm/dind-alpine-3.19.tar
save:
	if [ -f ./${ALPINE_IMAGE_TAR} ]; then rm ./${ALPINE_IMAGE_TAR}; fi
	docker save -o ${ALPINE_IMAGE_TAR} ${ALPINE_IMAGE}

load:
	docker load -i ${ALPINE_IMAGE_TAR}

