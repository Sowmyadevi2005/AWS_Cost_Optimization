import boto3  # Import the Boto3 library to interact with AWS services

# Create an EC2 client for the 'us-east-1' region
ec2 = boto3.client('ec2', region_name='us-east-1')

# Describe snapshots owned by the user
snapshot_response = ec2.describe_snapshots(OwnerIds=['self'])

# Iterate through the snapshots and process each one
for snapshot in snapshot_response['Snapshots']:
    snapshot_id = snapshot['SnapshotId']  # Get the snapshot ID
    volume_id = snapshot.get('VolumeId')  # Safely get the volume ID

    if not volume_id:  # Check if the volume ID is not present
        ec2.delete_snapshot(SnapshotId=snapshot_id)  # Delete the snapshot
        print(f"Deleted EBS snapshot {snapshot_id} as it was not attached to any volume.")  # Print a message indicating the volume ID was not found

    else:
        try:
            # Describe the volume to check its attachments
            volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
            if not volume_response['Volumes'][0]['Attachments']:  # Check if the volume is detached
                ec2.delete_snapshot(SnapshotId=snapshot_id)  # Delete the snapshot
                print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.")
        except ec2.exceptions.ClientError as e:
            if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                # The volume associated with the snapshot is not found (it might have been deleted)
                ec2.delete_snapshot(SnapshotId=snapshot_id)  # Delete the snapshot
                print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found")  # Print a message indicating the snapshot was deleted