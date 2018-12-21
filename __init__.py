# -*- coding: utf8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest
from credentials import ACCESS_ID, ACCESS_SECRET, REGION
# Create an AcsClient instance
client = AcsClient(ACCESS_ID, ACCESS_SECRET, REGION)
'''
# Create a request and set parameters
request = DescribeInstancesRequest.DescribeInstancesRequest()
request.set_PageSize(10)
# Initiate an API request and display the response value
response = client.do_action_with_exception(request)
print response
'''
