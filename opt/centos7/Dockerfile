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
ENV CACHE_DIR_YUM=/wine/cache/yum
ENV CACHE_DIR_GO=/wine/cache/go

############################################################
# install base softwares
############################################################

# repo
ADD repo/centos-base-ali.repo /etc/yum.repos.d/CentOS-Base.repo
ADD repo/centos-epel-ali.repo /etc/yum.repos.d/epel.repo

# 基础工具下载
RUN --mount=type=cache,target=${CACHE_DIR_YUM} \
    yum install -y curl wget tar bzip2 unzip vim passwd sudo tree rsync man git tig tmux \
    # 编译
    gcc gcc-c++ make yum-utils automake cmake autoconf rpm-build redhat-rpm-config \
    # 网络
    iptables ipset iproute hostname net-tools telnet nc tcpdump route bridge-utils traceroute \
    # 性能
    htop psmisc vmstat iostat pidstat sysstat strace lsof \
    # 语言、组件
    python-pip mysql-client redis openssh-server openssh-client \
    # 依赖
    zlib libffi libtool python-devel libpng-devel libjpeg-devel openssl-devel mysql-devel \
    zlib-devel libffi-devel bzip2-devel sqlite-devel readline-devel tk-devel \
    perl-ExtUtils-MakeMaker ncurses-devel curl-devel expat-devel gettext-devel \
    kernel-devel kernel-debug-devel \
    # dind
    supervisor NetworkManager python-setuptools iptables-services mysql 
    # --nogpgcheck
    # && groupinstall "Development Tools" \
    # && yum clean all

# openvswitch
# see: https://gist.github.com/umardx/a31bf6a13600a55c0d07d4ca33133834
RUN --mount=type=cache,target=${CACHE_DIR_YUM} \
    yum install -y openssl11-libs libibverbs unbound unbound-devel graphviz \
    kernel-debug-devel libtool python-twisted-core \
    python-zope-interface PyQt4 desktop-file-utils libcap-ng-devel groff \
    checkpolicy selinux-policy-devel python3-devel sphinx-build-3 python3-sphinx 
    # && yum clean all

############################################################
# openssl
############################################################

COPY pkg/openssl-1.1.1w.tar.gz /tmp/
RUN cd /tmp/ \
    && tar -xzf openssl-1.1.1w.tar.gz \
    && cd openssl-1.1.1w  \
    && ./config --prefix=/usr \
    && make \
    && make install_sw install_ssldirs \
    && rm -rf /tmp/openssl-*

############################################################
# zsh
############################################################

# 安装zsh，默认安装在：/usr/local/bin/zsh
# 参考：https://blog.csdn.net/u012605514/article/details/121797773
COPY zsh/zsh-5.8.tar.xz /tmp/
RUN cd /tmp \
    && tar -xf zsh-5.8.tar.xz \
    && cd zsh-5.8 \
    && ./configure --without-tcsetpgrp \
    && make \
    && make install \
    && rm -rf /tmp/zsh-* 
RUN ln -s $(which zsh) /bin/zsh \
    && echo "/bin/zsh" >> /etc/shells

# 安装 oh my zsh 
COPY zsh/ohmyzsh-master.zip /tmp/
RUN cd /tmp \
    && unzip -q ohmyzsh-master.zip \
    && mv ohmyzsh-master ${HOME_DIR}/.oh-my-zsh \
    && cp ${HOME_DIR}/.oh-my-zsh/templates/zshrc.zsh-template ${HOME_DIR}/.zshrc \
    && rm -rf /tmp/ohmyzsh-*

############################################################
# python3
############################################################
COPY pkg/Python-3.12.0.tgz /tmp/
RUN cd /tmp/ \
    && tar -xzf Python-3.12.0.tgz \
    && cd Python-3.12.0 \
    && ./configure --prefix=/usr/local/python3.12 --with-ssl \
    && make \
    && make install \
    && rm -rf /tmp/Python-*
RUN ln -s /usr/local/python3.12/bin/python3.12 /usr/bin/python3.12 \
    && ln -s /usr/local/python3.12/bin/pip3.12 /usr/bin/pip3.12

############################################################
# golang
############################################################
RUN cd /tmp \
    && wget https://golang.google.cn/dl/go1.22.3.linux-amd64.tar.gz \
    && tar -zxf go1.22.3.linux-amd64.tar.gz -C /usr/local \
    && rm -rf /tmp/go*
ENV PATH="$PATH:/usr/local/go/bin"
# install golang dlv gopls staticcheck
# RUN go env -w GOPROXY=https://mirrors.aliyun.com/goproxy/ \
RUN go env -w GOPROXY=https://goproxy.cn,direct \
    && go env -w GO111MODULE=on \
    && go env -w GOSUMDB='off'
RUN --mount=type=cache,target=${CACHE_DIR_GO} \
    go install golang.org/x/tools/gopls@v0.15.3 \
    && go install github.com/go-delve/delve/cmd/dlv@v1.22.1 \
    && go install honnef.co/go/tools/cmd/staticcheck@v0.4.7 

############################################################
# docker
############################################################

# install docker for dind
# https://download.docker.com/linux/static/stable/x86_64/docker-19.03.0.tgz
COPY docker/docker-19.03.0.tgz /tmp/docker/
RUN set -eux; \
    cd /tmp/docker/ \
    && tar -xzf docker-19.03.0.tgz --strip-components 1 -C /usr/local/bin \
    && rm -rf /tmp/docker

# install docker compose
# https://github.com/docker/compose/releases/download/v2.22.0/docker-compose-linux-x86_64
COPY docker/docker-compose-Linux-x86_64 /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose 

############################################################
# openvswitch
############################################################
# see: https://blog.csdn.net/weixin_42072280/article/details/119764004
# RUN --mount=type=cache,target=${CACHE_DIR_YUM} \
#     yum install -y epel-release \
#     && yum install -y centos-release-openstack-train \
#     && yum install -y openvswitch libibverbs \
#     && yum clean all 
#
# see: https://gist.github.com/umardx/a31bf6a13600a55c0d07d4ca33133834
COPY pkg/openvswitch-2.13.0.tar.gz ${HOME_DIR}/rpmbuild/SOURCES/
RUN set -eux; \
    cd ${HOME_DIR}/rpmbuild/SOURCES \
    && tar -xzf openvswitch-*.tar.gz \
    && rpmbuild -bb --nocheck openvswitch-2.13.0/rhel/openvswitch-fedora.spec \
    && yum localinstall -y ${HOME_DIR}/rpmbuild/RPMS/x86_64/openvswitch-2.13.0-*.rpm  

############################################################
# git
############################################################
COPY pkg/git-2.30.0.tar.gz /tmp/
RUN set -eux; \
    rm /usr/bin/git \
    && cd /tmp \
    && tar -zxf git-2.30.0.tar.gz \
    && cd git-2.30.0 \
    && make configure \
    && ./configure --prefix=/usr \
    && make all \
    && make install \
    && rm -rf /tmp/git-*

############################################################
# install others
############################################################

RUN --mount=type=cache,target=${CACHE_DIR_YUM} \
    yum install -y --disablerepo="*" --enablerepo="base,extras" \
    etcd ethtool 
    # && yum clean all

############################################################
# vscode
############################################################

# 安装vscode
# 对应以下版本：
#   版本: 1.85.2 (system setup)
#   提交: 8b3775030ed1a69b13e4f4c628c612102e30a681
#   日期: 2024-01-18T06:40:10.514Z
ENV VSCODE_ID=8b3775030ed1a69b13e4f4c628c612102e30a681
ENV VSCODE_BIN_DIR=${HOME_DIR}/.vscode-server/bin/${VSCODE_ID}
COPY vscode/vscode-server-linux-x64-1.85.2.tar.gz /tmp/
RUN mkdir -p ${VSCODE_BIN_DIR} \
    && tar -xzf /tmp/vscode-server-linux-x64-1.85.2.tar.gz -C ${VSCODE_BIN_DIR} --strip 1 \
    && rm /tmp/vscode-*
# 安装 vscode extensions
# ~/.vscode-server/bin/8b3775030ed1a69b13e4f4c628c612102e30a681/bin/code-server 
COPY vscode/ext/* /tmp/vscode/ext/
ENV VSCODE_BIN=${VSCODE_BIN_DIR}/bin/code-server
RUN cd /tmp/vscode/ext/ \
    # 传入 code-server 执行文件的路径，在脚本里遍历安装扩展文件
    && ./install.sh ${VSCODE_BIN}

############################################################
# others
############################################################

ENV PATH="$PATH:/usr/local/python3.12/bin"

# install supervisor
COPY supervisor/* /etc/supervisord.d/

# install systemctl 
# https://github.com/gdraheim/docker-systemctl-replacement/
# https://github.com/gdraheim/docker-systemctl-images/
COPY sys/systemctl.py /tmp
RUN mv /usr/bin/systemctl /usr/bin/systemctl.bak \
    && cp /tmp/systemctl.py /usr/bin/systemctl \
    && chmod a+x /usr/bin/systemctl 

############################################################
# configs
############################################################
ENV WINE_OPT_DIR=/wine/devbox/opt

# zsh config
# 自动补全
ENV ZSH_CUSTOM=${HOME_DIR}/.oh-my-zsh/custom
COPY zsh/incr-0.2.zsh ${ZSH_CUSTOM}/plugins/incr/incr.zsh
# zshr配置
RUN echo >> ${HOME_DIR}/.zshrc \
    && echo "source ${WINE_OPT_DIR}/rc/ext.zsh" >> ${HOME_DIR}/.zshrc \
    && sed -i "s/robbyrussell/ys/" ${HOME_DIR}/.zshrc 
# 切换shell
RUN chsh -s $(which zsh) 

# git config
COPY conf/.gitconfig /${HOME_DIR}/.gitconfig
# pip config
COPY conf/pip.conf ${HOME_DIR}/.pip/pip.conf
# tmux
COPY conf/tmux.conf ${HOME_DIR}/.tmux.conf
# docker proxy
COPY docker/daemon.json /etc/docker/
# COPY docker/docker.service.lib /usr/lib/systemd/system/docker.service
# /usr/lib/systemd/system/docker.service

# 配置ssh 
# RUN sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/g' /etc/ssh/sshd_config
# RUN sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/g' /etc/ssh/sshd_config
# Docker服务器开放的端口，供容器外部连接使用(在启动容器时做端口映射)
# EXPOSE 22   

WORKDIR ${WINE_OPT_DIR}/devc

CMD ["/bin/zsh"]
