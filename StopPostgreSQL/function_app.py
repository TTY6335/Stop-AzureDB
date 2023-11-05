import azure.functions as func
import datetime
import json
import logging

from azure.identity import DefaultAzureCredential
# Module for Mysql - Single Server
from azure.mgmt.rdbms import postgresql
# Module for PostgreSQL - Flexible Server
from azure.mgmt.rdbms import postgresql_flexibleservers

# Azure Subscription ID
subscription_id = '<YOUR_SUBSCRIPTION_ID>'

# Azure Resource Group Name
resource_group_name = '<YOUR_RESOURCE_GROUP_NAME>'


app = func.FunctionApp()
#Set schedule in UTC {second} {minute} {hour} {day} {month} {day-of-week}
@app.timer_trigger(schedule="0 0 13 * * *", arg_name="myTimer", run_on_startup=False,use_monitor=False) 
def StopPostgreSQL(myTimer: func.TimerRequest) -> None:
    # Get Azure Credentials
    credentials = DefaultAzureCredential()
    
    # Make single server for PostgreSQL management client
    postgresql_client = mysql.PostgreSQLManagementClient(credentials, subscription_id)

    # Get list of single servers
    servers = postgresql_client.servers.list_by_resource_group(resource_group_name)
    logging.info(servers)
    for server in servers:
        #Stop Mysql - Single Server
        logging.info('STOP %s',server.name)
        postgresql_client.servers.begin_stop(resource_group_name, server.name)


    # Make flexible servers for PostgreSQL management client
    postgresql_flex_client = postgresql_flexibleservers.PostgreSQLManagementClient(credentials, subscription_id)
    # Get list of flexible servers
    servers = postgresql_flex_client.servers.list_by_resource_group(resource_group_name)
    logging.info(servers)
    for server in servers:
        #Stop PostgreSQL - Flexible Server
        logging.info('STOP %s',server.name)
        postgresql_flex_client.servers.begin_stop(resource_group_name, server.name)

