#!/usr/bin/env python
# -*- coding:utf-8 -*-

from fabric.api import *


env.user = 'root'
env.password = '1k36n1bm36@bih'
env.roledefs = {'main': ['103.235.232.85'],
                'workers': ['103.235.232.90', '103.235.232.94', '103.235.232.98', '103.235.232.99', '103.235.232.111'],
                'dbserver': ['103.235.232.114']}

CMD_SYSTEM_DEPANDENCE = 'apt-get install -y libxml2-dev libxslt1-dev zlib1g-dev'
CMD_PYTHON_DEPANDENCE = 'pip install -r requirement.txt'
CMD_ZIP='7z a -tzip temp.zip -R conf pushlisher tasks worker'
CMD_UNZIP='unzip temp.zip'
CMD_BOOTUP='nohup celery -A tasks.stktask worker -E -l info --concurrency=1 &'
CMD_KILL_CELERY='pkill -f "celery"'
PATH_WORKSPACE='E:\workspace'



# /root/workspace/celery_queque_basic
@task
# @roles('main', 'workers', 'dbserver')
@roles('main')
def dep():
    run(CMD_SYSTEM_DEPANDENCE)
    with cd('~/workspace/celery_queque_basic'):
        run(CMD_PYTHON_DEPANDENCE)

@task
# @roles('main', 'workers', 'dbserver')
@roles('main')
def pack():
    with lcd(PATH_WORKSPACE):
        local(CMD_ZIP)

@task
# @roles('main', 'workers', 'dbserver')
@roles('main')
def stop_process():
    run(CMD_KILL_CELERY)

@task
# @roles('main', 'workers', 'dbserver')
@roles('main')
def deploy():
    with cd('~'):
        if int(run(" [ -e './workspace' ] && echo 11 || echo 10")) == 10:
            run('mkdir ./workspace')
        with cd('./workspace'):
            if int(run(" [ -e './celery_queque_basic' ] && echo 11 || echo 10")) == 11:
                run('rm -rf ./celery_queque_basic/*')
                with cd('./celery_queque_basic'):
                    with lcd(PATH_WORKSPACE):
                        put('temp.zip','temp.zip')
                        run(CMD_UNZIP)
                        run('rm temp.zip')
                        local('rm temp.zip')


@task
# @roles('main', 'workers', 'dbserver')
@roles('main')
def bootup():
    with cd('~/workspace/celery_queque_basic'):
        run(CMD_BOOTUP, pty=False)


pack()
stop_process()
deploy()
bootup()
