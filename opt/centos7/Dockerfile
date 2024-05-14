FROM centos:7.9.2009

# 时区
ENV TZ "Asia/Shanghai"
# 禁用交互式提示
ENV DEBIAN_FRONTEND noninteractive
# 设置编码，解决zsh下中文乱码问题
ENV LC_ALL=en_US.UTF-8  
ENV LANG=en_US.UTF-8
# terminal colors with xterm
ENV TERM xterm
# home dir
ENV HOME_DIR /root

# repo
ADD repo/centos-base-ali.repo /etc/yum.repos.d/CentOS-Base.repo
ADD repo/centos-epel-ali.repo /etc/yum.repos.d/epel.repo

# 常用命令下载
RUN yum install -y curl wget tar bzip2 unzip gcc gcc-c++ git make yum-utils htop man
RUN yum install -y vim vim-enhanced passwd sudo hostname net-tools rsync \
    automake cmake patch logrotate python-devel libpng-devel \
    libjpeg-devel pwgen mysql-client redis
RUN yum install -y iptables ipset iproute tree
RUN yum install -y perl-ExtUtils-MakeMaker ncurses-devel

# zsh
# 安装zsh，默认安装在：/usr/local/bin/zsh
# 参考：https://blog.csdn.net/u012605514/article/details/121797773
COPY zsh/zsh-5.8.tar.xz /tmp/
RUN cd /tmp \
    && tar xvf zsh-5.8.tar.xz \
    && cd zsh-5.8 \
    && ./configure --without-tcsetpgrp \
    && make \
    && make install \
    && rm -rf /tmp/zsh-* \
    && echo "/usr/local/bin/zsh" >> /etc/shells

# 安装 oh my zsh 
COPY zsh/ohmyzsh-master.zip /tmp/
RUN cd /tmp \
    && unzip ohmyzsh-master.zip \
    && rm -rf ohmyzsh-master.zip \
    && mv ohmyzsh-master ${HOME_DIR}/.oh-my-zsh \
    && cp ${HOME_DIR}/.oh-my-zsh/templates/zshrc.zsh-template ${HOME_DIR}/.zshrc \
    && ln -s $(which zsh) /bin/zsh \
    && chsh -s $(which zsh) 

# 安装 golang 
RUN cd /tmp \
    && wget https://golang.google.cn/dl/go1.22.3.linux-amd64.tar.gz \
    && tar -zxf go1.22.3.linux-amd64.tar.gz -C /usr/local \
    && rm -rf ./go*
ENV PATH="$PATH:/usr/local/go/bin"

# 安装最新git

# 安装vscode
# 对应以下版本：
#   版本: 1.85.2 (system setup)
#   提交: 8b3775030ed1a69b13e4f4c628c612102e30a681
#   日期: 2024-01-18T06:40:10.514Z
ENV VSCODE_ID=8b3775030ed1a69b13e4f4c628c612102e30a681
ENV VSCODE_BIN_DIR=${HOME_DIR}/.vscode-server/bin/${VSCODE_ID}
COPY vscode/vscode-server-linux-x64-1.85.2.tar.gz /tmp/
RUN mkdir -p ${VSCODE_BIN_DIR} \
    && tar -zxf /tmp/vscode-server-linux-x64-1.85.2.tar.gz -C ${VSCODE_BIN_DIR} --strip 1 \
    && rm /tmp/vscode-*

# 安装 vscode extensions


##############################
# zsh config
##############################

# 自动补全
ENV ZSH_CUSTOM=${HOME_DIR}/.oh-my-zsh/custom
RUN mkdir -p ${ZSH_CUSTOM}/plugins/incr
COPY zsh/incr-0.2.zsh ${ZSH_CUSTOM}/plugins/incr/incr.zsh
# 其他配置
COPY zsh/ext.zsh /tmp/ 
RUN cat /tmp/ext.zsh >> ${HOME_DIR}/.zshrc
# 设置主题
RUN sed -i "s/robbyrussell/ys/" ${HOME_DIR}/.zshrc 


##############################
# golang config
##############################

# RUN go env -w GOPROXY=https://goproxy.cn,direct \
#     && go env -w GO111MODULE=on \
#     && go env -w GOSUMDB='off'


# gitconfig
COPY .gitconfig /root/.gitconfig


# 其他工具
# RUN yum install -y tree

# python pip
# RUN yum install -y python-pip 

# 配置ssh 
# RUN yum install -y openssh-server
# RUN sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/g' /etc/ssh/sshd_config
# RUN sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/g' /etc/ssh/sshd_config

# Docker服务器开放的端口，供容器外部连接使用(在启动容器时做端口映射)
# EXPOSE 22   

WORKDIR /wine

CMD ["/bin/zsh"]


