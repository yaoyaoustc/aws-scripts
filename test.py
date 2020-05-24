import boto3
from S3_IaC import create_file_name, copy_to_bucket, empty_bucket
# create a s3 connection using resource
s3_resource = boto3.resource('s3')

file_name = '7bf371README.md'
local_path = './tmp/'
empty_bucket(bucket_to, s3_resource)