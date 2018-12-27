from aliyun.client import client
from aliyun.auto_scaling import AutoScaling
from aliyun.instances import Instance
from aliyun.security_group import SecurityGroup
from aliyun.tag import Tag

class Conformity:

    def __init__(self):
        self._auto_scaling = AutoScaling()
        self._instance = Instance()
        self._security_group = SecurityGroup()
        self._tag = Tag()
        self.__valid_tags = ['env', 'serviceType', 'serviceName']
        self.__valid_env_tag_value = ['dev', 'stage', 'prod', 'uat']

    def is_auto_scaling_enabled(self, instance_id):
        return self._auto_scaling.is_instance_in_auto_scale(instance_id)


    def proper_tag(self, instance_id):
        tags = self._instance.tags(instance_id)
        return self._tag.validate_tags(tags)

    def is_monitor_enabled(self):
        pass

    def is_port_open_to_public(self):
        pass

    def __get_instances(self):
        return self._instance.get_instances()

    def __instances_id(self):
        return map(lambda instance: instance['InstanceId'], self.__get_instances())

    def security_group_status(self, instance):
        security_group_ids = instance['SecurityGroupIds']['SecurityGroupId']
        status = self._security_group.valid_security_groups(security_group_ids)
        msg = ''
        if not status:
            msg = 'contain invalid cidr 0.0.0.0/0 or port range is greater than 0, for ex: allowed range: 22/22'
        return {'valid': status, 'msg': msg}

    def __map_confirmity_status(self, instance):
        return {
            'instance_id': instance['InstanceId'],
            'instance_name': instance['InstanceName'],
            'is_auto_scaling_enabled': self.is_auto_scaling_enabled(instance['InstanceId']),
            'tag_status': self.proper_tag(instance['InstanceId']),
            'is_monitoring_enabled': False,
            'security_group_status': self.security_group_status(instance)
        }

    def perform(self):
        instances = self._instance.get_instances()
        instance_ids = self.__instances_id()
        return map(lambda instance: self.__map_confirmity_status(instance), instances)


