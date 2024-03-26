# OpenCV 영상처리
import cv2
print(cv2.__version__)  # 4.9.0 ver 확인

# cv2 : imread videocapture
# cv2는 단일 영상 (frame, 이미지) 혹은 video를 다루는 패키지
# 저장된 영상, 실시간 영상에 대한 데이터 처리 가능
# (0)은 기본 카메라 장치, 내장 웹캠 0번

image = cv2.imread("samoyed.png", cv2.IMREAD_ANYCOLOR)
# IMREAD_ANYCOLOR : 3채널 이미지
# IMREAD_COLOR : BGR 이미지
# IMREAD_UNCHANGED : 원본 사용
# IMREAD_GRAYSCALE : 흑백 처리 이미지 사용 (1채널)
# IMREAD_REDUCED_GRAYSCALE_2 : 사이즈 1/2로 줄이고, 그레이 스케일

cv2.imshow("image", image)
cv2.waitKey(3000)

# # capture = cv2.VideoCapture('dog_video.mp4')
# capture = cv2.VideoCapture(0)
#
# # set 함수로 카메라 속성 설정 가능
# # 속성명과 벨류 형태로 매개변수 지정
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)
#
# while cv2.waitKey(30) < 0:
#     # 위 waitKey 30 < 0 은 사용자의 키 이벤트 대기 루프 -> 아무 키나 키 이벤트 발생
#     # 30ms로 설정하고
#     # 키 입력이 없으면 -1 반환
#     # 키 입력이 들어오면 ord('x')
#     ret, frame = capture.read()        # capture : 파일 객체 취급 -> read 가능
#     cv2.imshow("result Frame", frame)
# capture.release()
# cv2.destroyAllWindows()