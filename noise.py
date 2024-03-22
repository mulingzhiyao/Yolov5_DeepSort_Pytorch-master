import cv2
import random

img = cv2.imread('1.jpg', 1)
imgInfo = img.shape
height = imgInfo[0] - 1  # 防止越界
width = imgInfo[1] - 1

temp = 500  # 噪声点的个数
for i in range(0, temp):
    if random.randint(1, temp) % 2 == 0:
        img[random.randint(0, height), random.randint(0, width)] = (255, 255, 255)
    if random.randint(1, temp) % 2 != 0:
        img[random.randint(0, height), random.randint(0, width)] = (0, 0, 0)
cv2.imshow('dst', img)
cv2.imwrite('noise.jpg', img)

cv2.waitKey(0)