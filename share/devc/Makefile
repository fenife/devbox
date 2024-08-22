
include $(INC_DIR)/Makefile.common

############################################################
# build
############################################################
VMC_IMAGE=devc-vmc:latest

build: 		## docker build image
	docker build -f ./Dockerfile -t $(VMC_IMAGE) .

############################################################
# vmc1
############################################################
VMC_NAME1=vmc1

start1: 		## docker start vmc1
	docker run -d $(DEVC_WITH_OPTIONS) \
	--name $(VMC_NAME1) --hostname $(VMC_NAME1) \
	$(VMC_IMAGE)

stop1:		## docker stop vmc1
	docker stop $(VMC_NAME1)
	docker rm $(VMC_NAME1)

at1:		## attach to vmc1
	docker exec -it $(VMC_NAME1) zsh

