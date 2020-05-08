import boto3
from S3_IaC import create_file_name, copy_to_bucket, empty_bucket
# create a s3 connection using resource
s3_resource = boto3.resource('s3')

bucket_from = 'yy5fa75245-032f-4cb0-83c0-98cb514a616c'
bucket_to ='yya99ad65a-5590-4096-89d8-65a4949bf759'
file_name = '7bf371README.md'
local_path = './tmp/'
empty_bucket(bucket_to, s3_resource)