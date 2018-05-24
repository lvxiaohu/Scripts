#coding:utf-8
import paramiko

hostname='103.235.232.60'
username='root'
password='PeK8]f-b,n['
paramiko.util.log_to_file('a')

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()


ssh.connect(hostname=hostname,username=username,password=password)
stdin,stdout,stderr=ssh.exec_command('free -m')
print(stdout.read())
ssh.close()