"""
Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

Objective: To gain experience with AWS Lambda and Boto3 by creating a Lambda function that will automatically clean up old files in an S3 bucket.

Task: Automate the deletion of files older than 30 days in a specific S3 bucket.
"""
import json
import boto3
from datetime import datetime, timezone, timedelta

# Initialize S3 client
s3 = boto3.client('s3')
    
def lambda_handler(event, context):
    # TODO implement
    bucket_name = 'sr-autoclean-s3'
    days_old = 30  # Customize based on how old the files should be
    
    # Get the current time
    now = datetime.now(timezone.utc)
    
    # Get the list of objects in the S3 bucket
    response = s3.list_objects_v2(Bucket=bucket_name)
    
    if 'Contents' in response:
        for obj in response['Contents']:
            # Get the last modified date of the object
            last_modified = obj['LastModified']
            
            # Calculate the file's age
            file_age = now - last_modified
            
            # Delete file if it's older than the specified number of days
            if file_age > timedelta(days=days_old):
                print(f"Deleting {obj['Key']}...")
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
    else:
        print("Bucket is empty or no files to delete.")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Cleanup complete.')
    }
