import cv2
# capture = cv2.VideoCapture("dog_video.mp4")
# while cv2.waitKey(30) < 0:
#     if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):   # 현재 프레임이 마지막 프레임이라면
#         capture.set(cv2.CAP_PROP_POS_FRAMES, 0) # 처음 프레임으로 돌아가기
#         # => 반복재생
#
#         # 조건문 : 전체 프레임 카운트와 현재 프레임 카운트가 같다면 (== 영상 끝)
#         # cpature.set(cv2.CAP_PROP_POS_FRAME 을 0으로 설정
#     ret, frame = capture.read()
#     cv2.imshow("frame", frame)
#
# capture.release()
# cv2.destroyAllWindows(






# src = cv2.imread("samoyed.png", cv2.IMREAD_COLOR)
# height, width, chanel = src.shape
# matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)    # 이미지 회전
# # (기준(중앙점), 각도, 크기(배수))
#
# dst = cv2.warpAffine(src, matrix, (width, height))
# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()
#
# getRotationMatrix2D함수는 이미지 회전 확대 기능 / 필터 기능 (속성 설정만 함)
# 중심점(축) : w/2, h/2
# warpAffine(원본이미지, matrix(필터), 출력이미지 사이즈) 함수는 매개변수로 회전 마스크 matrix를 넣어줌 (설정한 속성을 대상 이미지에 적용)
# 아핀(warpAffine) 변환함수:
# 원본이미지 (src)에 matrix를 적용하고
# 출력이미지 사이즈를 dsize로 width, height 원본 사이즈 동일하게 변형하는 작업
# 아핀 맵 행렬에 따라 회전된 이미지를 반환한다.


# 영상/이미지 처리에서 확대/축소를 업샘플링/다운 샘플링으로 표현
# 업샘프링 : 원본 이미지 크기 확대
# 다운샘프링 : 원본 이미지 크기 축소


# src = cv2.imread('samoyed.png', cv2.IMREAD_COLOR)
# height, width, chanel = src.shape
# dst = cv2.pyrUp(src, dstsize=(width*2, height*2), borderType=cv2.BORDER_DEFAULT)
# # pyrUP : 업샘플링 함수 : 이미지 확대, 확대에는 dstsize로 확대 배율 설정(튜플형태)
# #borderType 매개변수 :
# # cv2.BORDER_DEFALT : 기본값
# # cv2.BORDER_CONSTANT : 픽셀 채우기
# # cv2.BORDER_REFLECT : 경계 기준 이미지 반사 채우기
# # cv2.BORDER_REFLECT_101 : 경계 기준 이미지 반사 채우기, 경계 픽셀 제외
# # 이미지 연산 중 이미지 경계 처리 방법 지정하는 속성
#
# dst2 = cv2.pyrDown(src)
# # pyrDOWN : 다운샘플링 함수 : 이미지 축소, 고정적으로 절반으로 축소함
#
# reflected_src = cv2.copyMakeBorder(src, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
# # copyMakeBorder 함수 : 테두리 두께 설정 및 테두리 속성 설정
# cv2.imshow('ref', reflected_src)
#
# cv2.imshow('src', src)
# cv2.imshow("up", dst)
# cv2.imshow("down", dst2)
# cv2.waitKey()
# cv2.destroyAllWindows()









# # ROI 관심 구역 : Region Of Interest
# # R-CNN의 특징
# # 기존 CNN 신경만에 비해 속도가 매우 빠름.
# # 특정 구역을 지정해서 해당 구역에 대해서 신경망 처리
# # seg
# # 영상 처리시 객체 탐지 detect, 추척 tracking, 검출하는 영역을 관심 영역이라고 한다.
# # 특정 ROI 만 추출하여 해당 부분에만 영상처리를 적용해 빠르게 구동
# # 불필요한 부분 연산이 줄어 정확도, 속도 향상
#
#
# src = cv2.imread("samoyed.png", cv2.IMREAD_COLOR)
# roi1 = src[100:400,200:500]       # 색상 채널은 슬라이싱에서 제외
# # 복사
# cv2.imshow("src", src)
# cv2.imshow("dst", roi1)
# cv2.waitKey()




# # 복사의 종류
# lista = []
# listb = [1,2,3,4]
# listc = [1]
#
# listc.append(listb)
# print(listc)
#
# listc += listb
# print(listc)
#
# listc = [1,2,3]
# print(listc)
# def changList(list_x):
#     temp = list_x
#     list_x.append(10)
#     print("temp", temp)
#     print("list_x",list_x)
#
# changList(listc)
#
#
# # 깊은 복사 vs 얕은 복사
#
# # 파이썬의 객체는 immutable 객체와 mutable 객체로 나뉜다.
# # immutable 객체 : 값을 바꿀 수 없는 객체
# # mutable 객체 : 값을 바꿀 수 있는 객체
#
# # immutable 객체는 값이 바뀌면 다른 메모리 공간을 할당하여 주소값도 바뀜
# # mutable 객체는 주소값이 동일해도 그 안의 값 바꿀 수 있음
#
# # immutalbe : tuple, str, int, float, boolean
# # mutable : list, dict
#
# # mutable 객체를 변수에 대입할 때
# # ex) temp = list_x
# # def changList(list_x)
# # 이 때 실제 값이 복사되는 것이 아니라 참조 주소값만 복사된다.
# # 따라서 temp = list_x 를 해놔도 후에 list_x의 구성을 변경하면, temp 구성도 같이 바뀌게 된다.
#
# # 위 동일한 작업을 immutable 객체를 대상을 수행하면
# # ex) temp = src
# # 후에 src의 값 할당이 바뀌면 재할당이 이루어지며 메모리 주소가 변경된다.
# # 따라서 temp와 src는 다른 값을 가지게 된다.
#
#
# a = [1,2,3]
# b = a[:]
# print(id(a))
# print(id(b))
# print(a==b)
# print(a is b)
#
# a.append(10)
# print(a)
# print(b)
#
# # list 슬라이싱을 통한 새로운 값 할당
# # 슬라이싱을 통한 할당을 하면 새로운 id가 부여된다.
# # 서로 영향 없음
# # 슬라이싱은 얕은 복사(shallow copy)라고 한다.
#
#
# a = [[1,2], [3,4]]
# b = a[:]
# print(id(a))
# print(id(b))
# print(id(a[0]))
# print(id(b[0]))
#
# a[0] = [5,6]
# print(a)
# print(b)
# print(id(a[0]))
# print(id(b[0]))
#
#
# import copy
# a = [[1,2],[3,4]]
# b = copy.copy(a)
# a[1].append(5)
# print(a)
# print(b)
#
# #########################
# a = [[1,2],[3,4]]
# b = copy.deepcopy(a)
# a[1].append(5)
# print(a)
# print(b)

# 결론 : 대입 = 형태로 복사하면 원본도 영향 받는다.
#     : 원본을 변형하고 싶지 않으면 deepcopy() 사용










# # 영상 binary : 이진화 작업
# # 이진화 : 어느 value를 기준을 값이 높거나 낮은 픽실의 값을 특정 기준 값으로 변환
# # 일반적으로 검정 or 흰색의 값으로 변경
# # 기준 밸류에 따라 이분법적으로 구분하여, 픽섹을 T or F 로 나누는 연산이고,
# # 이미지 행렬(matrix)의 모든 픽셀에 대해 연산을 수행한다.
#
# # cv2.cvtColor(대상 이미지 객체, cv2.COLOR_BGR2GRAY)   # 그레이컬러 영상이 됨
# # cv2.threshold(그레이스케일 이미지 개체, threshV, maxV, cv2.THRESH_BINARY)
#
# src = cv2.imread("samoyed.png", cv2.IMREAD_COLOR)
# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# ret, dst = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)
# cv2.imshow("dst", dst)
# cv2.imshow("src", src)
# cv2.waitKey()
#
# # 220 이상 => 255 처리 / 220 미만 => 0 처리
# # thresh : 임계값
#
# # cv2.THRESH_BINARY : 임계값 초과시 maxValue 아닐 경우 0
# # cv2.THRESH_BINARY_INV : 임계값 초과시 0 아닐경우 maxValue
# # cv2.THRESH_TRUNC : 임계값 초과시 thresh 값으로, 아닐 경우 변형 없음
# # cv2.THRESH_TOZERO : 임계값 초과시 변형 X, 미만은 0 처리
#
# # RGB => GRAYSCALE 공식
# # 3채널 -> 1채널 변환
# # G = (0.299*R) + (0.587*G) + (0.114*B)
# # 0.299 + 0.587 + 0.114 = 1
# # 1채널 GRAY 값도 0~255






# blur : 흐리게 처리
# 흐림 효과, 블러링, 스무딩
# 블러는 영상의 샤프니스를 줄여 노이즈를 줄이는 작업이다.
# 원하는 객체 외 외부 영향 최소화 목적
# 블러는 영상이나 이미지를 번지게 처리함.
# 해당 픽셀과 주변 값들을 비교해서 게산한다.
# 노이즈 제거가 주 목적이고, 후 작업에 연산 속도 향상

src = cv2.imread('samoyed.png', cv2.IMREAD_COLOR)
dst = cv2.blur(src, (3, 3), anchor=(-1,-1), borderType=cv2.BORDER_DEFAULT)
# blur 함수로 블러처리 가능
# ksize : 커널의 크기 -> 주변의 픽셀 고려하는 범위 : 주로 홀수 단위로 설정
# anchor = (-1,-1) : 커널의 중심점, / -1, -1 하면 커널 사이즈에 맞게 자동설정
cv2.imshow('dst', dst)
cv2.waitKey()



















































