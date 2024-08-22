
include $(INC_DIR)/Makefile.common

############################################################
# build
############################################################

VMC_IMAGE=devc-vmc:latest

DEVBOX_DIR=/wine/devbox
DEVBOX_CODE_DIR=/wine/devbox/code
CODE_DIR=/wine/code


build: 		## docker build image
	docker build -f ./Dockerfile -t $(VMC_IMAGE) .

############################################################
# vmc1
############################################################
VMC_OPTIONS = \
	-d --privileged \
	--add-host="$(HOST_NAME):$(HOST_IP)"  \
	--add-host="mysql:$(HOST_IP)"  \
	--add-host="redis:$(HOST_IP)"  \
	--add-host="rabbitmq:$(HOST_IP)" \
	-v $(DEVBOX_DIR):$(DEVBOX_DIR) \
	-v $(CODE_DIR):$(CODE_DIR) 

VMC_NAME1=vmc1

start1: 		## docker start vmc1
	docker run $(VMC_OPTIONS) \
	--name $(VMC_NAME1) --hostname $(VMC_NAME1) \
	$(VMC_IMAGE)

stop1:		## docker stop vmc1
	docker stop $(VMC_NAME1)
	docker rm $(VMC_NAME1)

at1:		## attach to vmc1
	docker exec -it $(VMC_NAME1) zsh

