#-*- coding:utf-8 -*-
print "It's Qcloud API test!"
from QcloudApi.qcloudapi import QcloudApi
from json import loads
from json import dumps
import json
module='cvm'
action = 'StopInstances'
config = {
    'Region': 'ap-beijing',
    'secretId': 'AKIDBKIA9ye6OUPEr6w8JNHzWzJTTciisCev',
    'secretKey': 'GR3V5YIzb6SNCqIckfPzlSr661oPo25z',
}
action_params = {
    # 'limit':2,
    # 'private-ip-address':'172.21.16.3',
   # 'instance-id':'ins-0wl1ujk7',
    # 'Filters.1.Name':'private-ip-address',
    # 'Filters.1.Values.1':'172.21.16.3',
    'Version': '2017-03-12',
    #'Region':'ap-beijing',
    'InstanceIds.1':'ins-3aesju6b',
	# 'Filters': [{
 #        'Name': 'zone',
 #        'Values': ['ap-beijing-3','ap-beijing-1']
    # },
    # {
    # 	'Name':'private-ip-address',
    # 	'Values':['172.21.16.3']
    # }
    # ],
    'ForceStop':'FALSE',
}
try:
    service = QcloudApi(module, config)
   # print(service.generateUrl(action, action_params))
    return  service.call(action, action_params)
   # res=json.loads(answer)
   # print res
#------------------------------
    service.generateUrl(action, action_params)
    answer = (service.call(action, action_params))
    print answer
    # print answer
    # zi_dict=eval(answer)
    # print zi_dict['totalCount']
    # instance=(zi_dict['instanceSet'][0])
    # print(len(zi_dict)
    # for instance in zi_dict['instanceSet']:

    # 	a=dict(instance.items())
    # 	print(a)
    	# if a['lanIp']=='172.21.16.3':
    		# print(a['instanceId'])
    # for  k,v in instance.items():
    	# if k == 'lanIp' and v =='172.21.16.3':

        # print(k,v)
#______________________________
except Exception as e:
   import traceback
   print('traceback.format_exc():\n%s' % traceback.format_exc())













