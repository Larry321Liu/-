# 灰度化
import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2gray


img = cv2.imread("lenna.png")
h,w = img.shape[:2]   # 获取图片的高和宽
img_gray = np.zeros([h,w],img.dtype)  #创建一张和当前图片大小一样的单通道图片
for i in range(h):
    for j in range(w):
        m = img[i,j]    #取出当前high和wide中的BGR坐标
        img_gray[i,j] = int(m[0]*0.11 + m[1]*0.59 + m[2]*0.3)  #将B(0.11)G(0.59)R(0.3)坐标转化为gray坐标并赋值给新图像

plt.subplot(221)  # subplot(m,n,p) 将当前图窗划分为 m×n 网格，并在 p 指定的位置创建坐标区。
img = plt.imread("lenna.png")
plt.imshow(img)  # plt.imshow(img)用于接收和处理图像，但无法显示图像


img_gray = rgb2gray(img)
plt.subplot(222)
plt.imshow(img_gray,cmap = "gray")

# 二值化
rows,cols = img_gray.shape
for i in range(rows):
    for j in range(cols):
        if(img_gray[i,j] <= 0.5):
            img_gray[i,j] = 0
        else:
            img_gray[i,j] = 1
# img_binary = np.where(img_gray >= 0.5,1,0)


plt.subplot(223)
plt.imshow(img_gray,cmap = 'gray')
plt.show()