Python Scripts to reduce the cost by deleting unused and unutilized resources
NatGateways Deletion: 
Step1: Create an EC2 Client: Connect to the EC2 service in the specified region. 
Step2: Describe NAT Gateways: Retrieve information about all NAT Gateways. 
Step3: Iterate Through NAT Gateways: Loop through each NAT Gateway and check its state. 
Step4: Check State: If the NAT Gateway is in the deleting or deleted state, skip it. If it is available, check if it is associated with any VPC. 
Step5: Delete Unused NAT Gateways: If the NAT Gateway is not associated with any VPC, delete it.
 Step6: Print Messages: Print messages indicating the actions taken.

Elastic Ips Deletion:
Step1: Create an EC2 Client: Connect to the EC2 service in the specified region. 
Step2: Describe Elastic IP addresses: Retrieve information about all Elastic IP addresses
Step3: Iterate through the Elastic IP addresses and process each one
Step4 : Check State : if the InstanceID is not in the address then Release the Elastic IP
Step5: Print Messages: Print messages indicating the actions taken

EBS Volumes Snapshots Deletion :
Step1: Create an EC2 Client: Connect to the EC2 service in the specified region. 
Step2: Describe snapshots owned by the user
Step3: Iterate through the snapshots and process each one
Step4: Check  state: if the volume ID is not present then Delete the snapshot
	Else,
Step5: Describe the volume to check its attachments
a)	if the volume is detached then Delete the snapshot
b)	if The volume associated with the snapshot is not found (it might have been deleted) then  Delete the snapshot
