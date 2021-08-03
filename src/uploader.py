import boto3
import os
 
def upload_files(path):
    session = boto3.Session(
        aws_access_key_id='AKIA3IXH2WVCGBCFTX5E',
        aws_secret_access_key='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',
        region_name='us-west'
    )
    s3 = session.resource('s3')
    bucket = s3.Bucket('kimikat')
 
    for subdir, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(subdir, file)
            with open(full_path, 'rb') as data:
                bucket.put_object(Key=full_path[len(path)+1:], Body=data)
 
if __name__ == "__main__":
    upload_files('/Users/nicolacave/dsi_galvanize/capstones/capstone3/data/data')