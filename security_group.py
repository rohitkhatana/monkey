import json

# -*- coding: utf8 -*-
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

from client import client

class SecurityGroup:

    def security_group_by_security_id(self, security_id):
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('ecs.aliyuncs.com')
        request.set_method('POST')
        request.set_version('2014-05-26')
        request.set_action_name('DescribeSecurityGroupAttribute')
        request.add_query_param('SecurityGroupId', security_id)
        response = client.do_action(request)
        return json.loads(response)

    def __valid_port_range(self, port_range):
        start_port, end_port = port_range.split('/')
        return start_port == end_port

    def is_valid(self, security_group):
        not_allowd_cidr = '0.0.0.0/0'
        permissions = security_group['Permissions']['Permission']
        invalid_cidrs = filter(lambda permission: permission['SourceCidrIp'] == not_allowd_cidr, permissions)
        invalid_port_range = filter(lambda permission: not self.__valid_port_range(permission['PortRange']), permissions)
        return len(invalid_port_range) == 0 and len(invalid_cidrs) == 0


    def valid_security_groups(self, security_ids):
        result = map(lambda security_id: self.is_valid(self.security_group_by_security_id(security_id)), security_ids)
        return result[0] if result else True

