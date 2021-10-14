import logging
import boto3
from botocore.exceptions import ClientError
import os
import json
import random
import pathlib
from pathlib import Path
import tkinter as tk
from tkinter import filedialog 




def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# Get buckets from user
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names and set True if hotdogchecker is already existing
print("Checking bucket")
bucket_exist = False
print('Existing buckets:')
for bucket in response['Buckets']:
    if(bucket["Name"]=="hotdogchecker"):
        bucket_exist = True
    print(f'  {bucket["Name"]}')
    
# Create the bucket only if not already existing
# Let's also add 20 images
if(not(bucket_exist)):
    print("Creating bucket")
    create_bucket("hotdogchecker")
    print("bucket OK")
    # Create a bucket policy
    print("Creating bucket policy")

    # Convert the policy from JSON dict to string
    # Set the new policy
    s3.put_bucket_policy(Bucket="hotdogchecker",  Policy='{"Version": "2012-10-17", "Statement": [{ "Sid": "AddPermHotDog","Effect": "Allow","Principal": "*", "Action": [ "s3:GetObject" ], "Resource": ["arn:aws:s3:::hotdogchecker/*" ] } ]}')

    print("Policy OK")
    print("Upload files")
    for i in range(1,11):
        print("uploading"+str(i)+"/10" )
        upload_file(Path().absolute()+"\\images\\trueHotDog"+str(i)+".jpg", "hotdogchecker")
        upload_file(Path().absolute()+"\\images\\falseHotDog"+str(i)+".jpg", "hotdogchecker")
    print("Files uploaded")


print("Getting images from cloud")
s3 = boto3.resource('s3')
bucket = s3.Bucket('hotdogchecker')
allImages = []
for obj in bucket.objects.all():
    allImages.append(obj.key)
    

print(*allImages,  sep = "\n")

if(input("1- upload file 2- get 4 randoms images [1-2] :")=='1'):
    myDialog = tk.Tk()
   # root.withdraw()
    file_path = tk.filedialog.askopenfilename ( title = "Select a file ...",filetypes=(("png files","*.png"),("jpeg files","*.jpg"),("all files","*.*")))
    myDialog.destroy()
    print("uploading "+file_path)
    upload_file(file_path,"hotdogchecker")
    print("File added to bucket")
    
else:
    # Let's shuffle the list, so we can show 4 randoms images
    print("Shuffle")
    random.shuffle(allImages)
    # Check réupérerlien image OU DL images
    print("Showing 4 images")
    #Let's take the 4th first pictures (the list has been shuffled)
    for i in range (4):
        print("https://hotdogchecker.s3.amazonaws.com/"+allImages[i])

    





