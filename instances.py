import json

# -*- coding: utf8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest

from client import client

class Instance:

    def get_instances(self):
        # Create a request and set parameters
        request = DescribeInstancesRequest.DescribeInstancesRequest()
        request.set_PageSize(10)
        # Initiate an API request and display the response value
        response = client.do_action_with_exception(request)
        response = json.loads(response)
        return response['Instances']['Instance']
