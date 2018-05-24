#!/usr/bin/env python
# -*- coding:utf-8 -*-

# --coding:utf-8 --

from fabric.api import *
from fabric.context_managers import *

# from fabric.contrib.console import confirm

# CMD_DOWENLOAD_REPO='ls'
CMD_DOWENLOAD_REPO = 'curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo'
CMD_INSTALL_HTTPD = 'yum install -y httpd'
CMD_Start_HTTPD = 'service  httpd start'
CMD_restart_HTTPD = 'service  httpd restart'
PATH_local_html = 'F:/公司备份/html_bin.ch.tar.gz'
PATH_Remote_html = '/var/www/html'

env.user = 'root'
# env.hosts=['103.235.232.60']  #定义单机
env.roledefs = {'web': ['103.235.232.60']}
# env.roledefs={'web':['103.235.232.60']}

env.password = 'BIH.cn123'



def system_repo():
    run(CMD_DOWENLOAD_REPO)
    run('yum clean all && yum makecache')


def upload_html():
    with settings(warn_only=True):
        run(CMD_INSTALL_HTTPD)
        # with lcd(E:\):
        put('E:\html_bin.ch.tar.gz',PATH_Remote_html)
        # put(PATH_local_html, PATH_Remote_html)
    # if result.failed and not confirm('Put file failed,Continue[y/n]?')：
    #     abort("Aborting file put task!")


def tar_task():
    with cd(PATH_Remote_html):
        run('tar -zxvf html_bin.ch.tar.gz')


def start_web():
    run(CMD_Start_HTTPD)


def check_web():
    print("Http deploy Successful！URL:http://103.235.232.60")



@task
@roles('web')
def main():
    # system_repo()
    # upload_html()
    # tar_task()
    # start_web()
    check_web()

execute(main)
