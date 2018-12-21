from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from client import client

request = CommonRequest()
request.set_accept_format('json')
request.set_domain('ess.ap-southeast-5.aliyuncs.com')
request.set_method('POST')
request.set_version('2014-08-28')
request.set_action_name('DescribeScalingInstances')

request.add_query_param('RegionId', 'ap-southeast-5')

response = client.do_action(request)
print(response) 
