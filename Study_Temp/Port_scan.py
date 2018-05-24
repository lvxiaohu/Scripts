#conding:utf-8

import nmap
import sys

scan_row=[]
input_data = raw_input('Please input hosts and port :')
scan_row = input_data.split(" ")
if len(scan_row)!=2:
    print("Input errors,example \"192.168.1.0/24 80,443,8080,22\"")
    sys.exit()
hosts = scan_row[0]
port = scan_row[1]

try:
    nm = nmap.PortScanner()
except nmap.PortScannerError:
    print('Nmap not found' , sys.exc_info()[0])
    sys.exit(0)
except:
    print('Unexpected error:' , sys.exc_info()[0])
    sys.exit(0)

try:
    nm.scan(hosts=hosts , arguments=' - v -sS -p ' +port)
except Exception,e:
    print('Scan erro:'+str(e))

for host in nm.all_hosts():
    print('--'*20)
    print('Host : s% (s%)' % (host,nm[host].hostname()))
    print('State : s%' % mm[host].state())

for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : {0} ({1})'.format(host, nm[host].hostname()))
    print('State : {0}'.format(nm[host].state()))

    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : {0}'.format(proto))

        lport = list(nm[host][proto].keys())
        lport.sort()
        for port in lport:
            print('port : {0}\tstate : {1}'.format(port, nm[host][proto][port]))


print('----------------------------------------------------')