import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import boto3
import io
from PIL import Image

s3 = boto3.resource('s3', region_name='us-east-1')
bucket = s3.Bucket('mybucket15825')
object = bucket.Object('264893.jpg')

file_stream = io.BytesIO()
object.download_fileobj(file_stream)

im = Image.open(file_stream)
im.show('image')
#img = mpimg.imread(file_stream)
# whatever you need to do