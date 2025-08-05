import cv2 as cv

img=cv.imread("img.jpg")
cv.imshow("Display window", img)
k = cv.waitKey(5000) # Wait for a keystroke in the window