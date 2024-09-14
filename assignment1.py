"""
Assignment 1: Automated Instance Management Using AWS Lambda and Boto3

Objective: In this assignment, you will gain hands-on experience with AWS Lambda and Boto3, Amazon's SDK for Python. You will create a Lambda function that will automatically manage EC2 instances based on their tags.

Task: You're tasked to automate the stopping and starting of EC2 instances based on tags. 
"""
import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    
    # Getting all instances
    instances = ec2.instances.all()
    
    auto_stop_instances = []
    auto_start_instances = []

    # Iterating through instances and checking their tags
    for instance in instances:
        for tag in instance.tags or []:
            if tag['Key'] == 'Action':
                if tag['Value'] == 'Auto-Stop' and instance.state['Name'] == 'running':
                    auto_stop_instances.append(instance.id)
                elif tag['Value'] == 'Auto-Start' and instance.state['Name'] == 'stopped':
                    auto_start_instances.append(instance.id)
                    
    # Stopping instances with 'Auto-Stop' tag
    if auto_stop_instances:
        print(f'Stopping instances: {auto_stop_instances}')
        ec2.instances.filter(InstanceIds=auto_stop_instances).stop()
        
    # Starting instances with 'Auto-Start' tag
    if auto_start_instances:
        print(f'Starting instances: {auto_start_instances}')
        ec2.instances.filter(InstanceIds=auto_start_instances).start()
    
    #finally if all runs fine this will be printed during test of Lambda
    return {
        'statusCode': 200,
        'body': 'Operation Completed!'
    }
