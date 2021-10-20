import cv2
import imutils

image = cv2.imread("C:/Users/zeroc/git/Python_Study/HELLO_PYTHON/day12/rena.jpg",cv2.IMREAD_COLOR)

trns = imutils.translate(image,25,-75)
rotat = imutils.rotate(image,45,(0,0))
resz = imutils.resize(image,100)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

canny = imutils.auto_canny(image)

url = "https://www.google.co.kr/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png"
dst = imutils.url_to_image(url)

cv2.imshow("image",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()