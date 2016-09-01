from __future__ import print_function
import time 
import requests
import operator
import json
import numpy as np

# Python Image Testing Example 
# Variables

_url = 'https://api.projectoxford.ai/vision/v1/analyses'
_key = '08284d968e4742b098a136ecfe11e436' #Here you have to paste your primary key
_maxNumRetries = 1
print ("key="+ _key)
def processRequest( json, data, headers, params ):

    """
    Helper function to process the request to Project Oxford

    Parameters:
    json: Used when processing images from its URL. See API Documentation
    data: Used when processing image read from disk. See API Documentation
    headers: Used to pass the key information and the data type request
    """

    retries = 0
    result = None

    while True:

        response = requests.request( 'post', _url, json = json, data = data, headers = headers, params = params )

        if response.status_code == 429: 

            print( "Message: %s" % ( response.json()['error']['message'] ) )

            if retries <= _maxNumRetries: 
                time.sleep(1) 
                retries += 1
                continue
            else: 
                print( 'Error: failed after retrying!' )
                break

        elif response.status_code == 200 or response.status_code == 201:

            if 'content-length' in response.headers and int(response.headers['content-length']) == 0: 
                result = None 
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str): 
                if 'application/json' in response.headers['content-type'].lower(): 
                    result = response.json() if response.content else None 
                elif 'image' in response.headers['content-type'].lower(): 
                    result = response.content
        else:
            print( "Error code: %d" % ( response.status_code ) )
            print( response.content )
            print( "Message: %s" % ( response.json()['error']['message'] ) )
			
        break
        
    return result
	

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
params = { 'visualFeatures' : 'Color,Categories,Description,Tags,ImageType'} 

headers = dict()
headers['Ocp-Apim-Subscription-Key'] = _key
headers['Content-Type'] = 'application/json' 

json = { 'url': urlImage } 
data = None

result = processRequest( json, data, headers, params )

print(result)

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
	print('writing img to file!')
	# f.close()
	# f2 = open('img', 'w')
	# f2.write(img)
	# f2.close()

print(json.JSONEncoder().encode(result))