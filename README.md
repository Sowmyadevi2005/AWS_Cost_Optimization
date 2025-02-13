# AWS_Cost_Optimization
Python Scripts to reduce the cost by deleting unused and unutilized resources

**NatGateways Deleation:**
**Step1**:
Create an EC2 Client: Connect to the EC2 service in the specified region.
**Step2**: 
Describe NAT Gateways: Retrieve information about all NAT Gateways.
**Step3**:
Iterate Through NAT Gateways: Loop through each NAT Gateway and check its state.
**Step4**:
Check State: If the NAT Gateway is in the deleting or deleted state, skip it. If it is available, check if it is associated with any VPC.
**Step5**:
Delete Unused NAT Gateways: If the NAT Gateway is not associated with any VPC, delete it.
**Step6**:
Print Messages: Print messages indicating the actions taken.'''


Describe Elastic IPs

Import the Boto3 Library

import boto3
This line imports the Boto3 library, which is the AWS SDK for Python. It allows you to interact with various AWS services.

Create an EC2 Client

ec2 = boto3.client('ec2', region_name='us-east-1')
This line creates an EC2 client object for the us-east-1 region. The client object is used to interact with the EC2 service.

Describe Elastic IPs

addresses = ec2.describe_addresses()
This line calls the describe_addresses method to retrieve information about all Elastic IP addresses associated with your AWS account. The response is stored in the addresses variable.

Iterate Through the Addresses and Release Unused Ones

for address in addresses['Addresses']:
    if 'InstanceId' not in address:
        ec2.release_address(AllocationId=address['AllocationId'])
        print(f"Released unused Elastic IP: {address['PublicIp']}")
Loop Through Addresses: The for loop iterates through each Elastic IP address in the addresses['Addresses'] list.
Check for Unused Addresses: The if 'InstanceId' not in address condition checks if the Elastic IP address is not associated with any instance (i.e., it is unused).
Release Unused Address: If the Elastic IP address is unused, the ec2.release_address method is called with the AllocationId of the address to release it.
Print Confirmation: A message is printed to confirm that the unused Elastic IP address has been released.
