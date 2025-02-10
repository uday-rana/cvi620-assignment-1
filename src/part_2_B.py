import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    # Read the first image
    img1 = cv2.imread('../img/cat.jpeg')
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

    # Read the second image
    img2 = cv2.imread('../img/Dog and Cat.jpg')
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    # Print original dimensions
    print("Image 1 dimensions:", img1.shape)
    print("Image 2 dimensions:", img2.shape)

    # Resize img2 to match img1 dimensions
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    print("New image 2 dimensions:", img2.shape)

    # Display both original images side by side
    plt.figure(figsize=(15,5))
    plt.subplot(121)
    plt.imshow(img1)
    plt.title('Image 1')
    plt.axis('off')

    plt.subplot(122)
    plt.imshow(img2)
    plt.title('Image 2')
    plt.axis('off')
    
    # Use plt.draw() and plt.pause() instead of plt.show()
    plt.draw()
    plt.pause(1.0)

    # Get alpha value from user
    alpha = float(input("\nEnter blend factor (0-1): "))

    # Linear blending using cv2.addWeighted
    blended = cv2.addWeighted(img1, 1-alpha, img2, alpha, 0)

    # Display blended result
    plt.figure(figsize=(10,8))
    plt.imshow(blended)
    plt.title(f'Blended Image (alpha={alpha})')
    plt.axis('off')
    plt.show()  # Keep the final show() to prevent window from closing

if __name__ == "__main__":
    main()
