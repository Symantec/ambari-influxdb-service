__author__ = 'shivpriya_tamboskar'

import sys, os, pwd, signal, time
from resource_management import *
from subprocess import call
from influxdb import influxdb

class influxdb_service(Script):
  def install(self, env):
    # Install packages listed in metainfo.xml
    self.install_packages(env)
    self.configure(env)
    #if any other install steps were needed they can be added here

  def configure(self, env):
    import params
    env.set_params(params)
    influxdb()

  #To stop the service, use the linux service stop command and pipe output to log file
  def stop(self, env):
    import params
    env.set_params(params)
    Execute('service influxdb stop')

  #To start the service, use the linux service start command and pipe output to log file
  def start(self, env):
    import params
    env.set_params(params)
    Execute('service influxdb start')

  #To restart the service, use the linux service restart command and pipe output to log file
  def start(self, env):
    import params
    env.set_params(params)
    Execute('service influxdb restart')

  #To get status of the, use the linux service status command
  def status(self, env):
    import status_params
    env.set_params(status_params)
    check_process_status(status_params.influxdb_pid_file)

if __name__ == "__main__":
    influxdb_service().execute()
