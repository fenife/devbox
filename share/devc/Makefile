
include $(INC_DIR)/Makefile.common

############################################################
# build
############################################################

CVM_IMAGE=devc-cvm:latest

DEVBOX_DIR=/wine/devbox
DEVBOX_CODE_DIR=/wine/devbox/code
CODE_DIR=/wine/code


build: 		## docker build image
	docker build -f ./Dockerfile -t $(CVM_IMAGE) .

############################################################
# cvm1
############################################################
CVM_OPTIONS = \
	-d --privileged \
	--add-host="$(HOST_NAME):$(HOST_IP)"  \
	--add-host="mysql:$(HOST_IP)"  \
	--add-host="redis:$(HOST_IP)"  \
	--add-host="rabbitmq:$(HOST_IP)" \
	-v $(DEVBOX_DIR):$(DEVBOX_DIR) \
	-v $(CODE_DIR):$(CODE_DIR) 

CVM_NAME1=cvm1

start1: 		## docker start cvm1
	docker run $(CVM_OPTIONS) \
	--name $(CVM_NAME1) --hostname $(CVM_NAME1) \
	$(CVM_IMAGE)

stop1:		## docker stop cvm1
	docker stop $(CVM_NAME1)
	docker rm $(CVM_NAME1)

at1:		## attach to cvm1
	docker exec -it $(CVM_NAME1) zsh

