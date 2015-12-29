__author__ = 'shivpriya_tamboskar'

from resource_management import *

config = Script.get_config()

#influxdb_pid_file = format("{influxdb_pid_dir}/influxdb.pid")

influxdb_pid_file = "/var/run/influxdb/influxd.pid"