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

############################################################
# install base softwares
############################################################

# repo
ADD repo/centos-base-ali.repo /etc/yum.repos.d/CentOS-Base.repo
ADD repo/centos-epel-ali.repo /etc/yum.repos.d/epel.repo

# 基础工具下载
RUN yum install -y \
    curl wget tar bzip2 unzip vim passwd sudo tree rsync man git tig tmux \
    gcc gcc-c++ make yum-utils automake cmake autoconf \
    iptables ipset iproute hostname net-tools telnet nc tcpdump route bridge-utils \
    traceroute htop psmisc vmstat iostat pidstat sysstat strace lsof \
    python-pip mysql mysql-client redis openssh-server openssh-client etcd ethtool \
    python-devel openssl-devel mysql-devel zlib-devel \
    && yum clean all

# git config
COPY conf/.gitconfig /${HOME_DIR}/.gitconfig
# pip config
COPY conf/pip.conf ${HOME_DIR}/.pip/pip.conf
# tmux
COPY conf/tmux.conf ${HOME_DIR}/.tmux.conf

CMD ["/bin/bash"]
