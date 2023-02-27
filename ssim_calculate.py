import cv2
from skimage.metrics import structural_similarity
import time
import numpy as np

start = time.time()
# 读入图像，转为灰度图像
# src = cv2.imread('static/images/demo/gt_ed/14.jpg')
# src = cv2.imread('static/images/demo/gt_ed/13.jpg')
# src = cv2.imread('static/images/demo/gt_ed/17.jpg')
# src = cv2.imread('static/images/demo/gt_ed/18.jpg')
# src = cv2.imread('static/images/demo/gt_ncr/14.jpg')
# src = cv2.imread('static/images/demo/gt_ncr/13.jpg')
# src = cv2.imread('static/images/demo/gt_ncr/17.jpg')
src = cv2.imread('static/images/demo/gt_ncr/18.jpg')
img = cv2.imread('static/images/demo/ET-T2-100.jpg')
grayA = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 计算两个灰度图像之间的结构相似度
(score, diff) = structural_similarity(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
cv2.namedWindow("diff", cv2.WINDOW_NORMAL)
cv2.imshow("diff", diff)
print("SSIM:{}".format(score))
