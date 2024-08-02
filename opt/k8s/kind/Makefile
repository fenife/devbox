
include $(BASE_OPT_DIR)/include/Makefile.common

CLUSTER_NAME=local

start:
	kind create cluster --config=cluster.yaml

stop:
	kind delete cluster -n $(CLUSTER_NAME)

ctx:
	kubectl cluster-info --context kind-$(CLUSTER_NAME)

ver:
	kubectl version

info:
	kubectl cluster-info
	@echo
	kubectl get nodes -o wide
	@echo
	kubectl get pods -o wide --all-namespaces


# IMAGE := ubuntu:24.10
# IMAGE := ubuntu:22.04
# IMAGE := ubuntu:20.04
# IMAGE := golang:1.22.5
IMAGE := python:3.12.4
pull:
	docker pull m.daocloud.io/docker.io/$(IMAGE)
	docker tag m.daocloud.io/docker.io/$(IMAGE) $(IMAGE)






