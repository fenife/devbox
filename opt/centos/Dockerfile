FROM centos:7.9.2009

# 时区
ENV TZ "Asia/Shanghai"
# 禁用交互式提示
ENV DEBIAN_FRONTEND noninteractive
# 设置编码，解决shell下中文乱码问题
ENV LANG zh_CN.UTF-8
# terminal colors with xterm
# ENV TERM xterm

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
ENV HOME=/root
WORKDIR ${HOME}
ENV ZSH_DIR=${HOME}/.zsh
# 编译zsh，默认安装在：/usr/local/bin/zsh
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

# 配置zsh
# 参考：https://dev.to/hbenvenutti/using-zsh-without-omz-4gch
# WORKDIR ${HOME}
# ENV ZSH_DIR=${HOME}/.zsh
# COPY zsh ${ZSH_DIR}
# RUN touch ${ZSH_DIR}/.zsh_history \
#     && mv ${ZSH_DIR}/.zshrc ${HOME}/.zshrc \
#     && chsh -s $(which zsh)

# oh my zsh 
COPY zsh/ohmyzsh-master.zip /tmp/
RUN cd /tmp \
    && unzip ohmyzsh-master.zip \
    && rm -rf ohmyzsh-master.zip \
    && mv ohmyzsh-master ~/.oh-my-zsh \
    && cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc \
    && sed -i "s/robbyrussell/ys/" ~/.zshrc \
    && chsh -s $(which zsh)

RUN ln -s $(which zsh) /bin/zsh

# 配置ssh 
# RUN yum install -y openssh-server
# RUN sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/g' /etc/ssh/sshd_config
# RUN sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/g' /etc/ssh/sshd_config

# golang goproxy
# RUN cd /tmp \
#     && wget https://golang.google.cn/dl/go1.22.3.linux-amd64.tar.gz \
#     && tar -zxf go1.22.3.linux-amd64.tar.gz -C /usr/local \
#     && rm -rf ./go*
# ENV PATH="$PATH:/usr/local/go/bin"
# RUN go env -w GOPROXY=https://goproxy.cn,direct \
#     && go env -w GO111MODULE=on \
#     && go env -w GOSUMDB='off'

# gitconfig
# COPY .gitconfig /root/.gitconfig

# 其他工具
# RUN yum install -y iptables ipset iproute tree

# python pip
# RUN yum install -y python-pip 

# Docker服务器开放的端口，供容器外部连接使用(在启动容器时做端口映射)
# EXPOSE 22   

CMD ["zsh"]


