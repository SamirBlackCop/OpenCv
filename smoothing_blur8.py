import cv2
import numpy as np
# All this filters are effective in different type of Images

img = cv2.imread("saltAndwater.png", 1)

kernal = np.ones((5,5), np.float32)/25
kernal1 = np.ones((2,2), np.uint8)

# cv2.filter2D is used for homogeneous filter
dat = cv2.filter2D(img, -1, kernal)
dat1 = cv2.filter2D(img, -1, kernal1)

# gaussian_blur
gaussian_blur = cv2.GaussianBlur(img, (5,5), 0)

# salt & paer filter
median = cv2.medianBlur(img, 5)

# bilateral filter
bilateral = cv2.bilateralFilter(img, 9, 75, 75)


cv2.imshow("original", img)
cv2.imshow("homo", dat)
cv2.imshow("homoWith new kernal", dat1)
cv2.imshow("gaussian_blur", gaussian_blur)
cv2.imshow("median", median)
cv2.imshow("bilateral", bilateral)




cv2.waitKey(0)
cv2.destroyAllWindows()