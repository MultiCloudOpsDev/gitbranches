import boto3

# Create EC2 client
ec2 = boto3.client('ec2', region_name='ap-south-1')  # Mumbai region

# Describe all EC2 instances
response = ec2.describe_instances()

# Loop through instances and print details
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("Instance ID:", instance['InstanceId'])
        print("State:", instance['State']['Name'])
        print("Type:", instance['InstanceType'])
        print("Private IP:", instance.get('PrivateIpAddress', 'N/A'))
        print("Public IP:", instance.get('PublicIpAddress', 'N/A'))
        print("-" * 20)
