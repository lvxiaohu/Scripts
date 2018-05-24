#--coding:utf-8
import socket
print('Clinet Start')
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',2212))
