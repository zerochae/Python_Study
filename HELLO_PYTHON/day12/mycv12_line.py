import cv2

image = cv2.imread("C:/Users/zeroc/git/Python_Study/HELLO_PYTHON/day12/rena.jpg",cv2.IMREAD_COLOR)
print(image)


cv2.line(image, (30,30),(200,30),(0,0,255),5)

cv2.imshow("image",image)

cv2.waitKey(0)
cv2.destroyAllWindows()