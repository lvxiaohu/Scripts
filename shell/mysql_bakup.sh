#!/bin/bash
#mysql 备份脚本
#保留最近10天备份
#备份目录
backupDir=/jumpserver-data/jumpserver/mysql-bak
#mysqlDump
mysqldump="docker run --rm -i --network=jms_default registry.fit2cloud.com/public/mysql:5 mysqldump"
#mysqldump=/usr/bin/mysqldump
#ip
host=127.0.0.1
#用户名
username=root
password=ICAgIGluZXQgMTkyLjE2OC4xLj


#今天日期
today=`date +%Y%m%d`
#十天前的日期
timeTenDayAgo=`date -d -10day +%Y%m%d`
#要备份的数据库数组
databases=(jumpserver)


# echo $databaseCount

for database in ${databases[@]}
  do
    echo '开始备份'$database
    $mysqldump -h$host -u$username -p$password $database | gzip > $backupDir/$database-$today.sql.gz
    echo '成功备份'$database'到'$backupDir/$database-$today.sql.gz
    if [ ! -f "$backupDir/$database-$timeTenDayAgo.sql.gz" ]; then
      echo '10天前备份不存在，无需删除'
    else
        rm -f $backupDir/$database-$timeTenDayAgo.sql.gz
        echo '删除10天前备份文件'$backupDir/$database-$timeTenDayAgo.sql.gz
    fi
  done

