__author__ = 'shivpriya_tamboskar'



from resource_management import *
import sys


def influxdb():
  import params

  Directory([params.conf_dir],
       owner=params.influxdb_user,
       group=params.user_group,
       recursive=True
  )

  Directory([params.influxd_dir],
       owner=params.influxdb_user,
       group=params.user_group,
       recursive=True
  )
  configurations = params.config['configurations']['influxdb-site']

  File(format("{conf_dir}/influxdb.conf"),
       content=Template("influxdb-cluster.conf.j2"),
       owner=params.influxdb_user,
       group=params.user_group
  )

  File(format("{influxd_dir}/influxdb"),
       content=Template("influxdb.conf.j2"),
       owner=params.influxdb_user,
       group=params.user_group
  )