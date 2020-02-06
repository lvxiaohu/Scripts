#!/bin/bash

#提示：使用本脚本请修改：第20行

# redis连接信息
max_used=0.8 #最大使用率，0.8代表 80%，超过80%触发切换
redis_password=jfjuU4O4xMLX
redis_host=127.0.0.1

# 内存使用情况
redis_cmd="docker exec -it jms_redis redis-cli -h $redis_host -a $redis_password info"
maxmemory_human=`docker exec -it jms_redis redis-cli -h $redis_host -a $redis_password info memory|grep "maxmemory_human"|awk -F: '{print $2}'`
used_memory=`docker exec -it jms_redis redis-cli -h $redis_host -a $redis_password  info memory|grep "used_memory_human"|awk -F: '{print $2}'`

# 连接数
max_connected_clients=4000    # 根据实际情况设置一个最大连接数，可去redis.conf查看设置maxclients 参数
connected_clients=`docker exec -it jms_redis redis-cli -h $redis_host -a $redis_password  info Clients|grep -i "connected_clients"|awk -F: '{print $2}'`

logs_file=/tmp/redis_check.log
run_time=`date +%Y-%m-%d-%H:%M:%S`

function change_service() {
    # system stop keepalived
    echo "提示：system stop keepalived"
}

function check_mem() {
    new_maxmemory_human=`echo $maxmemory_human|awk -FG '{print $1}' `
    std_maxmemory_human=`awk 'BEGIN{print "'$new_maxmemory_human'" * "'1000'"}'`
    if [ `echo $used_memory|grep -i 'G'` ];then
    new_used_memory=`echo $used_memory|awk -FG '{print $1}' `
    std_used_memory=`awk 'BEGIN{print "'$new_used_memory'" * "'1000'"}'`
    echo $used_memory
    echo $std_used_memory
    echo $std_maxmemory_human
    if [ `awk 'BEGIN{print "'$std_used_memory'"}'` -gt `awk 'BEGIN{print "'$std_maxmemory_human'" * "'$max_used'"}'` ] ;then
        echo "$run_time: 内存跑满，触发切换" >> $logs_file
        change_service
        else
        echo "内存正常"
    fi
    else 
    std_used_memory=`echo $used_memory|awk -FM '{print $1}'`

    if [ `awk 'BEGIN{print "'$std_used_memory'" * "'100'"}'` -gt `awk 'BEGIN{print "'$std_maxmemory_human'" * "'$max_used'" * "'100'"}'` ] ;then
        echo "$run_time: 内存跑满，触发切换" >> $logs_file
        change_service
        else
        echo "内存正常"
    fi
    fi
}

function check_connected() {
    # echo $max_connected_clients
    std_connected=`awk 'BEGIN{print "'$max_connected_clients'" * "'$max_used'"}'`
    # echo $std_connected
    # echo $connected_clients
    if [ `awk 'BEGIN{print "'$connected_clients'" * "'1'"}'` -gt `awk 'BEGIN{print "'$std_connected'" * "'1'"}'` ];then
    echo "$run_time: 连接数超过最大限制，触发切换" >> $logs_file
    change_service
    else
    echo "连接数正常"
    fi
}
function main() {
    $redis_cmd > /dev/null
    if [ $? = 0 ];then
    check_connected
    check_mem
    else
    echo "$run_time: redis异常，触发切换" >> $logs_file
    change_service
    exit 0
    fi
    }

main