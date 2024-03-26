import cv2          # opencv-python
import numpy as np

image_path = "samoyed.png"
image_array = cv2.imread(image_path)    # cv2 영상처리 패키지
# imread : image read (이미지경로) image_array에 데이터 저장
print(image_array)
print(image_array.shape)
print(image_array.size)


# x = 1
# y = 1
# pix_v = image_array[y,x]
# print("value", pix_v)


height, width, _ = image_array.shape
print(height)
print(width)
print(_)    # 채널 : B G R

# widthHalf = width // 2
# image_array[:,:widthHalf] = [0,0,0]
cv2.imshow("image result", image_array)
cv2.waitKey(0)
cv2.destroyAllWindows()

# opencv로 불러온 이미지는 numpy배열 형태의 픽셀에 해당되는 B G R 가진다.


















