#!/bin/bash

# exec /usr/sbin/init 

# nohup /usr/sbin/init >> /dev/null 2>&1 &
nohup /usr/sbin/init > /var/log/systemd-init.log 2>&1 &

/bin/zsh
