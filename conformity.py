from client import client
from auto_scaling import AutoScaling
from instances import get_instances

class Conformity:

    def __init__(self):
        self._auto_scaling = AutoScaling()

    def is_auto_scaline_enabled(self):
        return self._auto_scaling.is_instance_in_auto_scale('asd')

    def is_proper_tag(self):
        pass

    def is_monitor_enabled(self):
        pass

    def is_port_open_to_public(self):
        pass

    def _get_instances(self):
        return get_instances()

    def perform(self):
        instances = self._get_instances()
        print instances


Conformity().perform()
