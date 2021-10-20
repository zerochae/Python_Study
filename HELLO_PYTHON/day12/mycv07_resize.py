import cv2

image = cv2.imread("C:/Users/zeroc/git/Python_Study/HELLO_PYTHON/day12/rena.jpg",cv2.IMREAD_COLOR)

resize = cv2.resize(image,(100,50))
resize2 = cv2.resize(image, dsize=(0,0),fx=0.3,fy=0.7,interpolation=cv2.INTER_AREA)

cv2.imshow("image",resize2)

cv2.waitKey(0)
cv2.destroyAllWindows()