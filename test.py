import os
from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.monitor import MonitorManagementClient

# This form of get_client_from_auth_file relies on the AZURE_AUTH_LOCATION
# environment variable.
cred_file = os.path.dirname(__file__) + "/resource/local-sp.json"
monitor_client = get_client_from_auth_file(MonitorManagementClient, auth_path=cred_file)
print(monitor_client.activity_logs)
print(dir(monitor_client.activity_logs))