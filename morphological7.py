import cv2
import numpy as np

img = cv2.imread("smarties.png", 0)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

# dilation (morphological operation always works on binary image so use threshold)
kernal = np.ones((2,2), np.uint8) # it is a 2x2 matrix it is applied on where is black dot appear on image you can use custome matrix
dialation = cv2.dilate(mask, kernal)
dialation_itr  =  cv2.dilate(mask, kernal, iterations=2)



# erosion
erosion= cv2.erode(mask, kernal, iterations=1)

# opening
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)


# closing
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)


cv2.imshow("maks", mask) # in simg there is black dot in img to remove this from img we use dilasion technique
cv2.imshow("original", img)
cv2.imshow("dilate", dialation)
cv2.imshow("dilate_iter", dialation_itr)
cv2.imshow("erosion", erosion)
cv2.imshow("opening", opening)
cv2.imshow("closing", closing)



cv2.waitKey(0)
cv2.destroyAllWindows()