
include ./Makefile.common

############################################################
# network 
############################################################

NET=dind-net
NET0=dind-net0
NET1=dind-net1
NET2=dind-net2

net-create:
	docker network create --driver=bridge --subnet=192.168.0.0/24 --gateway=192.168.0.1 \
	-o com.docker.network.bridge.name=br-$(NET0) $(NET0)
	docker network create --driver=bridge --subnet=192.168.1.0/24 --gateway=192.168.1.1 \
	-o com.docker.network.bridge.name=br-$(NET2) $(NET1)
	docker network create --driver=bridge --subnet=192.168.2.0/24 --gateway=192.168.2.1 \
	-o com.docker.network.bridge.name=br-$(NET2) $(NET2)

net-delete:
	docker network rm $(NET0)
	docker network rm $(NET1)
	docker network rm $(NET2)

############################################################
# container
############################################################

VM_IMAGE=dind-alpine-3.19:latest

ZONE=0
VM=1
VM_NAME=dind$(ZONE)$(VM)
VM_NET=$(NET)$(ZONE)
VM_IP=192.168.$(ZONE).1$(VM)

start: 
	docker run --rm -it --privileged --name $(VM_NAME) --hostname $(VM_NAME) \
	--network $(VM_NET) --ip $(VM_IP) \
	$(VM_IMAGE)

stop:
	docker stop $(VM_NAME)
	docker rm $(VM_NAME)

enter:
	docker exec -it $(VM_NAME) bash


