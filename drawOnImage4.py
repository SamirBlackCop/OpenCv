import cv2
img = cv2.imread('lena.jpg', 1)
img = cv2.line(img, (0,0), (255,255), (255, 0, 0), 5)  # if you provide thickness as -1 then the area will fill with the color

#img = cv2.arrowedLine(img, (0,0), (255,255), (255, 0, 0), 5)  will create an array
#img = cv2.rectangle(img, (0,0), (255,255), (255, 0, 0), 5)

font= cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (10, 500), font, 4, (0, 255, 255), 10, cv2.LINE_AA)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()