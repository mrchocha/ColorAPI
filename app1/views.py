from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests
import shutil
import cv2 
import numpy as np
import os

# function to convert the rgb value to hex
def rgb2hex(r,g,b):
    return '#%02x%02x%02x' % (r, g, b)

# function for getting the primary color
def getPrimaryColor(img):
    
    #find the frequency of each unique color
    unique_colors,count_of_color=np.unique(img.reshape(-1,3),axis=0,return_counts=True)
    
    #find the hec code color with maximum freqency that will be the primary color of image
    r,g,b=unique_colors[np.argmax(count_of_color)]
    return rgb2hex(r,g,b)


#function for getting border color 
def getBorderColor(img):
    #convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #perform canny edge detection on the image
    edges = cv2.Canny(gray,100,200)

    #find the no. rows and  no. columns image(matrix of pixels)
    rows,cols=edges.shape[0],edges.shape[1]
    indices=[]
    
    #find the indices of gray image where pixel value is 1 (which will represent the edge in photo)
    for i in range(0,rows):
        for j in range(0,cols):
            if (edges[i,j]==255):
                #find pixel value on equivalent index in original image
                indices.append(img[i,j])
    indices=np.array(indices)

    #count the frequency of each chosen pixel
    unique,count=np.unique(indices.reshape(-1,3),axis=0,return_counts=True)
    
    #find the hec code color with maximum freqency that will e the border color
    r,g,b=unique[np.argmax(count)]
    return rgb2hex(r,g,b)

#function to accept the get request
@api_view(['GET'])
def Home(request,img_url):
    #detect if file is png,jpg or jpeg and create the file name to download the data
    file_name="img."+img_url.split(".")[-1]

    #get the data from given url find the store response
    res=requests.get(img_url,stream=True)

    #if url is not acceptable 
    if(res.status_code!=200):
        return Response({"Status":"Some thing went wrong! Please check the URL"},status=status.HTTP_400_BAD_REQUEST)
    
    #store the  data in file
    with open(file_name, 'wb') as out_file:
        shutil.copyfileobj(res.raw, out_file)
    
    #read the image file as matrix of pixels
    img = cv2.imread(file_name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #delete the file
    os.remove(file_name)

    #return the response
    return Response(
        {
            "dominant_color": getPrimaryColor(img),
            "logo_border": getBorderColor(img),
        })