#!/usr/bin/env python3

import boto3
import sys
from urllib.request import urlretrieve
from os import system


locustfile_url, master_cluster, master_service, master_port = sys.argv[1:]


def find_master_ip():

    client = boto3.client('ecs')

    tasks = client.list_tasks(cluster=master_cluster, serviceName=master_service)

    task = tasks['taskArns'][0]

    task_desc = client.describe_tasks(cluster=master_cluster, tasks=[task])

    return task_desc['tasks'][0]['containers'][0]['networkInterfaces'][0]['privateIpv4Address']


urlretrieve(locustfile_url, 'locustfile.py')

master_ip = find_master_ip()

cmd = f'locust --worker --master-host={master_ip} --master-port={master_port}'
print('Starting locust:', cmd)

system(cmd)
