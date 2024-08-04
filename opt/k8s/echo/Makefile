
include $(BASE_OPT_DIR)/include/Makefile.common

ECHO_APP_IMAGE=echo-app:latest
REGISTER_ECHO_APP_IMAGE=register.dev.local:5000/echo-app:latest
ECHO_APP_NAME=echo-app
CLUSTER_NAME=local

start-pod:		## start pod
	kubectl apply -f rs.yaml

stop-pod:		## stop pod
	kubectl delete -f rs.yaml

start-svc:		## start svc
	kubectl apply -f svc.yaml

stop-svc:		## stop svc
	kubectl delete -f svc.yaml

start-np:		## start svc nodeport
	kubectl apply -f svc-nodeport.yaml

stop-np:		## stop svc nodeport
	kubectl delete -f svc-nodeport.yaml

start: start-pod start-svc start-np	## start all 

clean: stop-pod stop-svc stop-np	## clean all

tag:		## tag image 
	docker tag $(ECHO_APP_IMAGE) $(REGISTER_ECHO_APP_IMAGE)

# kind load docker-image $(REGISTER_ECHO_APP_IMAGE) --name $(CLUSTER_NAME)
load: 	## load image to kind
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

atn:	## attach node
	docker exec -it $(NODE) bash

atp:	## attach pod
	kubectl exec -it $(POD) bash

ping1:	## curl service ip from node
	$(NODE_EXEC) curl -s http://$(SVC_IP):6000

# see: file in pod: /etc/resolv.conf
ping2: 		## curl service dns name from pod
	$(POD_EXEC) cat /etc/resolv.conf
	@echo
	$(POD_EXEC) curl -s http://$(SVC_DNS):6000

ping3: 		## service nodeport
	$(NODE_EXEC) curl -s http://127.0.0.1:30006
