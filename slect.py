#coding:utf:8
from QcloudApi.qcloudapi import QcloudApi
from json import loads
from json import dumps
import json

module = 'cvm'
action = 'DescribeInstances'
config = {
    'Region': 'ap-beijing',
    'secretId': 'AKIDYFqHXa0G82sW9bRtlXEwVt7B4kEZHsjO',
    'secretKey': 'c2KQK2YwAD5lGaieP2Vo0GNJ3by98vYz',
}

action_params = {
    'Version': '2017-03-12',
    'Filters': [{
        'Name': 'zone',
        'Values': ['ap-beijing-1', 'ap-beijing-3']
    },
        {
            'Name': 'private-ip-address',
            'Values': ['172.21.0.3']
        }
    ],
    'Limit': 1,
}
# ________________________________________________


try:
    service = QcloudApi(module, config)
    # print(service.generateUrl(action, action_params))
    # service.call(action, action_params)
    answer = (service.call(action, action_params))
    jss = json.loads(answer)
    # print type(jss)
    # print jss
    # print ('172.21.0.3 '),\
    InstanceId=jss['Response']['InstanceSet'][0]['InstanceId']
    ImageId=jss['Response']['InstanceSet'][0]['ImageId']

    dicts={'ImageId':ImageId,'InstanceId':InstanceId}
    for  i ,j  in dicts.items():
        print(i,j)

except Exception as e:
    import traceback

    print('traceback.format_exc():\n%s' % traceback.format_exc())
# ________________________________________________________
#添加公网IP
# try:
#     action="AllocateAddresses"
#     module='eip'
#     action_params={
#         'Version': '2017-03-12',
#         'AddressCount':2,
#     }
#     service = QcloudApi(module, config)
#
#     addip = (service.call(action, action_params))
#     print (addip)
#____________________________________________________
#绑定公网IP到云主机
try:
    action="AssociateAddress"
    module='eip'
    action_params={
        'Version': '2017-03-12',
        'AddressId':'eip-1uptj0mb',
        'InstanceId':'ins-maluk82x',
    }
    service = QcloudApi(module, config)
    boundip = (service.call(action, action_params))
    print (boundip)

#____________________________________________________
   # zi_dict = eval(answer)
    # print zi_dict['totalCount']
    # instance=(zi_dict['instanceSet'][0])
    # print(len(zi_dict)
    # for instance in zi_dict['instanceSet']:
    # 	a=dict(instance.items())
    #     print(a)
    # if a['lanIp']=='172.21.0.3':
    #     print(a['instanceId'])
    #

except Exception as e:
    import traceback

    print('traceback.format_exc():\n%s' % traceback.format_exc())
