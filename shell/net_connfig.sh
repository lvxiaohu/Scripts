#!/usr/bin/env bash
#! /bin/bash

#获取真实网卡列表
NetworkDevice=`nmcli device show|grep GENERAL.DEVICE:|awk '{print $2}'|grep "^e"|head -5|awk '$0=""NR". "$0'`

#echo  -e """网卡信息:\n \033[32m ${NetworkDevice}\033[0m"""
function network_chose {
    echo -e "开始配置网络..."
    printf "%-5s|%-10s\n" 网卡ID 网卡名称
    echo -e "===============================\033[34m
${NetworkDevice} \033[0m
==============================="

    read -p  "选择你需要配置网卡(输入网卡ID 例：1 ):"  NetworkNum
    if echo $NetworkNum | grep -q '[^0-9]'
        then
            echo -e "\033[32m 不是有效的网卡ID，请重新输入... \033[0m"
            network_chose
        else
            chose_net_device=`echo $NetworkDevice|head -$NetworkNum|awk '{print $2}'`
    fi
}

function check_ip {
    VALID_CHECK=$(echo $IP|awk -F. '$1<=255&&$2<=255&&$3<=255&&$4<=255{print "yes"}')
    if echo $IP|grep -E "^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$">/dev/null; then
        if [ ${VALID_CHECK:-no} == "yes" ]; then
            continue
        else
            echo -e "\033[31m IP $IP 输入错误，请重新输入 \033[0m"
            network_set
        fi
    else
        echo "IP format error!"
    fi
}

function network_set {
    read -p "请输入请你的IPV4地址："          ipaddr
    read -p "请输入请你的子网掩码/NETMASK[例:255.255.255.0]："  ip_netmask
    read -p "请输入请你的网关地址："  ip_gw
    read -p "请输入请你的DNS地址："  ip_dns
    for IP in $ipaddr $ip_netmask $ip_gw $ip_dns;do
        check_ip
        done
    echo "" > /etc/sysconfig/network-scripts/ifcfg-$chose_net_device
cat << EOF >>/etc/sysconfig/network-scripts/ifcfg-$chose_net_device
NAME=$chose_net_device
GATEWAY=$ip_gw
DNS1=$ip_dns
DEVICE=ens192
ONBOOT=yes
USERCTL=no
BOOTPROTO=static
NETMASK=$ip_netmask
IPADDR=$ipaddr
#PEERDNS=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
EOF
}

function restart_network () {
    read -p "网络配置已完成，是否重启网络(y/n):" yn
    if [ "$yn" == "Y" ] || [ "$yn" == "y" ]; then
            echo "将要重启网络..."
            systemctl restart network
        if [ $? -eq 0 ]
        then
            echo "启动成功"
            else
            echo "启动失败"
        fi
    elif [ "$yn" == "N" ] || [ "$yn" == "n"  ]; then
            echo "修改IP地址后需要重启网络服务使之生效，请手动重启服务...[systemctl restart network]"
    fi
}

function main {
    network_chose
    echo 配置的网卡文件为：$chose_net_device
    network_set
    restart_network
}

main
