import cv2

image = cv2.imread("C:/Users/zeroc/git/Python_Study/HELLO_PYTHON/day12/rena.jpg",cv2.IMREAD_COLOR)
print(image)

cv2.imshow("image",image)

cv2.waitKey(0)
cv2.destroyAllWindows()