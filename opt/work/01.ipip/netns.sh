#!/bin/bash

NS1="ns1"
Veth1="veth1"
Veth_Peer1="peer1"
Veth1_Addr="10.10.1.2/24"
Veth1_Ip="10.10.1.2"
Veth_Peer1_Addr="10.10.1.1/24"
NS1_Subnet="10.10.1.0/24"
NS1_Gw="10.10.1.1"
NS1_Inner_Ip="192.168.1.10"
NS1_Tun1="tun1"

NS2="ns2"
Veth2="veth2"
Veth_Peer2="peer2"
Veth2_Addr="10.10.2.2/24"
Veth2_Ip="10.10.2.2"
Veth_Peer2_Addr="10.10.2.1/24"
NS2_Subnet="10.10.2.0/24"
NS2_Gw="10.10.2.1"
NS2_Inner_Ip="192.168.2.10"
NS2_Tun2="tun2"

echo

function ns_setup() {
    # 1、创建两个网络命名空间
    ip netns add ${NS1}
    ip netns add ${NS2}

    # 2、创建两对 veth pair ，一端各挂在一个命名空间下
    ip link add ${Veth1} type veth peer name ${Veth_Peer1}
    ip link add ${Veth2} type veth peer name ${Veth_Peer2}

    ip link set ${Veth1} netns ${NS1}
    ip link set ${Veth2} netns ${NS2}

    # 3、分别配置地址，并启用
    ip addr add ${Veth_Peer1_Addr} dev ${Veth_Peer1}
    ip link set ${Veth_Peer1} up
    ip addr add ${Veth_Peer2_Addr} dev ${Veth_Peer2}
    ip link set ${Veth_Peer2} up

    ip netns exec ${NS1} ip addr add ${Veth1_Addr} dev ${Veth1}
    ip netns exec ${NS1} ip link set ${Veth1} up
    ip netns exec ${NS2} ip addr add ${Veth2_Addr} dev ${Veth2}
    ip netns exec ${NS2} ip link set ${Veth2} up

    # 4、分别配置路由
    ip netns exec ${NS1} route add -net ${NS2_Subnet} gw ${NS1_Gw}
    ip netns exec ${NS2} route add -net ${NS1_Subnet} gw ${NS2_Gw}

    # 此时执行ping是通的
    # ip netns exec ${NS1} ping ${Veth2_Ip} -W1 -c1

    # 5、创建 tun设备，并设置为ipip隧道
    ip netns exec ${NS1} ip tunnel add ${NS1_Tun1} mode ipip remote ${Veth2_Ip} local ${Veth1_Ip}
    ip netns exec ${NS1} ip link set ${NS1_Tun1} up
    ip netns exec ${NS1} ip addr add ${NS1_Inner_Ip} peer ${NS2_Inner_Ip} dev ${NS1_Tun1}

    ip netns exec ${NS2} ip tunnel add ${NS2_Tun2} mode ipip remote ${Veth1_Ip} local ${Veth2_Ip}
    ip netns exec ${NS2} ip link set ${NS2_Tun2} up
    ip netns exec ${NS2} ip addr add ${NS2_Inner_Ip} peer ${NS1_Inner_Ip} dev ${NS2_Tun2}
}

function ping1() {
    # 测试隧道是否通
    ip netns exec ${NS1} ping ${NS2_Inner_Ip} -W1 -c1
}

function ping2() {
    # 测试隧道是否通
    ip netns exec ${NS2} ping ${NS1_Inner_Ip} -W1 -c1
}

function ns_clear() {
    ip netns del ${NS1}
    ip netns del ${NS2}
}

function _ns_info() {
    ip netns exec $1 ip addr
	echo
	ip netns exec $1 route -n
	echo
	ip netns exec $1 netstat -nat
}

function ns1() {
    _ns_info ${NS1}
}

function ns2() {
    _ns_info ${NS2}
}
