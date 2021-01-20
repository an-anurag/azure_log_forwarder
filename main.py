from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.monitor import MonitorManagementClient
import datetime
import os

cred_file = os.path.dirname(__file__) + "/resource/local-sp.json"
# Get a client for Monitor
client = get_client_from_auth_file(MonitorManagementClient, auth_path=cred_file)
print(client)
# Generate query here
today = datetime.datetime.now().date()
print(today)
filter = "eventTimestamp ge {}".format(today)
select = ",".join(["eventTimestamp", "eventName", "operationName", "resourceGroupName"])

# Grab activity logs
activity_logs = client.activity_logs.list(filter=filter, select=select)
print(activity_logs)
# Print the logs
for log in activity_logs:
    print(" ".join([
        str(log.event_timestamp),
        str(log.resource_group_name),
        log.event_name.localized_value,
        log.operation_name.localized_value
    ]))
