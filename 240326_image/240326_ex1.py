import cv2

src = cv2.imread("dog.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

blur = cv2.blur(gray, (5,5), anchor=(-1,-1), borderType=cv2.BORDER_DEFAULT)

ret, dst = cv2.threshold(blur, 167, 255, cv2.THRESH_BINARY)


cv2.imshow("blur", blur)
cv2.imshow("result", dst)
cv2.waitKey()

# 커널은 이미지에서 특정 픽셀 spot (x,y)의 주변 일정 범위 박스 공간
# 신호처리 분야에서 커널은 필터라고 부름

# anchor 포인트 (고정점)
# 고정점은 커널을 통해 컨벌루션된 값을 할당한 지점
# 컨벌루션 : 새로운 픽셀을 만들어 낼 때 커널의 크기의 화소 값을 이용해서 어떤 시스템(함수)를 통과시켜 계산하는 행위를 의미
# 커널 내 고정점은 하나의 포인트이다.
