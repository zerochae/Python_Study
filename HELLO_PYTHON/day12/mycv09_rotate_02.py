import cv2

image = cv2.imread("C:/Users/zeroc/git/Python_Study/HELLO_PYTHON/day12/rena.jpg",cv2.IMREAD_COLOR)

rotate = cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE);

cv2.imshow("image",rotate)

cv2.imwrite("C:/Users/zeroc/git/Python_Study/HELLO_PYTHON/day12/rena2.jpg",rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()