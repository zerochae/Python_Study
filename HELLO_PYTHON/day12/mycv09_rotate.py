import cv2

image = cv2.imread("C:/Users/zeroc/git/Python_Study/HELLO_PYTHON/day12/rena.jpg",cv2.IMREAD_COLOR)


height, width, channel = image.shape
matrix = cv2.getRotationMatrix2D((width/2,height/2),45,1)
dst = cv2.warpAffine(image,matrix,(width,height))

cv2.imshow("image",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()