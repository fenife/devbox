
include ../../include/Makefile.common


CLUSTER_NAME=dev1

start:
	kind create cluster --config=cluster.yaml

stop:
	kind delete cluster -n $(CLUSTER_NAME)

ctx:
	kubectl cluster-info --context kind-$(CLUSTER_NAME)





