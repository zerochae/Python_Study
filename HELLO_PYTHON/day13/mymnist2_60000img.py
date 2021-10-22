# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import cv2
# MNIST 데이터셋 불러오기
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# image = cv2.imread(train_images[0][0],cv2.COLOR_BGR2GRAY)


for index,item in enumerate(train_images) :
    cv2.imwrite("C:/Users/zeroc/git/Python_Study/HELLO_PYTHON/day13/images/{}/{}.png".format(train_labels[index],index),item)

# grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# cv2.imshow("image",image)

cv2.waitKey(0)
cv2.destroyAllWindows()