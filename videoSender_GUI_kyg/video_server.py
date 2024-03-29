import socket
import cv2      # 필터 사용
import numpy    # 픽셀 접근 용도
from queue import Queue

from _thread import *


enclosure_queue = Queue()       # 대기줄 객체 공간

# queue 영상 데이터 대기줄 임시 저장 공간
def threaded(client_socket, addr, queue):       # 스레드 2

    print("connected by :", addr[0], ':', addr[1])
    while True:
        try:
            data = client_socket.recv(1024)     # 클라이언트에서 보낸 데이터("1") 받음
            if not data:
                print('Disconnected by ' + addr[0] , ':', addr[1])
                break
            stringData = queue.get()    # 인코딩한 상태

            # 프레임 길이 전송 / 16자리로 전송(16byte)
            client_socket.send(str(len(stringData)).ljust(16).encode())     # 클라이언트 count 가 16인 이유

            # 영상 데이터 전송
            client_socket.send(stringData)

        except :
            print('Disconnected by ' + addr[0], ':', addr[1])
            break
    client_socket.close()

count = 0
def webcam(queue):  # 스레드1
    global  count
    # video_path = "v.mp4"
    capture = cv2.VideoCapture(0)   # 웹캠 장치 불러오기

    while True:
        ret, frame = capture.read() # 동영상 정보 읽어오기
        if ret == False:
            continue
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        # imencode(
        result, imgencode = cv2.imencode('.jpg', frame, encode_param)   # 영상 인코드 함수

        data = numpy.array(imgencode)
        stringData = data.tostring()
        if count == 0:
            print(stringData)
        count = 1
        queue.put(stringData)   # queue에 인코딩한 영상 데이터 담아두기
        cv2.imshow('server', frame) # 윈도우에 출력


        key = cv2.waitKey(1)    # 화면 꺼지지 않게 처리
        if key == 27:
            break


HOST = '192.168.31.128'
PORT = 9999
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# SO_REUSEADDR 선언을 1로 해주면 같은 주소가 접속 반복해도 허용해줌
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# enclosure_queue.clear()

server_socket.bind((HOST, PORT))
server_socket.listen()

def clear_queue(queue):
    while not queue.empty():
        queue.get()     # queue에서 가장 앞에 있는 요소를 추출함(추출된 요소는 queue에서 제거됨)

print('server start')
start_new_thread(webcam, (enclosure_queue,))    # 스레드1 : 웹캠 작동
while True:
    print("wait")
    client_socket, addr = server_socket.accept()    # 클라이언트 접속 허용 작업
    clear_queue(enclosure_queue)
    start_new_thread(threaded, (client_socket, addr, enclosure_queue,))     # 스레드2 : 서버 작동


server_socket.close()


