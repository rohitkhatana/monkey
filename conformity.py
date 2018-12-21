from client import client
from auto_scaling import AutoScaling
from instances import Instance

class Conformity:

    def __init__(self):
        self._auto_scaling = AutoScaling()
        self._instance = Instance()
        self.__valid_tags = ['env', 'serviceType', 'serviceName']
        self.__valid_env_tag_value = ['dev', 'stage', 'prod', 'uat']

    def is_auto_scaling_enabled(self, instance_id):
        return self._auto_scaling.is_instance_in_auto_scale(instance_id)

    def __tag_display_msg(self, valid, msg):
        return {'valid': valid, 'msg': msg}

    def __valid_env_tag_value(self, tags):
        env = filter(lambda tag: tag['TagKey'] == 'env', tags)
        if len(env) == 1:
            if env[0]['TagValue'] in self.__valid_env_tag_value:
                return True
            else:
                return False
        else:
            False

    def __find_missing_tags(self, tags):
        valid = False
        msgs = []
        if not self.__valid_env_tag(tags):
            msgs.append('invalid value for env tag or tag missing, valid value'.append(''.join(self.__valid_env_tag_value)))
        missing = filter(lambda tag: tag['TagKey'] not in self.__valid_tags, tags)
        #TODO: check for other tags value also
        if len(missing) == 0:
            return True, msgs
        else:
            return False, msgs

    def proper_tag(self, instance_id):
        tags = self._instance.tags(instance_id)

        if len(tags) == 0:
            return self.__tag_display_msg(False, 'missing environment, serviceName, serviceType tag')
        else:
            invalid, msgs = self.__find_missing_tags(tags)
            return self.__tag_display_msg(invalid, ''.join(msgs))

    def is_monitor_enabled(self):
        pass

    def is_port_open_to_public(self):
        pass

    def __get_instances(self):
        return self._instance.get_instances()

    def __instances_id(self):
        return map(lambda instance: instance['InstanceId'], self.__get_instances())

    def __map_confirmity_status(self, instance):
        return {
            'is_auto_scaling_enabled': self.is_auto_scaling_enabled(instance['InstanceId']),
            'tag_status': self.proper_tag(instance['InstanceId']),
            'is_monitoring_enabled': False,
        }

    def perform(self):
        instances = self._instance.get_instances()
        instance_ids = self.__instances_id()
        print map(lambda instance: self.__map_confirmity_status(instance), instances)

        print instances


Conformity().perform()
