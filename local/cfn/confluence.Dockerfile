
FROM cptactionhank/atlassian-confluence:7.9.3

USER root

# 将代理破解包加入容器
COPY "atlassian-agent.jar" /opt/atlassian/confluence/

COPY "atlassian-agent.jar" "agented.sh" /opt/atlassian/confluence/agented/

# 设置启动加载代理包
RUN echo 'export CATALINA_OPTS="-javaagent:/opt/atlassian/confluence/atlassian-agent.jar ${CATALINA_OPTS}"' >> /opt/atlassian/confluence/bin/setenv.sh



