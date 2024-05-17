
include ../Makefile.common

CENTOS_IMAGE_FROM=centos:7.9.2009
DEVC_CENTOS_IMAGE=devc-centos-7.9:latest

CENTOS_IMAGE=$(DEVC_CENTOS_IMAGE)
CENTOS_NAME=centos7
CENTOS_DATA_DIR=$(ROOT_DIR)/var/centos

pull:
	docker pull $(CENTOS_IMAGE)

build: 
	docker build -t $(CENTOS_IMAGE) .

start: 
	docker run --rm -it --privileged \
	--name $(CENTOS_NAME) --hostname $(CENTOS_NAME) \
	$(CENTOS_IMAGE)

stop:
	docker stop $(CENTOS_NAME)
	docker rm $(CENTOS_NAME)

enter:
	docker exec -it $(CENTOS_NAME) bash

run: start


