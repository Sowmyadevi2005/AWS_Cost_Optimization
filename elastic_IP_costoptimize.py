import boto3  # Import the Boto3 library to interact with AWS services

# Create an EC2 client for the 'us-east-1' region
ec2 = boto3.client('ec2', region_name='us-east-1')

# Describe Elastic IP addresses
elasticip_response = ec2.describe_addresses()

# Iterate through the Elastic IP addresses and process each one
for response in elasticip_response['Addresses']:
    if 'InstanceId' not in response:  # Check if the Elastic IP is not attached to any instance
        ec2.release_address(AllocationId=response['AllocationId'])  # Release the Elastic IP
        print(f"Elastic IP address {response['PublicIp']} is deleted as it is not attached to any instance")  # Print a message indicating the Elastic IP was deleted