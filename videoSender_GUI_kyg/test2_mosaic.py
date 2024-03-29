import cv2

# 이미지 로드
image = cv2.imread("mask1.jpg")

# 모자이크 처리할 영역 좌표
x, y, w, h = 100, 100, 200, 200

# 모자이크 처리할 영역 추출
roi = image[y:y+h, x:x+w]

# 추출한 영역 축소 후 확대 (모자이크 효과)
factor = 10
small_roi = cv2.resize(roi, (w // factor, h // factor))
mosaic_roi = cv2.resize(small_roi, (w, h), interpolation=cv2.INTER_NEAREST)

# 모자이크 처리된 영역을 원본 이미지에 적용
image[y:y+h, x:x+w] = mosaic_roi

# 결과 이미지 출력
cv2.imshow("Mosaic Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()