import json

# -*- coding: utf8 -*-
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest

from client import client

class Instance:

    def tags(self, instance_id):
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('ecs.aliyuncs.com')
        request.set_method('POST')
        request.set_version('2014-05-26')
        request.set_action_name('DescribeTags')
        #request.set_resource_type('Instance')
        #request.set_resource_id(instance_id)
        request.add_query_param('ResourceType', 'Instance')
        request.add_query_param('ResourceId', instance_id)
        response = client.do_action(request)
        response = json.loads(response)
        return response['Tags']['Tag']

    def get_instances(self):
        # Create a request and set parameters
        request = DescribeInstancesRequest.DescribeInstancesRequest()
        request.set_PageSize(10)
        # Initiate an API request and display the response value
        response = client.do_action_with_exception(request)
        response = json.loads(response)
        return response['Instances']['Instance']


