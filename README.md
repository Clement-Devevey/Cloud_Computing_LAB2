# Cloud_Computing_LAB2
Cloud_Computing_LAB2

# Files worker.py and client.py
The repository will include all the files to run your code, A README, a small report describing your
project and a 3 minutes maximum demo video of your code.
- Deadline : October 31th 2021

Goals
- Create an AWS application in which a client submits a request to a worker on EC2. The request is
composed of a list of integers.
- The EC2 worker is a Python application that receives the list (the request) and calculates the min, max,
mean, median and send them back to the client.
- After sending the response, the EC2 worker must write a log file describing this transaction as txt file
on S3 Amazon Storage Cloud.
- Additional details
– the client is limited to 10 numbers. If more numbers are entered, a message error should be sent
– numbers must be positive - again a message error is sent to the client if one of the number is not
positive

<<<<<<< HEAD

https://docs.djangoproject.com/fr/3.2/intro/tutorial01/
https://medium.datadriveninvestor.com/basic-application-with-django-3afab115bb9a

https://aws.plainenglish.io/using-node-js-to-display-images-in-a-private-aws-s3-bucket-4c043ed5c5d0


=======
# Files bucket.py

Go Further: the hot-dog application
You work for a very promising company which goal is to develop an app capable to recognize hot-dogs on
images. To proceed, the company needs labeled data, meaning data with a label 1 when it represents a
hot-dog ; 0 when it represents something else. To help collect and annotate data, you will create a new AWS
application that shows a sample of images to a client (each image successively), let the client label each of
the image, and record/store that label in a table.
- [x] The set of images available for labeling is stored in a S3 bucket
- [ ] The file storing the label information for each image is also on a S3 bucket
- [ ] Each client is shown 4 random images out of the total number of images that are in the bucket
- [ ] If multiple client are shown the same image, you should record each answer in the same text file
- [x] A client can contribute and upload more hot-dog images to the bucket
- [x] You are free to choose whatever images you want to build the set of images (you need around 20
images). Half of this images must represent hot-dogs. As for the other half, pick whatever you want
>>>>>>> 7e27282eb829748102691837291b02129312a4e2
