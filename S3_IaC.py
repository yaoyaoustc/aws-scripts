import boto3
import uuid

# create bucket name

def create_bucket_name(bucket_prefix):
    '''
    use uuid to create unique bucket name
    '''
    return ''.join([bucket_prefix,str(uuid.uuid4())])

def create_bucket(bucket_prefix, s3_connection):
    '''
    create a bucket using your credentials
    :param bucket_prefix: prefix of your bucket name
    :param s3_connection: s3 connecttion established by boto3

    :return bucket_name
    :return bucket_response as a dictionary
    '''

    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)

    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': current_region
        }
    )
    print(bucket_name, current_region)
    return bucket_name, bucket_response

def create_file_name(file_name):
    return ''.join([str(uuid.uuid4().hex[:6]), file_name])

def upload_file_s3(local_file_name, bucket_name, extra_args, s3_connection):
    s3_file_name = create_file_name(local_file_name)
    s3_connection.Object(bucket_name, s3_file_name) \
                 .upload_file(Filename = local_file_name, \
                              ExtraArgs = extra_args)

def download_file_s3(file_name, bucket_name, s3_connection, local_path):
    s3_connection.Object(bucket_name,file_name) \
                 .download_file(f'{local_path}/{file_name}')
    print('download successful')

def copy_to_bucket(bucket_from, bucket_to, file_name, s3_connection):
    copy_source = {
        'Bucket': bucket_from,
        'Key': file_name
    }
    s3_connection.Object(bucket_to, file_name).copy(copy_source)
    print("copy successful")

def empty_bucket(bucket_name, s3_connection):
    res = []
    bucket = s3_connection.Bucket(bucket_name)
    for obj_version in bucket.object_versions.all():
        res.append({'Key': obj_version.object_key,
                    'VersionId': obj_version.id})
    print(res)
    bucket.delete_objects(Delete={'Objects': res})
    print("bucket is empty")
