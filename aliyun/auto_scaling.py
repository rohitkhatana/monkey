from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from client import client
import json



class AutoScaling:

    def __get_auto_scaling_group_with_instances(self):
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('ess.ap-southeast-5.aliyuncs.com')
        request.set_method('POST')
        request.set_version('2014-08-28')
        request.set_action_name('DescribeScalingInstances')

        request.add_query_param('RegionId', 'ap-southeast-5')

        response = client.do_action(request)
        response = json.loads(response)
        return response['ScalingInstances']['ScalingInstance']


    def is_instance_in_auto_scale(self, instance_id):
        instances = self.__get_auto_scaling_group_with_instances()
        instance = filter(lambda instance: instance['InstanceId'] == instance_id, instances)
        return True if len(instance) == 1 else False
