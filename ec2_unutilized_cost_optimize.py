import boto3
from datetime import datetime, timedelta

# Create CloudWatch and EC2 clients
cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')
ec2 = boto3.client('ec2', region_name='us-east-1')

# Define the time period for analysis (e.g., last 7 days)
end_time = datetime.utcnow()
start_time = end_time - timedelta(days=7)

# Define the threshold for underutilization (e.g., CPU utilization < 10%)
cpu_threshold = 10.0

# Describe EC2 instances
instances = ec2.describe_instances()

# Initialize a list to store underutilized instance IDs
underutilized_instances = []

# Iterate through the instances and check their CPU utilization
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        
        # Get CPU utilization metrics for the instance
        metrics = cloudwatch.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
            StartTime=start_time,
            EndTime=end_time,
            Period=3600,  # 1-hour intervals
            Statistics=['Average']
        )
        
        # Calculate the average CPU utilization over the period
        datapoints = metrics['Datapoints']
        if datapoints:
            avg_cpu_utilization = sum(dp['Average'] for dp in datapoints) / len(datapoints)
            if avg_cpu_utilization < cpu_threshold:
                underutilized_instances.append(instance_id)
                print(f"Instance {instance_id} is underutilized with average CPU utilization: {avg_cpu_utilization:.2f}%")

# Print the list of underutilized instances
print("Underutilized instances:", underutilized_instances)
'''Explanation:
Create CloudWatch and EC2 Clients: Connect to the CloudWatch and EC2 services in the specified region.
Define Time Period: Set the time period for analyzing CPU utilization (e.g., the last 7 days).
Define Threshold: Set the threshold for underutilization (e.g., CPU utilization < 10%).
Describe EC2 Instances: Retrieve information about all EC2 instances.
Check CPU Utilization: For each instance, retrieve CPU utilization metrics from CloudWatch and calculate the average CPU utilization over the specified period.
Identify Underutilized Instances: If the average CPU utilization is below the threshold, add the instance ID to the list of underutilized instances.
Print Results: Print the list of underutilized instances.'''