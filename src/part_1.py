import os
import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

output_dir = "./out"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

i = 1

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
        cv.imwrite(f"./{output_dir}/image{i}.jpg", frame)
        i = i + 1
    elif key == ord("q"):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
