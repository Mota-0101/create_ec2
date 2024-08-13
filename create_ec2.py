import boto3

ec2_cliente = boto3.client('ec2', region_name='us-east-1')

instance_type = "t2.micro"
ami_id = "ami-04a81a99f5ec58529"

response = ec2_cliente.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    MinCount=1,
    MaxCount=1
)

instance_id = response['Instances'][0]['InstanceId']

print(response)

print(f"Instância EC2 de ID: {instance_id} criada com sucesso!")
