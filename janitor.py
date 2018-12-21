import paramiko
import json
from instances import get_instances

class Janitor:

  def __init__(self, key, username):
    self.key = key
    self.username = username

  def check_last_activity(self, dataInstances):
    instanceList = get_instances()
    ipList = []
    for instance in instanceList :
      ipList.append(instance["PublicIpAddress"]["IpAddress"][0])

    for ipAddr in ipList :
      key = paramiko.RSAKey.from_private_key_file(self.key)
      sshClient = paramiko.SSHClient()
      sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      sshClient.connect( hostname = ipAddr, username = self.username, pkey = key )
      commands = [ "last -x" ]

      for command in commands:
        stdin , stdout, stderr = sshClient.exec_command(command)
        print stdout.read()
        print stderr.read()

      sshClient.close()
