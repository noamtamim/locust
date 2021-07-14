#!/usr/bin/env python3

import boto3
import sys


def find_master_ip(master_cluster, master_service):

    client = boto3.client('ecs')

    tasks = client.list_tasks(cluster=master_cluster, serviceName=master_service)

    task = tasks['taskArns'][0]

    task_desc = client.describe_tasks(cluster=master_cluster, tasks=[task])

    return task_desc['tasks'][0]['containers'][0]['networkInterfaces'][0]['privateIpv4Address']



if __name__ == '__main__':
    print(find_master_ip(sys.argv[1], sys.argv[2]))
