import boto3

# Create an EC2 client for the 'us-east-1' region
ec2 = boto3.client('ec2', region_name='us-east-1')

# Describe NAT Gateways
nat_gateways_response = ec2.describe_nat_gateways()

# Iterate through the NAT Gateways and process each one
for nat_gateway in nat_gateways_response['NatGateways']:
    nat_gateway_id = nat_gateway['NatGatewayId']  # Get the NAT Gateway ID
    state = nat_gateway['State']  # Get the state of the NAT Gateway

    # Check if the NAT Gateway is not in use (states: 'available', 'pending', 'deleting', 'deleted')
    if state in ['deleting', 'deleted']:
        print(f"NAT Gateway {nat_gateway_id} is already being deleted or has been deleted.")
    elif state == 'available':
        # Check if the NAT Gateway is associated with any VPC
        vpc_id = nat_gateway.get('VpcId')
        if not vpc_id:
            # Delete the NAT Gateway if it is not associated with any VPC
            ec2.delete_nat_gateway(NatGatewayId=nat_gateway_id)
            print(f"Deleted NAT Gateway {nat_gateway_id} as it is not associated with any VPC.")
        else:
            print(f"NAT Gateway {nat_gateway_id} is associated with VPC {vpc_id} and is in use.")
    else:
        print(f"NAT Gateway {nat_gateway_id} is in state {state} and cannot be deleted.")



