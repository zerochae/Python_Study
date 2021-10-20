import cv2
import imutils
from PIL import ImageFont
import os

image = cv2.imread("C:/Users/zeroc/git/Python_Study/HELLO_PYTHON/day12/rena.jpg",cv2.IMREAD_COLOR)

	# 폰트 색상 지정
blue = (255, 0, 0)
green= (0, 255, 0)
red= (0, 0, 255)
white= (255, 255, 255) 
# 폰트 지정
font =  cv2.FONT_HERSHEY_PLAIN

fontfolder = "C:/WINDOWS/FONTS/"
selectfont = ImageFont.truetype(os.path.join(fontfolder,'ARIAL.TTF'))
 
# 이미지에 글자 합성하기
img = cv2.putText(image, "zerochae", (350, 40), selectfont, 2, blue, 1, cv2.LINE_AA)
 
# 이미지 보여주고 창 끄기

cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()