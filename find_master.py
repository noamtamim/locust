#!/usr/bin/env python3

import boto3
import sys
import time


client = boto3.client('ecs')


def run_and_wait(func, sleep_sec, max_sleep):
    total_sleep = 0
    while True:
        result = func()
        
        if result:
            return result
        
        if total_sleep > max_sleep:
            return None
        
        print('Waiting...', file=sys.stderr)
        time.sleep(sleep_sec)
        total_sleep += sleep_sec
        

def find_master_ip(master_cluster, master_service):
    
    def get_master_task():
        task_arns = client.list_tasks(cluster=master_cluster, serviceName=master_service)['taskArns']
        if task_arns:
            return task_arns[0]

        return None
    
    def get_task_ip_if_running(task):
        task_desc = client.describe_tasks(cluster=master_cluster, tasks=[task])['tasks'][0]
        status = task_desc['lastStatus']
        if status == 'RUNNING':
            return task_desc['containers'][0]['networkInterfaces'][0]['privateIpv4Address']
        
        print('Task status:', status, file=sys.stderr)
        return None
        
    master_task = run_and_wait(get_master_task, 2, 60)
    if not master_task:
        print('Timed-out waiting for master to be started', file=sys.stderr)
        return None
    
    master_ip = run_and_wait(lambda: get_task_ip_if_running(master_task), 5, 120)
    if not master_ip:
        print('Timed-out waiting for master to be running', file=sys.stderr)
        return None
    
    return master_ip


if __name__ == '__main__':
    master_ip = find_master_ip(sys.argv[1], sys.argv[2])
    if not master_ip:
        print('Master is not available', file=sys.stdin)
        exit(1)
    
    print(master_ip)
