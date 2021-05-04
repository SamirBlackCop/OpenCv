import cv2
img = cv2.imread('OpenCV_Logo.png', 1)
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imggray, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print(len(contours))


cv2.drawContours(img, contours, -1, (0, 255, 255), 3)    # -1 will draw all contours
cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()