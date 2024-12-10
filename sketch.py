import numpy as np
import imageio
import scipy.ndimage
import cv2

# Path to the input image
img = "hanuman2.jpg"

# Function to convert an RGB image to grayscale
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

# Function to blend images for sketch effect
def dodge(front, back):
    final_sketch = front * 255 / (255 - back)
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255
    return final_sketch.astype('uint8')

# Read the input image (original image remains untouched)
original_image = imageio.imread(img)

# Convert the image to grayscale
gray = rgb2gray(original_image)

# Invert the grayscale image
inverted = 255 - gray

# Apply Gaussian blur to the inverted image
blurred = scipy.ndimage.gaussian_filter(inverted, sigma=15)

# Create the sketch by blending the blurred and grayscale images
sketch = dodge(blurred, gray)

# Save the sketch image as a new file
cv2.imwrite("hanuman2-sketch.jpg", sketch)
