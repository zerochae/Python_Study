import cv2

image = cv2.imread("C:/Users/zeroc/git/Python_Study/HELLO_PYTHON/day12/rena.jpg",cv2.IMREAD_COLOR)

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("C:/Users/zeroc/git/Python_Study/HELLO_PYTHON/day12/grey_rena.png",grayImage)

cv2.waitKey(0)
cv2.destroyAllWindows()