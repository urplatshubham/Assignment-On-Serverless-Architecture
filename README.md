# Assignment-On-Serverless-Architecture

## **Overview**
This document provides a detailed description of how I completed this assignment:

1. **Assignment 1**: Automated Instance Management Using AWS Lambda and Boto3
2. **Assignment 2**: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3
3. **Assignment 3**: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3
4. **Assignment 15**: Implement a Log Cleaner for S3

---

## **Assignment 1: Automated Instance Management Using AWS Lambda and Boto3**

### **Objective**
The goal of this assignment was to automate the stopping and starting of EC2 instances based on tags using AWS Lambda and Boto3. Specifically, instances with the tag `Auto-Start` are started, and instances with the tag `Auto-Stop` are stopped.

### **Steps I took to complete this assignment**
1. **Creating a lambda function**:
   - I navigated to Lambda page -> Named the function "SR-EC2_AutoStartStop"
   - I used an **existing IAM role** that already had permissions to access EC2 and manage instances.
   - I used 'Sonal_EC2FullAcess' which had the role configured for my Lambda function to use
   - I added an estimate timeout of 2 min to prevent from failing of execution of the lambda function
  
2. **Create EC2 instances**:
   - I created EC2 instance one with custom tags.
   - For the first instance, I added the tag:
     Key: Action and Value: Auto-Stop
   - Similarly, For the second instance:
     Key: Action and Value: Auto-Start
   - Launched both the instances

3. **Writing the Lambda Function Code**:
I wrote a Python-based Lambda function using **Boto3** to describe EC2 instances, checking their tags, and either stop or start the instances leveraging some help from internet and ChatGPT.

4. **Testing**:
I manually tested the function by invoking the Lambda function in the console and checking the EC2 dashboard for status changes. Then I checked the cloudwatch log for verifying
![CloudWatchResult](https://github.com/urplatshubham/Assignment-On-Serverless-Architecture/blob/main/Assignment%20-%20Screenshots/Assignment1-watchlog.png)
---

## **Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3**

### **Objective**
The goal of this assignment was to automate the deletion of files older than 30 days from a specific S3 bucket using AWS Lambda and Boto3.

### **Steps Implemented**
1. **Creating a lambda function**:
   - I navigated to Lambda page -> Named the function "S3CleanupFunction-SR"
   - I used an **existing IAM role** that already had permissions to access S3 and manage storage.
   - I used 'service-role/prashant-s3-lambda-role' which had the role configured for my Lambda function to use.
   - Attached screenshot for referrence: ![CloudWatchResult](https://github.com/urplatshubham/Assignment-On-Serverless-Architecture/blob/main/Assignment%20-%20Screenshots/Role-assignment.png)
   - I added an estimate timeout of 2 min to prevent from failing of execution of the lambda function

2. **Writing the Lambda Function Code**:
I wrote a Python-based Lambda function using **Boto3** to list the objects in an S3 bucket and delete those older than 30 days leveraging some help from internet and ChatGPT.

3. **Testing**:
I manually Uploaded a file to the S3 bucket which was an old one (30 days older) and invoked function by manually invoking it. Verified that files older than 30 days were successfully deleted.
![CloudWatchResult](https://github.com/urplatshubham/Assignment-On-Serverless-Architecture/blob/main/Assignment%20-%20Screenshots/Assignment2-cleanup.png)
---

## **Assignment 3: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3**

### **Objective**
The goal of this assignment was to identify S3 buckets that do not have server-side encryption enabled and log the results.

### **Steps Implemented**
1. **Creating a lambda function**:
   - I navigated to Lambda page -> Named the function "S3CleanupFunction-SR"
   - I used an **existing IAM role** that already had permissions to access S3 and manage storage.
   - I used 'service-role/prashant-s3-lambda-role' which had the role configured for my Lambda function to use
   - I added an estimate timeout of 2 min to prevent from failing of execution of the lambda function

2. **Writing the Lambda Function Code**:
I wrote a Python-based Lambda function using **Boto3** to check all S3 buckets for encryption and log the ones that do not have encryption enabled leveraging some help from internet and ChatGPT.

3. **Testing**:
I manually tested the function by checking the CloudWatch logs for unencrypted buckets for which I have attached a screenshot above.
![CloudWatchResult](https://github.com/urplatshubham/Assignment-On-Serverless-Architecture/blob/main/Assignment%20-%20Screenshots/Logs-Assignment3.png)
---

## **Assignment 15: Implement a Log Cleaner for S3**

### **Objective**
The goal of this assignment was to implement a Lambda function that automatically deletes log files older than 90 days from an S3 bucket.

1. **Creating a lambda function**:
   - I navigated to Lambda page -> Named the function "S3CleanupFunction-SR"
   - I used an **existing IAM role** that already had permissions to access S3 and manage storage.
   - I used 'service-role/prashant-s3-lambda-role' which had the role configured for my Lambda function to use
   - Add an estimate timeout of 2 min to prevent from failing of execution of the lambda function

2. **Writing the Lambda Function Code**:
I wrote a Python-based Lambda function using **Boto3** to delete log files older than 90 days from the specified S3 bucket leveraging some help from internet and ChatGPT.

### **Testing**:
1. To test the functionality of the code:
   - I **Changed the `DELETE_AFTER_DAYS` value to 1** to simulate older logs.
   - Then I **Uploaded a log file** with a modification date from the previous day into the S3 bucket.
   - I manually invoked the Lambda function to check whether the function detected and deleted the log file.
   - Finally verified that the log file was deleted and that the appropriate logging information was written to CloudWatch.

3. After confirming that the Lambda with its desired functionality worked with a simulated 1-day old log, reverted the `DELETE_AFTER_DAYS` value to 90 for actual use.
![CloudWatchResult](https://github.com/urplatshubham/Assignment-On-Serverless-Architecture/blob/main/Assignment%20-%20Screenshots/Assignment15.png)
---

## **Conclusion**
With the help of the assignments I was able to demonstrate how to automate routine AWS tasks using Lambda and Boto3, including EC2 management, S3 file cleanup, and auditing bucket encryption.

