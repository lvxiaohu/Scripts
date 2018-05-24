#!/usr/bin/env python
# -*- coding:utf-8 -*-

# --coding:utf-8 --


'''
env.hosts   #定义目标主机，可以用IP或主机名表示，以python的列表形式定义。如env.hosts=['192.168.1.21','192.168.1.22']
env.exclude_hosts   #排除指定主机，如env.exclude_hosts=['192.168.1.21']
env.user   #定义用户名，如env.user='root'
env.port   #定义端口，默认为22，如env.port='22'
env.password   #定义密码，如env.password='123456'
env.passwords  #定义多个密码，不同主机对应不同密码，如：env.passwords = {'root@192.168.1.21:22':'123456','root@192.168.1.22:22':'654321'}
env.gateway   #定义网关（中转、堡垒机）IP，如env.gateway='192.168.1.23
env.roledefs   #定义角色分组，比如web组合db组主机区分开来：env.roledefs = {'webserver':['192.168.1.21','192.168.1.22'],'dbserver':['192.168.1.25','192.168.1.26']}

env.deploy_release_dir   #自定义全局变量，格式：env. + '变量名称'，如env.age,env.sex等


env.roledefs = {'webserver':['192.168.1.21','192.168.1.22'],'dbserver':['192.168.1.25','192.168.1.26']}
#引用分组时使用python装饰器方式来进行,如：
@roles('webserver')
def webtask():
    run('/usr/local/nginx/sbin/nginx')

@roles('webserver','dbserver')
def publictask():
    run('uptime')


local    #执行本地命令，如local('uname -s')
lcd      #切换本地目录，如lcd('/home')
cd       #切换远程目录
run     #执行远程命令
sudo   #sudo方式执行远程命令，如sudo('/etc/init.d/httpd start')
put     #上次本地文件导远程主机，如put('/home/user.info','/data/user.info')
get     #从远程主机下载文件到本地，如：get('/data/user.info','/home/user.info')
prompt  #获得用户输入信息，如：prompt('please input user password:')
confirm  #获得提示信息确认，如：confirm('Test failed,Continue[Y/N]?')
reboot   #重启远程主机，如：reboot()

@task   #函数修饰符，标识的函数为fab可调用的，非标记对fab不可见，纯业务逻辑
@runs_once   #函数修饰符，标识的函数只会执行一次，不受多台主机影响
'''

from fabric.api import *
from fabric.context_managers import *

# from fabric.contrib.console import confirm


CMD_DOWENLOAD_REPO = 'sh -c "curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo"'
CMD_INSTALL_HTTPD = 'yum install httpd'
CMD_Start_HTTPD = 'system start httpd'
CMD_restart_HTTPD = 'system restart httpd'
PATH_local_html = 'F:\公司备份\html_bin.ch.tar.gz'
PATH_Remote_html = '/var/www/html'

env.user = 'root'
env.hosts=['103.235.232.60']  #定义单机
# env.roledefs = {'web': ['103.235.232.60']}
# env.roledefs={'web':['103.235.232.60']}

env.password = 'BIH.cn123'



def system_repo():
    run(CMD_DOWENLOAD_REPO)
    run('yum clean all && yum makecache')


def upload_html():
    with settings(warn_only=True):
        result = put(PATH_local_html, PATH_Remote_html)
    # if result.failed and not confirm('Put file failed,Continue[y/n]?')：
    #     abort("Aborting file put task!")


def tar_task():
    with cd(PATH_Remote_html):
        run('tar -zxvf html_bin.ch.tar.gz')


def start_web():
    run(CMD_Start_HTTPD)


def check_web():
    print("Http deploy successful！")



@task
# @roles('web')
def main():
    system_repo()
    upload_html()
    tar_task()
    start_web()

main()