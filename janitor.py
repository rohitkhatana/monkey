import paramiko
import json
from instances import Instance

class Janitor:

  instances = Instance()
  username = "root"

  def __init__(self, key, username):
    self.key = key
    self.username = username

  def run_ssh_check(self, commands):
    instanceList = self.instances.get_instances()
    ipList = self.instances.get_ip_list()
    
    commandResult = ""
    err = ""

    for ipAddr in ipList :
      key = paramiko.RSAKey.from_private_key_file(self.key)
      sshClient = paramiko.SSHClient()
      sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      sshClient.connect( hostname = ipAddr, username = self.username, pkey = key )

      for command in commands:
        stdin , stdout, stderr = sshClient.exec_command(command)
        commandResult = stdout.read()
        err = stderr.read()

      sshClient.close()

    return commandResult, err

  def set_commands(self, commands):
    self.commands = commands

  def get_logs_activity(self):
    return self.run_ssh_check(["locate *.log -0 | xargs -0 ls -ltd"])

  def get_last_activity(self):
    return self.run_ssh_check(["last -x"])

  def send_alert(self):
    # implement alert here
    pass
