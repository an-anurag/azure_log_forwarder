import os

from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.monitor import MonitorManagementClient

# Authenticate with auth file
auth_file = os.path.dirname(__file__) + '/resource/local-sp.json'
monitor_client = get_client_from_auth_file(MonitorManagementClient, auth_path=auth_file)

# fetch events with monitor cli
log_filter = "eventTimestamp ge 2021-01-17 15:26:26.896643"
select = ",".join(["eventTimestamp", "eventName", "operationName", "resourceGroupName"])
activities = monitor_client.activity_logs.list(filter=log_filter, select=None)
"""
 '_attribute_map', '_classify', '_create_xml_node', '_flatten_subtype', '_get_rest_key_parts', '_infer_class_models', 
 '_subtype_map', '_validation', 'additional_properties', 'as_dict', 'authorization', 'caller', 'category', 'claims', 
 'correlation_id', 'description', 'deserialize', 'enable_additional_properties_sending', 'event_data_id', 'event_name', 
 'event_timestamp', 'from_dict', 'http_request', 'id', 'is_xml_model', 'level', 'operation_id', 'operation_name', 
 'properties', 'resource_group_name', 'resource_id', 'resource_provider_name', 'resource_type', 'serialize', 'status', 
 'sub_status', 'submission_timestamp', 'subscription_id', 'tenant_id', 'validate'
"""
print(dir(activities))
"""
'advance_page', 'async_advance_page', 'async_get', 'current_page', 'get', 'next', 'next_link', 'raw', 'reset'
"""
print(activities.raw)
print(activities.next)
print(activities.next_link)