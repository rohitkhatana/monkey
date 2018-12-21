import paramiko
import json
from instances import Instance

class Janitor:

  instances = Instance()

  def __init__(self, key, username):
    self.key = key
    self.username = username
    self.commands = ["last -x"]

  def check_last_activity(self):
    instanceList = self.instances.get_instances()
    ipList = self.instances.get_ip_list()

    for ipAddr in ipList :
      key = paramiko.RSAKey.from_private_key_file(self.key)
      sshClient = paramiko.SSHClient()
      sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      sshClient.connect( hostname = ipAddr, username = self.username, pkey = key )

      for command in self.commands:
        stdin , stdout, stderr = sshClient.exec_command(command)
        print stdout.read()
        print stderr.read()

      sshClient.close()
