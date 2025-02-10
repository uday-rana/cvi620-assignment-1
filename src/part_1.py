"""
CVI620 Assignment 1 Part 1
Uday Rana
"""

import os
import sys

import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    sys.exit("Cannot open camera")

OUTPUT_DIR = "./out"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


def get_unique_filename(directory, base_name, extension):
    """Creates a unique filename by appending a number counter before the file extension"""
    counter = 1
    while True:
        new_filename = f"{base_name}{counter}{extension}"
        filepath = os.path.join(directory, new_filename)
        if not os.path.exists(filepath):
            return filepath
        counter += 1


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv.imshow("Photo Booth", frame)
    key = cv.waitKey(1)

    if key == ord("s"):
        filename = get_unique_filename(OUTPUT_DIR, "image", ".jpg")
        cv.imwrite(filename, frame)
    elif key == ord("q"):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
