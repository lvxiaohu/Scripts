#!/bin/bash

ip_use=/var/www/html/172.16.10.0_ip_use.html
ip_all=/var/www/html/172.16.10.0_ip_all.html
ip_none=/var/www/html/172.16.10.0_ip_none.html
ip_all_num=`cat ${ip_all}|wc -l`

echo -e "\033[32m 正常检测中，请稍后... ... \033[0m"


function checkall_ip {
    if [ ${ip_all_num} -eq 0 ]; then
        for i in $(seq 1 254)
          do
          `echo 172.16.10.${i} >> ${ip_all}`
          done
    fi
    }

function scanning_ip {
    scan_use_ip=`nmap -p 22,21,80,443 172.16.10.1-253 |grep 172|awk '{print $5}'`
    for a_ip in ${scan_use_ip}
    do
    echo -e "${a_ip}" >> ${ip_use}
    done
}

function install_nmap {
    which nmap > /dev/null
    if [ $? -ne 0 ];then
       yum install nmap -y
    fi
}


function none_ip {
   none_ip_status=`sort ${ip_all} ${ip_use}| uniq -u`
#   read -p "是否查看所有未被占用的IP: (y/n)" look_chose
   look_chose=y
   if [ ${look_chose} == 'y' ] || [ ${look_chose} == 'Y' ];then
       for i in ${none_ip_status}
       do
       echo -e $i
       echo -e $i >> ${ip_none}
       done
   fi
}
function ip_use_status {
    echo -e "--------以下IP已经被占用--------"
    sort ${ip_all} ${ip_use}|uniq -d
    echo -e "--------以上IP已经被占用--------"
    echo -e "IP总数量为：( \033[32m ${ip_all_num} \033[0m )个"
    echo -e "已用IP数量为：(\033[32m `sort ${ip_all} ${ip_use}|uniq -d|wc -l` \033[0m) 个"

}

function write_to_html {
    sed -i 's/^/<p> &/g' ${ip_use}
    sed -i 's/$/<\/p> &/g' ${ip_use}
    sed -i '1 i\<p>已被使用的IP列表<\/p>' ${ip_use}
    sed -i 's/^/<p> &/g' ${ip_none}
    sed -i 's/$/<\/p> &/g' ${ip_none}
    sed -i '1 i\<p>空闲IP列表<\/p>' ${ip_none}

}


function main {
    rm -rf $ip_use
    rm -rf $ip_none
    touch $ip_use
    install_nmap
    checkall_ip
    scanning_ip
    ip_use_status
    none_ip
    write_to_html
    }

main

