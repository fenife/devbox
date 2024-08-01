
include $(BASE_OPT_DIR)/include/Makefile.common

############################################################
# venv
############################################################

############################################################
# cvm1
############################################################
CVM_IMAGE=devc-cvm:latest
CVM_NAME=cvm1

DEVBOX_DIR=/wine/devbox
DEVBOX_CODE_DIR=/wine/devbox/code
CODE_DIR=/wine/code

build: 		## docker build image
	docker build -f ./Dockerfile \
	--build-arg IMAGE_FROM="$(DEVC_CENTOS_IMAGE)" \
	-t $(CVM_IMAGE) \
	.

CVM_OPTIONS = \
	-d --privileged \
	--add-host="$(HOST_NAME):$(HOST_IP)"  \
	--add-host="mysql:$(HOST_IP)"  \
	--add-host="redis:$(HOST_IP)"  \
	--add-host="rabbitmq:$(HOST_IP)" \
	-v $(DEVBOX_DIR):$(DEVBOX_DIR) \
	-v $(CODE_DIR):$(CODE_DIR) 

start: 		## docker start container
	docker run $(CVM_OPTIONS) \
	--name $(CVM_NAME) --hostname $(CVM_NAME) \
	$(CVM_IMAGE)

stop:		## docker stop container
	docker stop $(CVM_NAME)
	docker rm $(CVM_NAME)

enter:		## attach to container
	docker exec -it $(CVM_NAME) zsh

