import boto3
import botocore
import os

BUCKET_NAME = os.environ['SSL_KEY_STORE_S3_BUCKET']
KEY = os.environ['SSL_KEY_STORE_S3_FILENAME']

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, KEY)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise