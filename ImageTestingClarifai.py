from __future__ import print_function
from clarifai.client import ClarifaiApi
import time 
import requests
import operator
import json
import numpy as np

# Python Image Testing Example  https://github.com/clarifai/clarifai-python
# Clarifai Python Client
# Installation
# pip install git+git://github.com/Clarifai/clarifai-python.git
# set CLARIFAI_APP_ID=<an_application_id_from_your_account>
# set CLARIFAI_APP_SECRET=<an_application_secret_from_your_account>

key = "GiP3Poy1i8KVbA1jt0rF9LOSnYuzL9"

def dump( jsonData ):
    print ('result=' + str(jsonData))
    print(json.JSONEncoder().encode(result))
	
clarifai_api = ClarifaiApi()  # assumes environment variables are set.
result = clarifai_api.tag_image_urls('https://oxfordportal.blob.core.windows.net/vision/Analysis/3.jpg')

print ('result=' + str(result))
print ("testing")
dump( result)
print ("msft done")

# URL direction to image
#urlImage = "https://raw.githubusercontent.com/oakhillroboticmakerlabs/CVfirstSample/master/samples/commonObstacles/bigObstacle4.jpg"
# urlImage = 'https://oxfordportal.blob.core.windows.net/vision/Analysis/3.jpg'
#urlImage = "https://raw.githubusercontent.com/oakhillroboticmakerlabs/CVfirstSample/master/samples/Label4-Yellow-True.PNG"
# urlImage = "https://raw.githubusercontent.com/oakhillroboticmakerlabs/CVfirstSample/master/samples/commonObstacles/farm.jpg"
# urlImage = "https://raw.githubusercontent.com/oakhillroboticmakerlabs/CVfirstSample/master/samples/commonObstacles/river2.jpg"
#rlImage = "https://raw.githubusercontent.com/oakhillroboticmakerlabs/CVfirstSample/master/samples/commonObstacles/boatFront2.jpg"
#urlImage = "https://raw.githubusercontent.com/oakhillroboticmakerlabs/CVfirstSample/master/samples/commonObstacles/dam_obstacle.jpg"
urlImage = "https://raw.githubusercontent.com/oakhillroboticmakerlabs/CVfirstSample/master/samples/commonObstacles/little-river.jpg"

print('analyzing urlImage= '+urlImage)
# Computer Vision parameters


print("tags")
result = clarifai_api.tag_image_urls(urlImage)
dump(result)
print("color")
result = clarifai_api.color_urls('http://www.clarifai.com/img/metro-north.jpg')
dump(result)

if result is not None:
	print('writing result to file!')
	f0 = open('result.json', 'w')
	f0.write(str(result))
	f0.close()
    # Load the original image, fetched from the URL
	arr = np.asarray( bytearray( requests.get( urlImage ).content ), dtype=np.uint8 )
	# print('writing arr ')
	# img = cv2.cvtColor( cv2.imdecode( arr, -1 ), cv2.COLOR_BGR2RGB )
	f = open('arr', 'w')
	f.write(arr)
	f.close()


print(json.JSONEncoder().encode(result))