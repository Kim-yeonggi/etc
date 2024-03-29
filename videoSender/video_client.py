import socket
import numpy as np
import cv2

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf:
            return None
        # print(newbuf, "-----newbuf")
        buf += newbuf
        count -= len(newbuf)
    return buf

# 서버에 클라이언트 연결
HOST = '192.168.31.128'
PORT = 9999
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

count = 0
while True:

    # 서버에 준비 완료상태 전송
    message = '1'
    client_socket.send(message.encode())


    length = recvall(client_socket, 16)     # 받을 이미지 프레임 길이 측정
    # print(length)
    stringData = recvall(client_socket, int(length))    # 받은 프레임 길이만큼 데이터 받음
    data = np.frombuffer(stringData, dtype='uint8')     # .frombuffer() : 바이너리 데이터를 array로 변환
    if count == 0:
        print(length, "len")
        print(stringData, 'std')
        print(data, "----data")
        print(type(data))
        for i in data:
            count += 1
            print(i, "---i")
            print(count, 'c:\n')
    decimg = cv2.imdecode(data, 1)
    cv2.imshow('client', decimg)
    key = cv2.waitKey(1)

client_socket.close()