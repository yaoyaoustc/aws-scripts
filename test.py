import boto3
from rdsiac import list_db, create_db_ins, delete_db_ins
# create a s3 connection using resource
s3_resource = boto3.resource('s3')
rds_resource = boto3.client('rds')

#list_db(rds_resource)
#create_db_ins(rds_resource)
delete_db_ins(rds_resource)