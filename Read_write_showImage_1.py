import cv2
img = cv2.imread("lena.jpg", 0)
#  imread is to read the image and there is three flag as 0,1,-1
# 0=load img as grayscale
# 1=load img as colors
# -1= load img as it is
print(img)

cv2.imshow("image_show", img)
#image_show is the name of window where img will show
cv2.waitKey(5000)
# it will hold the img till 5 sec if you put 0 instead of 5000 it'll show until you cut it

#imwrite will create a copy of the given image
cv2.imwrite("lena_copy.png", img)

# after every operation use this command line
cv2.destroyAllWindows()
