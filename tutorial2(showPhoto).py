import cv2
import numpy as np
import random

img = cv2.imread('colorcolor.jpg')
# print(img.shape)

# img = np.empty((300, 300, 3), np.uint8)

# for row in range(300):
#     for col in range(img.shape[1]): #圖片寬度
#         img[row][col] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]//產生隨機顏色

newImg = img[0:650, 300:500]  # XY裁切橡素(左上基準:向外延伸像素)

cv2.imshow('img', img)
cv2.imshow('newImg', newImg)
cv2.waitKey(0)
