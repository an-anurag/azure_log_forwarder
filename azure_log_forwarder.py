import os
import json
import datetime

from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.monitor import MonitorManagementClient

# fetch events with monitor cli


class AzureLogForwarder:

    def __init__(self):
        self.auth_file = os.path.dirname(__file__) + '/resource/local-sp.json'
        self.monitor_client = get_client_from_auth_file(MonitorManagementClient, auth_path=self.auth_file)
        self.log_filter = "eventTimestamp ge 2021-01-17 15:26:26.896643"
        self.out_file = '/var/log/azure.log'

    def forward(self):
        activities = self.monitor_client.activity_logs.list(filter=self.log_filter, select=None)
        with open(self.out_file, 'a+') as log_file:
            for i in activities:
                jstr = json.dumps(i.as_dict())
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                event = 'Azure - ' + now + " " + jstr + '\n'
                print(event)
                log_file.write(event)


az = AzureLogForwarder()
az.forward()
