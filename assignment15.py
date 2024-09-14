"""
Assignment 15: Implement a Log Cleaner for S3

Objective: Create a Lambda function that automatically deletes logs in a specified S3 bucket that are older than 90 days.
"""
import boto3
import logging
from datetime import datetime, timezone, timedelta

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize the S3 client
s3_client = boto3.client('s3')

# Define the number of days after which logs should be archived (e.g., 90 days)
DELETE_AFTER_DAYS = 90

# Specify the backup bucket or folder where logs should be moved before deletion
backup_bucket_name = 's3-sr-logs-backup'  # Replace with your backup bucket name
backup_folder = 'archived-logs/'  # Optional folder within the same bucket or another bucket

def lambda_handler(event, context):
    # Specify the bucket name where logs are currently stored
    source_bucket_name = 's3-sr-logs-storing'  # Replace with your source bucket name

    try:
        # List all objects in the source bucket
        objects = s3_client.list_objects_v2(Bucket=source_bucket_name)

        if 'Contents' in objects:
            for obj in objects['Contents']:
                key = obj['Key']
                last_modified = obj['LastModified']

                # Calculate the age of the object
                age_in_days = (datetime.now(timezone.utc) - last_modified).days

                # If the object is older than the delete threshold, archive and delete it
                if age_in_days > DELETE_AFTER_DAYS:
                    logger.info(f"Archiving log file {key}, last modified {age_in_days} days ago")

                    # Define the new key (location in the backup bucket or folder)
                    new_key = backup_folder + key

                    # Copy the object to the backup location
                    s3_client.copy_object(
                        Bucket=backup_bucket_name,
                        CopySource={'Bucket': source_bucket_name, 'Key': key},
                        Key=new_key
                    )

                    logger.info(f"Log file {key} successfully copied to {new_key} in {backup_bucket_name}.")

                    # Delete the object from the source bucket after copying
                    s3_client.delete_object(Bucket=source_bucket_name, Key=key)

                    logger.info(f"Log file {key} successfully deleted from {source_bucket_name}.")
        else:
            logger.info("No log files found in the bucket.")

    except Exception as e:
        logger.error(f"Error processing bucket {source_bucket_name}: {e}")

    return {
        'statusCode': 200,
        'body': 'Log archiving and cleanup completed successfully'
    }
