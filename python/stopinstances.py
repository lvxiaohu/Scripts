#-*- coding:utf-8 -*-
print "It's Qcloud API test! For Stop Instances"
from QcloudApi.qcloudapi import QcloudApi
from json import loads
from json import dumps
import json
module='cvm'
action = 'DescribeImages'
config = {
    'Region': 'ap-beijing',
    'secretId': 'AKIDYFqHXa0G82sW9bRtlXEwVt7B4kEZHsjO',
    'secretKey': 'c2KQK2YwAD5lGaieP2Vo0GNJ3by98vYz',
}
action_params = {
    # 'limit':2,
    'Version': '2017-03-12',
    'InstanceIds.1':'ins-3aesju6b',
    'private-ip-address':'172.21.0.5',
    'ForceStop':'TRUE',

}
try:
    service = QcloudApi(module, config)
    # print(service.generateUrl(action, action_params))
    service.call(action, action_params)
    # res=json.loads(answer)
    # print res
#------------------------------
    service.generateUrl(action, action_params)
    answer = (service.call(action, action_params))
    print answer
    # print answer
    # zi_dict=eval(answer)  ``
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
