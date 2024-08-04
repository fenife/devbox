
include $(BASE_OPT_DIR)/include/Makefile.common

ECHO_APP_IMAGE=echo-app:latest
REGISTER_ECHO_APP_IMAGE=register.dev.local:5000/echo-app:latest
ECHO_APP_NAME=echo-app
CLUSTER_NAME=local

start-pod:
	kubectl apply -f rs.yaml

stop-pod:
	kubectl delete -f rs.yaml

start-svc:
	kubectl apply -f svc.yaml

stop-svc:
	kubectl delete -f svc.yaml

start: start-pod start-svc

clean: stop-pod stop-svc

tag:
	docker tag $(ECHO_APP_IMAGE) $(REGISTER_ECHO_APP_IMAGE)

# kind load docker-image $(REGISTER_ECHO_APP_IMAGE) --name $(CLUSTER_NAME)
load: 
	kind load docker-image $(ECHO_APP_IMAGE) --name $(CLUSTER_NAME)

push: tag		## push image to local registry
	docker push $(REGISTER_ECHO_APP_IMAGE)


############################################################
# pod runtime
############################################################
NODE := local-worker
POD := echo-app-mbzxt 
SVC_IP := 10.96.101.125
SVC_DNS := echo-svc.default

NODE_EXEC := docker exec -it $(NODE)
POD_EXEC := kubectl exec $(POD) --

atn:
	docker exec -it $(NODE) bash

atp:
	kubectl exec -it $(POD) bash

# curl service ip from node
ping1:
	$(NODE_EXEC) curl -s http://$(SVC_IP):6000

# curl service dns name from pod
# see: file in pod: /etc/resolv.conf
ping2: 
	$(POD_EXEC) cat /etc/resolv.conf
	@echo
	$(POD_EXEC) curl -s http://$(SVC_DNS):6000
