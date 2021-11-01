from django.shortcuts import render
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.http import HttpResponse
from .forms import ContactForm
import logging
import boto3
from botocore.exceptions import ClientError
import os
import json
import random
from django.utils.safestring import mark_safe

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

def getUrlImages(): # return 0 if user choose to upload files
    print("Getting images from cloud")
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('hotdogchecker')
    allImages = []
    for obj in bucket.objects.all():
        allImages.append(obj.key)

    # Let's shuffle the list, so we can show 4 randoms images
    print("Shuffle")
    random.shuffle(allImages)
    # Check réupérerlien image OU DL images
    print("Showing 4 images")
    #Let's take the 4th first pictures (the list has been shuffled)
    UrlImages = []
    for i in range (4):
        UrlImages.append("https://hotdogchecker.s3.amazonaws.com/"+allImages[i])
    return UrlImages
    
def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            s3 = boto3.client('s3')
            s3.download_file('hotdogchecker', 'testOn.txt', 'testOn.txt')
            # Reading
            f = open('testOn.txt')
            myImages = f.readlines()  # Returns a list object

            # getCheckedItems
            checkItems = [0,0,0,0]
            for i in range(4):
                if('image'+str(i+1) in form.cleaned_data['couleur']): 
                    checkItems[i] = 1

            # Writing
            for images in request.session.get('args'):
                if((images.replace('https://hotdogchecker.s3.amazonaws.com/', '')+"\n") not in myImages):
                    with open('testOn.txt', 'a') as writer:
                        writer.write(images.replace('https://hotdogchecker.s3.amazonaws.com/', '')+"\n")

            with open('testOn.txt', 'r') as istr:
                with open('output.txt', 'w') as ostr:
                    ostr.truncate(0)
                    for line in istr:
                        for i in range(4):
                            if request.session.get('args')[i].replace('https://hotdogchecker.s3.amazonaws.com/', '') in line:
                                if(checkItems[i]==0):
                                    line = line.rstrip('\n') + ' 0'
                                else:
                                    line = line.rstrip('\n') + ' 1'
                            else:
                                line = line.rstrip('\n')
                        print(line, file=ostr)
            #os.remove("testOn.txt")
            #os.rename('output.txt', 'testOn.txt')
            upload_file('output.txt', 'hotdogchecker', 'testOn.txt')

    args = getUrlImages()
    request.session['args'] = args
    form = ContactForm()
    return TemplateResponse(request, 'page.html', {'args':args,'form': form})