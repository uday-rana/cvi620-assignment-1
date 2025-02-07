# This is combined version of the part 3 and it runs with part 3 version 2
# Version 2 includes whe actual image(.jpg) files is loaded
# and displayed, with green rectangle , thickness to -1(filled)
# and text in the rectangle in the end of part 3
# you can also checkout whole process of doing part 3 in part3.ipynb


# https://matplotlib.org/stable/gallery/shapes_and_collections/compound_path.html#sphx-glr-gallery-shapes-and-collections-compound-path-py
# imports
import cv2
import matplotlib.pyplot as plt
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Build the path to the image
img_path = os.path.join(script_dir, "Lucy2.jpg")

# Load the image with error checking
img = cv2.imread(img_path)
if img is None:
    raise FileNotFoundError(f"Could not load image: {img_path}")

# Turning BGR to RGB color schema
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# lets put a text in the rectangle
text = "Sangjune"
# set the font
font = cv2.FONT_HERSHEY_SIMPLEX
# set the font size
font_size = 1
# set the color
color = (0, 0, 255)
# set the thickness
thickness = 2
# put the text on the image
rectangle = cv2.rectangle(img, (100, 100), (300, 200), (0, 255, 0), thickness=-1)
rectangle = cv2.putText(img, text, (100, 150), font, font_size, color, thickness)
# display the image
plt.imshow(img)
plt.show()
