import cv2

image = cv2.imread("C:/Users/zeroc/git/Python_Study/HELLO_PYTHON/day12/rena.jpg",cv2.IMREAD_COLOR)

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print(grayImage)

# gray

# [[161 162 163 ... 169 154 127]
#  [162 162 162 ... 171 157 130]
#  [162 162 162 ... 169 156 128]
#  ...
#  [ 44  41  53 ... 102 100 100]
#  [ 43  41  57 ... 104 106 106]
#  [ 44  42  57 ... 102 108 109]]

cv2.imshow("image",grayImage)

cv2.waitKey(0)
cv2.destroyAllWindows()