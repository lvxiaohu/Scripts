#!/usr/bin/env python
# -*- coding:utf-8 -*-

# from fabric.api import *
# from fabric1.api import *
from fabric.api import env
from fabric.api import cd
from fabric.api import lcd
from fabric.api import task
from fabric.api import run
from fabric.api import roles
from fabric.api import put
from fabric.api import local
from fabric.api import execute


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
env.user = 'root'
env.password = '1k36n1ih'
env.roledefs = {'main': ['root@103.235.232.85'],
                'workers': ['103.235.232.90', '103.235.232.94', '103.235.232.98', '103.235.232.99', '103.235.232.111'],
                'dbserver': ['103.235.232.114']}

CMD_SYSTEM_DEPANDENCE = 'apt-get install -y libxml2-dev libxslt1-dev zlib1g-dev python-pip python-pkg-resources fabric'
CMD_PYTHON_DEPANDENCE = 'pip install -r requirement.txt'
CMD_ZIP='tar -cvf temp.tar conf pushlisher tasks worker bootup.sh requirement.txt start_publish.sh stkpublisher.py'
CMD_UNZIP='tar -xvf temp.tar'
CMD_BOOTUP='nohup celery -A tasks.stktask worker -E -l info --concurrency=1 &> /dev/null &'
CMD_KILL_CELERY='pkill -f "celery"'
PATH_WORKSPACE='~/workspace'
PATH_PROJECT=PATH_WORKSPACE+'/celery_queque_basic'


# # /root/workspace/celery_queque_basic
# @task
# # @roles('main', 'workers', 'dbserver')
# @roles('main','workers','dbserver')
def dep():
    run(CMD_SYSTEM_DEPANDENCE)
    with cd(PATH_PROJECT):
        run(CMD_PYTHON_DEPANDENCE)

# @task
# # @roles('main', 'workers', 'dbserver')
# @roles('main','workers','dbserver')
def pack():
    with lcd(PATH_PROJECT):
        local(CMD_ZIP)
    
# @task
# # @roles('main', 'workers', 'dbserver')
# @roles('main','workers','dbserver')
def stop_process():
    run(CMD_KILL_CELERY,warn_only=True)


# @task
# # @roles('main', 'workers', 'dbserver')
# @roles('main','workers','dbserver')
def upload_clean():
    with cd('~'):
        if int(run(" [ -e './workspace' ] && echo 11 || echo 10")) == 10:
            run('mkdir ./workspace')
        with cd('./workspace'):
            if int(run(" [ -e './celery_queque_basic' ] && echo 11 || echo 10")) == 11:
                run('rm -rf ./celery_queque_basic')
                run('mkdir ./celery_queque_basic')
            else:
                run('mkdir ./celery_queque_basic')
            with cd('./celery_queque_basic'):
                with lcd(PATH_PROJECT):
                    put(PATH_PROJECT+'/temp.tar',PATH_PROJECT+'/')
                    run(CMD_UNZIP)
                    run('chmod +x ./bootup.sh')
                    run('rm -rf temp.tar')
                    local('rm -rf temp.tar')


# @task
# # @roles('main', 'workers', 'dbserver')
# @roles('main','workers','dbserver')
def bootup():
    with cd(PATH_PROJECT):
        run('./bootup.sh', pty=False)

@task
# @roles('main', 'workers', 'dbserver')
@roles('main','workers','dbserver')
def beta_go():
    pack()
    stop_process()
    upload_clean()
    dep()
    bootup()

execute(beta_go)
