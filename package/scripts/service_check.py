__author__ = 'shivpriya_tamboskar'

from resource_management import *
from resource_management.libraries.functions import get_unique_id_and_date

class ServiceCheck(Script):
  def service_check(self, env):
    import params
    env.set_params(params)

    Execute('service influxdb status')

if __name__ == "__main__":
  ServiceCheck().execute()
