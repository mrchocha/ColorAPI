# ColorAPI
Small API project to detect the dominant color and border color of the given image


# Tools And Technology used
- Django-rest framework
- OpenCV
- Canny edge detection
- Numpy

# How to Use?
You need to request the api with image link as
```
GET: /api/url_location_of_image
``` 

i.e
```
GET:  /api/https://storage.googleapis.com/bizupimg/profile_photo/Screenshot%202020-08-16%20at%205.02.30%20PM%20-%20Nikunj%20Daruka.png
```

# How ot Works?
- First of all you need to know that we an represent the image as matrix of some pixels 
- Each pixel represents the specific RGB value 

## For Primary color detection
- To detect primary color, I have found the frequency of each unique pixel.
- The most frequent one will be our primary color of the image.

## For Border color detection
- To detect the edge, I have first converted the color image to gray scale image.
- Then performed the Canny edge detection
- After that i have stored each index of matrix (image) with value 255 (white color) that represents the edge.
- Then found pixel that are at stored indices
- At the end find the frequency of all unique selected pixels and return the most frequent one.


# Thank you