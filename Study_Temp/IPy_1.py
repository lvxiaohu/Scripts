#--coding:utf-8
from IPy import IP
ip_s = input('Please input an IP or net-range:')
ips=IP(ip_s)
if len(ips) > 1:
    print('net: %s ' % ips.net())
    print('netmask: %s ' % ips.netmask())
    print('broadcast: %s ' % ips.broadcast())
    print('reverse address: %s ' % ips.reverseName())
    print('subnet: %s ' % len(ips))
else:
    print('reverse address: %s' % ips.reverseName())