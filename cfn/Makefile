
.PHONY: mysql cfn push pull
.PHONY: up stop exec clean

mysql:
	docker build -f mysql.Dockerfile -t mysql:5.7.30-confluence .	


cfn:
	docker build -f confluence.Dockerfile -t confluence:7.9.3-agented .

tag:
	#docker tag cptactionhank/atlassian-confluence:7.9.3 fenife/atlassian-confluence:7.9.3
	docker tag mysql:5.7.30-confluence fenife/mysql:5.7.30-confluence
	docker tag confluence:7.9.3-agented fenife/confluence:7.9.3-agented
	docker tag confluence:7.9.3-agented fenife/cfn:7.9.3

push:
	docker push fenife/mysql:5.7.30-confluence
	docker push fenife/confluence:7.9.3-agented

push2:
	docker push fenife/cfn:7.9.3

pull:
	docker pull fenife/mysql:5.7.30-confluence
	docker pull fenife/confluence:7.9.3-agented

up:
	docker compose up 

stop:
	docker compose stop

exec:
	docker exec -it confluence /bin/bash 

clean:
	sudo rm -rf /var/lib/cfn/*

conn:
	mysql -h127.0.0.1 -P3308 -uroot -proot

at: exec

# create database confluence;

# agented
# docker exec -it confluence /bin/bash
# cd /opt/atlassian/confluence/agented/
# vi agented.sh
# sh ./agented.sh

# jdbc:mysql://192.168.0.121:3308/confluence?characterEncoding=utf8&useUnicode=true&useSSL=false
# jdbc:mysql://192.168.0.121:3308/confluence?characterEncoding=utf8&useUnicode=true&useSSL=false&serverTimezone=UTC
# jdbc:mysql://172.17.64.10/confdb?useUnicode=true&characterEncoding=utf8

appkey = com.mxgraph.confluence.plugins.diagramly


java -jar /opt/atlassian/confluence/agented/atlassian-agent.jar -m fenife@163.com -n note -p com.stiltsoft.confluence.plugin.tablefilter.tablefilter -o Stiltsoft Europe -s B3XB-9GL2-08E5-N4VG -d


java -jar /opt/atlassian/confluence/agented/atlassian-agent.jar -m fenife@163.com -n note -p com.mxgraph.confluence.plugins.diagramly -o http://192.168.0.121 -s B3XB-9GL2-08E5-N4VG -d

java -jar /opt/atlassian/confluence/agented/atlassian-agent.jar -m fenife@163.com -n note -p com.stiltsoft.confluence.plugin.tablefilter.tablefilter -o http://192.168.0.121 -s B3XB-9GL2-08E5-N4VG -d

java -jar /opt/atlassian/confluence/agented/atlassian-agent.jar -m fenife@163.com -n note -p cz.morosystems.atlassian.plugin.easymind -o http://192.168.0.121 -s B3XB-9GL2-08E5-N4VG -d

