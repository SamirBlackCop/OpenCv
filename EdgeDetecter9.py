import cv2
img = cv2.imread('lena.jpg', 1)

canny = cv2.Canny(img, 150, 250)


cv2.imshow("original", img)
cv2.imshow("canny", canny)


cv2.waitKey(0)
cv2.destroyAllWindows()