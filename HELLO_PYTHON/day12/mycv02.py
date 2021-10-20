import cv2

image = cv2.imread("C:/Users/zeroc/git/Python_Study/HELLO_PYTHON/day12/r.png",cv2.IMREAD_COLOR)

grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# r

# [[[ 36  28 237]
#   [ 36  28 237]]

#  [[ 36  28 237]
#   [ 36  28 237]]]

# g

# [[[ 76 177  34]
#   [ 76 177  34]]

#  [[ 76 177  34]
#   [ 76 177  34]]]

# b

# [[[192  82  60]
#   [204  72  63]]

#  [[204  72  63]
#   [204  72  63]]]



cv2.imshow("image",grayImage)

cv2.waitKey(0)
cv2.destroyAllWindows()