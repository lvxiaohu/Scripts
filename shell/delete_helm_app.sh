#!/bin/bash
# 执行脚步将会删除仓库所有应用
echo -e "------- \033[32m start \033[0m -------"
read -p "用执行  #helm repo update 吗？y/n: " yn
if [ $yn = y ] || [ $yn = Y ];then
echo -e "------- \033[32m 同步 helm 仓库 \033[0m -------"
helm repo update
else
echo "跳过helm 仓库同步"
fi

echo -e "------- \033[32m 获取 helm 数据 \033[0m -------"
helm_repo=`helm repo list|awk '{print $2}'|grep -v URL`
helm_app=`curl  -X GET  http://chartmuseum.kubeapps.fit2cloud.com/api/charts|jq -r "to_entries|map(\"\(.key)=\(.value|tostring)\")|.[]"|awk -F= '{print $1}' 2>&1`

echo -e "------- \033[32m 开始删除 chart \033[0m -------"

if [ -z ${helm_app} ];then
echo " helm 仓库是空的! 没有可以删除项目"
else
for i in $helm_app
do
 a=(`helm search $i|grep -v NAME|awk '{print $2}'|grep -v Repo`)
 echo "--->${a}"
 echo "开始删除 $i  ===> http://chartmuseum.kubeapps.fit2cloud.com/api/charts/$i/$a"
 curl -v -X DELETE "http://chartmuseum.kubeapps.fit2cloud.com/api/charts/$i/$a" 2&> /dev/null
 if [ $? -eq 0 ];then
  echo -e "\033[32m 删除 $i 成功 \033[0m "
 else
  echo -e "\033[31m 删除 $i 失败 \033[0m "
 fi
done
fi
