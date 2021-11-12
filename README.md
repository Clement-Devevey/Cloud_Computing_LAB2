# Cloud_Computing_LAB2

# Directory worker-client
The repository will include all the files to run your code, A README, a small report describing your
project and a 3 minutes maximum demo video of your code.

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


# Directory monSite

Go Further: the hot-dog application
You work for a very promising company which goal is to develop an app capable to recognize hot-dogs on
images. To proceed, the company needs labeled data, meaning data with a label 1 when it represents a
hot-dog ; 0 when it represents something else. To help collect and annotate data, you will create a new AWS
application that shows a sample of images to a client (each image successively), let the client label each of
the image, and record/store that label in a table.
- [x] The set of images available for labeling is stored in a S3 bucket
- [x] The file storing the label information for each image is also on a S3 bucket
- [x] Each client is shown 4 random images out of the total number of images that are in the bucket
- [x] If multiple client are shown the same image, you should record each answer in the same text file
- [x] A client can contribute and upload more hot-dog images to the bucket
- [x] You are free to choose whatever images you want to build the set of images (you need around 20
images). Half of this images must represent hot-dogs. As for the other half, pick whatever you want

Thanks to Django, we have been able to link HTML and python. This way, we can get images from the bucket s3 and send the link of theses images to the HTML page. There is also a log file, called testOn.txt, to remember what choices users have made. Users make choices by checking checkbox and then press submit button. 

# Team
- Alexis DEGRANGE
- Clément DEVEVEY
