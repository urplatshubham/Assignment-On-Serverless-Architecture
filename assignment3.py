"""
Assignment 3: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3

Objective: To enhance your AWS security posture by setting up a Lambda function that detects any S3 bucket without server-side encryption.

Task: Automate the detection of S3 buckets that don't have server-side encryption enabled.
"""
import boto3
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Initialize the S3 client
    s3_client = boto3.client('s3')
    
    try:
        # Get the list of all buckets
        response = s3_client.list_buckets()
        
        for bucket in response['Buckets']:
            bucket_name = bucket['Name']
            logger.info(f"Processing bucket: {bucket_name}")
            
            # Check the bucket's tags
            try:
                tag_response = s3_client.get_bucket_tagging(Bucket=bucket_name)
                tags = tag_response['TagSet']
                
                # Log the tags for the bucket
                logger.info(f"Tags for bucket {bucket_name}: {tags}")
                
                # Check if the bucket has the 'Env=testing' tag
                is_testing_bucket = any(tag['Key'] == 'Env' and tag['Value'] == 'testing' for tag in tags)
                
                if is_testing_bucket:
                    logger.info(f"Bucket {bucket_name} is tagged for testing.")
                    
                    # Check if the bucket has server-side encryption enabled
                    try:
                        encryption_response = s3_client.get_bucket_encryption(Bucket=bucket_name)
                        logger.info(f"Bucket {bucket_name} has encryption enabled.")
                    except s3_client.exceptions.ClientError as e:
                        error_code = e.response['Error']['Code']
                        if error_code == 'ServerSideEncryptionConfigurationNotFoundError':
                            logger.info(f"Bucket {bucket_name} does not have encryption enabled.")
                        else:
                            logger.error(f"Error checking encryption for bucket {bucket_name}: {e}")
                else:
                    logger.info(f"Bucket {bucket_name} is not tagged for testing.")
                    
            except s3_client.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'NoSuchTagSet':
                    logger.info(f"Bucket {bucket_name} has no tags.")
                else:
                    logger.error(f"Error retrieving tags for bucket {bucket_name}: {e}")
    
    except Exception as e:
        logger.error(f"Error listing buckets: {e}")

    return {
        'statusCode': 200,
        'body': 'Tag and encryption check complete'
    }
