"""
This is combined version of the part 3 and it runs with part 3 version 2.

Version 2 includes when actual image(.jpg) files is loaded
and displayed, with green rectangle, thickness to -1(filled)
and text in the rectangle in the end of part 3.
You can also checkout whole process of doing part 3 in part3.ipynb.
"""

import os

import cv2
import matplotlib.pyplot as plt


# Constants
TEXT = "Sangjune"
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SIZE = 1
TEXT_COLOR = (0, 0, 255)  # Red in RGB
TEXT_THICKNESS = 2
RECT_COLOR = (0, 255, 0)  # Green in RGB


def main():
    """Main function to process and display the image."""
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

    # Draw rectangle and add text
    cv2.rectangle(img, (100, 100), (300, 200), RECT_COLOR, thickness=-1)
    cv2.putText(img, TEXT, (100, 150), FONT, FONT_SIZE, TEXT_COLOR, TEXT_THICKNESS)

    # Display the image
    plt.imshow(img)
    plt.show()


if __name__ == "__main__":
    main()
