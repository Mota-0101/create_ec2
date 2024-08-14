import boto3

s3_client = boto3.client('s3')

bucket_name = 'curso-boto3-teste-321'

response = s3_client.create_bucket(
    Bucket=bucket_name,
)


print(response)
print(f'Bucket s3 "{bucket_name}" criado com sucesso.')