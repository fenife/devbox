#!/bin/bash

. ./common.sh
. ./netns.sh

# set -x
# echo "argv: $*"
# echo

tcp_cap_file=/tmp/peer1.pcap

function info() {
    conntrack -L  
}

function pd1() {
    tcpdump -i $Veth_Peer1 -nvv -U -w $tcp_cap_file &
    sleep 1
    ping1
    sleep 1
    _stop_program tcpdump
    sleep 1
    tcpdump -nvv -r $tcp_cap_file
}

if [[ -z "$1" ]] || [[ $1 == help ]]; then
    help
else
    set -x
    eval $* 
fi

