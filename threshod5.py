import cv2
import numpy as np

img  = cv2.imread('gradient.png', 0)

_, thi = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  #  127 is the threshold parameter

cv2.imshow("Image", img)
cv2.imshow("Image", thi)


print(_)
print(thi)

cv2.waitKey(0)
cv2.destroyAllWindows()