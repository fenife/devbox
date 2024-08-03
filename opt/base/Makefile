
include $(BASE_OPT_DIR)/include/Makefile.common

CENTOS_BASE_IMAGE=centos-base:7.9
CENTOS_NAME=centos-base-7

build: 
	docker build -t $(CENTOS_BASE_IMAGE) .

start: 
	docker run --rm -it --privileged \
	--add-host="$(HOST_NAME):$(HOST_IP)"  \
	--name $(CENTOS_NAME) --hostname $(CENTOS_NAME) \
	$(CENTOS_BASE_IMAGE)

stop:
	docker stop $(CENTOS_NAME)
	docker rm $(CENTOS_NAME)

enter:
	docker exec -it $(CENTOS_NAME) zsh


