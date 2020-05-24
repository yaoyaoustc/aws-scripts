import boto3
from S3_IaC import empty_bucket 
# create a s3 connection using resource
s3_resource = boto3.resource('s3')

<<<<<<< HEAD
=======
bucket_from = 'yy5fa75245-032f-4cb0-83c0-98cb514a616c'
bucket_to ='yya99ad65a-5590-4096-89d8-65a4949bf759'
bucket_thrid = 'yyb21efcdf-b08d-45d0-b004-97417c9ef52c'
>>>>>>> 27ab130b511d21f73f1ef9f35693c070544c89b8
file_name = '7bf371README.md'
local_path = './tmp/'
extra_args = {
    'ACL': 'public-read'
}
for bucket_name in [bucket_from,bucket_thrid,bucket_to]:
    s3_resource.Bucket(bucket_name).delete()
