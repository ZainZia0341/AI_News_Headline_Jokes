import boto3
import json

def s3_creation_url():
    s3_client = boto3.client('s3')
    bucket_name = 'aijokes'
    s3_key = 'fine-tunning-data.jsonl'

    local_file_path = 'E:/Kachori/AI_News_Jokes/responses.jsonl'

    # Upload the file
    s3_client.upload_file(local_file_path, bucket_name, s3_key)

    s3_uri = f's3://{bucket_name}/{s3_key}'
    print(f"File uploaded to {s3_uri}")
    return s3_uri

s3_creation_url()
