import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from PIL import Image


def BGR_to_RGB(cvimg):
    pilimg = cvimg.copy()
    pilimg[:, :, 0] = cvimg[:, :, 2]
    pilimg[:, :, 2] = cvimg[:, :, 0]
    return pilimg

'''
data = np.load("static/images/demo/img_t2/T2-17.npy", allow_pickle=True)
# data = np.load("static/images/demo/img_t2/T1-18.npy", allow_pickle=True)
# data = np.load("img_t2/FeTS21_Training_124_100.npy", allow_pickle=True)
# data = np.load("img_t2/FeTS21_Training_213_100.npy", allow_pickle=True)
# data = np.load("img_t2/FeTS21_Training_196_100.npy", allow_pickle=True)
plt.imshow(data)              #执行这一行后并不会立即看到图像，这一行更像是将depthmap载入到plt里
plt.xticks([])  # 去掉x轴
plt.yticks([])  # 去掉y轴
plt.axis('off')  # 去掉坐标轴
# plt.colorbar()                   #添加colorbar
plt.savefig('T2-17.jpg')       #执行后可以将文件保存为jpg格式图像，可以双击直接查看。也可以不执行这一行，直接执行下一行命令进行可视化。但是如果要使用命令行将其保存，则需要将这行代码置于下一行代码之前，不然保存的图像是空白的
# plt.savefig('T2-14.jpg') 
# plt.savefig('T2-17.jpg') 
# plt.savefig('T2-18.jpg') 
plt.show()                        #在线显示图像
'''



# image = mpimg.imread('static/images/demo/img_t1/T1-14.jpg')
# image = mpimg.imread('static/images/demo/img_t1/T1-13.jpg')
# image = mpimg.imread('static/images/demo/img_t1/T1-17.jpg')
# image = mpimg.imread('static/images/demo/img_t1/T1-18.jpg')
# image = mpimg.imread('static/images/demo/img_t2/T2-13.jpg')
# image = mpimg.imread('static/images/demo/img_t2/T2-14.jpg')
# image = mpimg.imread('static/images/demo/img_t2/T2-17.jpg')
image = mpimg.imread('static/images/demo/img_t2/T2-18.jpg')
# image = mpimg.imread('static/images/demo/T2-100_.jpg')
# image = Image.open('static/images/demo/T2-100_.jpg')

# image.flags.writeable = True  # 将数组改为读写模式`
# Image.fromarray(np.uint8(image))
img1 = image.copy()
img2 = image.copy()
# mask1 = mpimg.imread('static/images/demo/gt_ed/14.jpg')
# mask2 = mpimg.imread('static/images/demo/gt_ncr/14.jpg')
# mask1 = mpimg.imread('static/images/demo/gt_ed/13.jpg')
# mask2 = mpimg.imread('static/images/demo/gt_ncr/13.jpg')
# mask1 = mpimg.imread('static/images/demo/gt_ed/17.jpg')
# mask2 = mpimg.imread('static/images/demo/gt_ncr/17.jpg')
mask1 = mpimg.imread('static/images/demo/gt_ed/18.jpg')
mask2 = mpimg.imread('static/images/demo/gt_ncr/18.jpg')
# mask1 = mpimg.imread('static/images/demo/ET-T2-100.jpg')
# mask1 = Image.open('static/images/demo/ET-T2-100.jpg')

img1[:,:,:][mask1[:,:,:]>=[200,200,200]] = 255
img2[:,:,:][mask2[:,:,:]>=[200,200,200]] = 255
img1 = BGR_to_RGB(img1)
img2 = BGR_to_RGB(img2)

#  cv2.imwrite('static/images/demo/final/ED-14-T1.jpg',img1)
#  cv2.imwrite('static/images/demo/final/NCR-14-T1.jpg',img2)
#  cv2.imwrite('static/images/demo/final/ED-13-T1.jpg',img1)
#  cv2.imwrite('static/images/demo/final/NCR-13-T1.jpg',img2)
#  cv2.imwrite('static/images/demo/final/ED-17-T1.jpg',img1)
#  cv2.imwrite('static/images/demo/final/NCR-17-T1.jpg',img2)
#  cv2.imwrite('static/images/demo/final/ED-18-T1.jpg',img1)
#  cv2.imwrite('static/images/demo/final/NCR-18-T1.jpg',img2)
#  cv2.imwrite('static/images/demo/final/ED-14-T2.jpg',img1)
#  cv2.imwrite('static/images/demo/final/NCR-14-T2.jpg',img2)
#  cv2.imwrite('static/images/demo/final/ED-13-T2.jpg',img1)
#  cv2.imwrite('static/images/demo/final/NCR-13-T2.jpg',img2)
#  cv2.imwrite('static/images/demo/final/ED-17-T2.jpg',img1)
#  cv2.imwrite('static/images/demo/final/NCR-17-T2.jpg',img2)
cv2.imwrite('static/images/demo/final/ED-18-T2.jpg',img1)
cv2.imwrite('static/images/demo/final/NCR-18-T2.jpg',img2)
# cv2.imwrite('static/images/demo/ET-22-T2.jpg',img1)


