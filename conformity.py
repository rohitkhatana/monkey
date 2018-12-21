from client import client
from auto_scaling import AutoScaling
from instances import Instance

class Conformity:

    def __init__(self):
        self._auto_scaling = AutoScaling()
        self._instance = Instance()

    def is_auto_scaling_enabled(self, instance):
        return self._auto_scaling.is_instance_in_auto_scale(instance)

    def is_proper_tag(self):
        pass

    def is_monitor_enabled(self):
        pass

    def is_port_open_to_public(self):
        pass

    def __get_instances(self):
        return self._instance.get_instances()

    def __instances_id(self):
        return map(lambda instance: instance['InstanceId'], self.__get_instances())

    def __map_confirmity_status(self, instance_id):
        return {
            'is_auto_scaling_enabled': self.is_auto_scaling_enabled(instance_id),
            'tag_status': '',
            'is_monitoring_enabled': False,
        }

    def perform(self):
        instances = self.__instances_id()
        print map(lambda instance_id: self.__map_confirmity_status(instance_id), instances)

        print instances


Conformity().perform()
