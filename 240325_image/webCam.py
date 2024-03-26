import cv2
def main():
    video_path = "dog_video.mp4"
    # capture = cv2.VideoCapture(video_path)
    capture = cv2.VideoCapture(0)
    # videoCapture : 카메라 장치나 비디오 파일을 불러오는 메서드
    # capture
    if not capture.isOpened():   # isOpened() 메서드로 카메라 연결 확인
        print("로딩 실패")
        return
    while True:
        ret, frame = capture.read()     # read 메서드로 프레임 가져옴
        if not ret:
            print("프레임 로드 실패")
            break
        cv2.imshow('재생', frame)     # cv2 제공하는 보여주는 화면
        key = cv2.waitKey(25)   # waitkey 사용자 입력 대기 25ms
        if key == ord('q'):     # 유니코드로 변환 / q 키 입력받으면 종료
            break
    capture.release()
    cv2.destroyAllWindows()     # imshow : 화면을 끈다
main()