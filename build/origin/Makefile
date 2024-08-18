
# IMAGE := b3log/siyuan:v3.0.17
# IMAGE := ubuntu:22.04
# IMAGE := ubuntu:20.04
# IMAGE := golang:1.22.5
# IMAGE := python:3.12.4
# IMAGE := golang:1.22.5-alpine3.20
# IMAGE := alpine:3.20
# IMAGE := kindest/node:v1.25.8
# IMAGE := registry:2.8
# IMAGE := kindest/node:v1.25.16
# IMAGE := kindest/node:v1.27.0
# IMAGE := ubuntu:24.04
IMAGE := ubuntu:24.10
pull:
	docker pull m.daocloud.io/docker.io/$(IMAGE)
	docker tag m.daocloud.io/docker.io/$(IMAGE) $(IMAGE)
	docker rmi m.daocloud.io/docker.io/$(IMAGE) 

