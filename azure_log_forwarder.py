import os
import sys
import json
import socket
import datetime

from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.monitor import MonitorManagementClient
from azure.identity import DefaultAzureCredential

# fetch events with monitor cli


class AzureLogForwarder:

    def __init__(self, host, port, outfile):
        self.credential = DefaultAzureCredential()
        self.auth_file = os.path.dirname(__file__) + '/resource/local-sp.json'
        self.monitor_client = get_client_from_auth_file(
            MonitorManagementClient,
            credential=self.credential,
            auth_path=self.auth_file
        )
        self.midnight = datetime.datetime.combine(datetime.datetime.today(), datetime.time())
        self.log_filter = "eventTimestamp ge %s" % self.midnight
        self.out_file = outfile
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = host
        self.port = port
        self.event_id_store = os.path.dirname(__file__) + '/resource/event_id_store.data'
        self.last_event_id = open(self.event_id_store, 'r').readlines()[-1].strip('\n')

    def forward(self, log):
        """
        A method to forward logs to graylog input
        :param host:
        :param port:
        :param log:
        :return:
        """
        if sys.version_info.major == '2':
            self._socket.sendto(log, (self.host, int(self.port)))
        else:
            self._socket.sendto(bytes(log), (self.host, int(self.port)))

    def run(self):
        try:
            activities = self.monitor_client.activity_logs.list(filter=self.log_filter, select=None)
            event_store = []

            # get only administrative events
            for i in activities:
                event_dict = i.as_dict()
                if event_dict['category']['value'] == "Administrative":
                    event_store.append(event_dict)

            # find top event id
            top_event = event_store[0]
            top_event_id = top_event['event_data_id']

            # check whether new event are there
            if top_event_id == self.last_event_id:
                print("No new events found")
            else:
                # if there is new event then remember it
                with open(self.event_id_store, 'a+') as id_store:
                    id_store.write("%s\n" % top_event_id)

                # process only new event
                for log in event_store[::-1]:
                    if log['event_data_id'] == self.last_event_id:
                        break
                    else:
                        with open(self.out_file, 'a+') as log_file:
                            jstr = json.dumps(log)
                            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            event = 'Azure - ' + now + " " + jstr + '\n'
                            self.forward(event)
                            log_file.write(event)
                            print(event)
        except IndexError:
            print("No new events found!")
