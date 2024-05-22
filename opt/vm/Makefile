
include ../Makefile.common

############################################################
# network 
############################################################

NET=vm-net
NET0=vm-net0
NET1=vm-net1
NET2=vm-net2

net-create:
	docker network create --driver=bridge --subnet=172.20.0.0/24 --gateway=172.20.0.1 $(NET0)
	docker network create --driver=bridge --subnet=172.20.1.0/24 --gateway=172.20.1.1 $(NET1)
	docker network create --driver=bridge --subnet=172.20.2.0/24 --gateway=172.20.2.1 $(NET2)

net-delete:
	docker network rm $(NET0)
	docker network rm $(NET1)
	docker network rm $(NET2)

############################################################
# container
############################################################

VM_IMAGE=$(DEVC_CENTOS_IMAGE)

ZONE=0
VM=1
VM_NAME=vm$(ZONE)$(VM)
VM_NET=$(NET)$(ZONE)
VM_IP=172.20.$(ZONE).1$(VM)

start: 
	docker run --rm -it --privileged --name $(VM_NAME) --hostname $(VM_NAME) \
	--network $(VM_NET) --ip $(VM_IP) \
	-v $(DIND_DIR):/wine/dind \
	$(VM_IMAGE)

stop:
	docker stop $(VM_NAME)
	docker rm $(VM_NAME)

enter:
	docker exec -it $(VM_NAME) zsh


