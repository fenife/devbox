
include ../../include/Makefile.common

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
	kubectl get nodes -o wide
	@echo
	kubectl get pods -o wide --all-namespaces






