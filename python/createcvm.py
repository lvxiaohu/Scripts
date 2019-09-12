from QcloudApi.qcloudapi import QcloudApi
from json import loads
from json import dumps
import json
module='cvm'
action = 'RunInstances'
config = {
    'Region': 'ap-beijing',
    'secretId': 'AKIDYFqHXa0G82sW9bRtlXEwVt7B4kEZHsjO',
    'secretKey': 'c2KQK2YwAD5lGaieP2Vo0GNJ3by98vYz',
}

action_params = {
    'Version':'2017-03-12',
    'InstanceChargeType':'POSTPAID_BY_HOUR',
    'Placement.Zone':'ap-beijing-3',
    'InstanceType':'S2.SMALL1',
    'ImageId':'img-8toqc6s3',
    'DataDisks.0.DiskType':'CLOUD_BASIC',
    'DataDisks.0.DiskSize':'60',
}
#________________________________________________


try:
    service = QcloudApi(module, config)
    print(service.generateUrl(action, action_params))
    # service.call(action, action_params)
    # answer = (service.call(action, action_params))
    # print answer
except Exception as e:
   import traceback
   print('traceback.format_exc():\n%s' % traceback.format_exc())