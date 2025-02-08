"""
CVI620 Assignment 1 Part 2
Uday Rana
"""

import sys

import cv2 as cv

# Part A - Brightness and Contrast

img = cv.imread("./img/cat.jpeg")

if img is None:
    sys.exit("Could not read the image.")

brightness_adjusted_img = cv.add(img, 100)
contrast_adjusted_img = cv.multiply(img, 1.9)

cv.imshow("Original image", img)
cv.imshow("Brightness-adjusted image", brightness_adjusted_img)
cv.imshow("Contrast-adjusted image", contrast_adjusted_img)
cv.waitKey(0)
