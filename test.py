import boto3
from S3_IaC import empty_bucket 
# create a s3 connection using resource
s3_resource = boto3.resource('s3')

file_name = '7bf371README.md'
local_path = './tmp/'
extra_args = {
    'ACL': 'public-read'
}
for bucket_name in [bucket_from,bucket_thrid,bucket_to]:
    s3_resource.Bucket(bucket_name).delete()
