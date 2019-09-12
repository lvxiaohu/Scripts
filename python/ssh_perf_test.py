#!/usr/bin/python
# coding: utf-8

import pexpect
import sys
import threading
import time
import random

HOST = "192.168.1.1"
PORT = 2222
USER = "admin"
PASSWORD = "admin"
HOST_NUM = 4
DEBUG = True
#DEBUG = False
# 并发会话数
TOTAL = 100

PS1 = "lxh"
RUN_COMMAND = ["tail /var/log/dmesg", "echo hello world"]
stop_event = threading.Event()


def connect(i=1):
    cmd = "ssh %s@%s -p%s" % (USER, HOST, PORT)
    print(u"开始连接 [%s]: %s" % (i, cmd))
    child = pexpect.spawn(cmd)

    if DEBUG:
        child.logfile = sys.stdout

    while not stop_event.is_set():
        index = child.expect([
            "password:", "Jumpserver", "主机名", PS1,
            pexpect.EOF, pexpect.TIMEOUT
        ])
        if index == 0:
            if DEBUG:
                print(u"开始输入密码：")
            child.sendline(PASSWORD)
            time.sleep(2)
        elif index == 1:
            if DEBUG:
                print(u"输入 p")
            child.sendline("p")
            time.sleep(1)
        elif index == 2:
            n = random.choice(range(2, HOST_NUM + 1))
            if DEBUG:
                print(u"选择一个登陆: %s" % (n))
            child.sendline(str(n))
        elif index == 3:
            if DEBUG:
                print(u"登陆成功，执行命令：%s" % RUN_COMMAND)
            child.sendline(RUN_COMMAND[0])
            time.sleep(1)
        time.sleep(1)


def run():
    for i in range(TOTAL):
        t = threading.Thread(target=connect, args=(i,))
        t.daemon = True
        t.start()
        time.sleep(0.1)
    done = input("Done ?")
    print("Done test")


if __name__ == '__main__':
    run()
