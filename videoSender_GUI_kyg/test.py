import cv2
import numpy as np




src = cv2.imread("iu.png", cv2.IMREAD_ANYCOLOR)
glasses = cv2.imread("glasses.png", cv2.IMREAD_ANYCOLOR)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eyes_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

# ret, frame =
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 2)     # 불러온 데이터 기반으로 객체 검출
eyes = eyes_cascade.detectMultiScale(gray, 1.3, 2)     # 불러온 데이터 기반으로 객체 검출

fx, fy, fw, fh = 0, 0, 0, 0
for (x, y, w, h) in faces:
    cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 사각형 범위
    fx, fy, fw, fh = x,y,w,h
dst = cv2.resize(glasses, dsize=(fw+90, fh-80))

g_gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
th = cv2.threshold(g_gray, 1, 255, cv2.THRESH_BINARY_INV)[1]


ex1, ey1, ew1, eh1 = 999999, 0, 0, 0
for (ex, ey, ew, eh) in eyes:
    print(ex, ey, ew, eh)
    if ex1 > ex:
        ex1, ey1, ew1, eh1,  = ex, ey, ew, eh
    cv2.rectangle(src, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)


print(ex1, ey1, ew1, eh1)
slice_img = src[ey1-10:ey1 + eh1+10, fx:fx + fw]


cv2.imshow("test", slice_img)
cv2.imshow("안경", glasses)
cv2.imshow("아이유", src)
cv2.waitKey()
