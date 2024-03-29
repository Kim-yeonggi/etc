import socket
import numpy as np
import cv2
import tkinter
import threading
from PIL import Image, ImageTk
from queue import Queue
import os


temp_queue = Queue()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')     # 학습된 데이터 불러옴
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
file_path = './'
glasses_img = './g'


class Client:
    def __init__(self, master):
        self.master = master
        self.master.title("client")
        self.master.geometry("800x600")
        self.flag = 0

        self.capNum = 1


        self.canvas = tkinter.Canvas(master, width=640, height=360, bg='white', bd=1, highlightthickness=0)

        self.canvas.focus_set()
        self.canvas.bind("<Button-1>", self.key_press)

        self.canvas.pack()

        self.buttons = tkinter.Label(self.master, width=20, height=5)

        self.filter1Button = tkinter.Button(self.buttons, text="색상 반전", width=15, height=3,  command=self.color_filter)
        self.filter2Button = tkinter.Button(self.buttons, text="얼굴 모자이크", width=15, height=3, command=self.mosaic_filter)
        self.defaltButton = tkinter.Button(self.buttons, text="원본 영상", width=15, height=3, command=self.back)

        self.buttons.pack(pady=20)
        self.filter1Button.pack(side="left")
        self.filter2Button.pack(side="left")

        self.defaltButton.pack(side="left")

        self.fileName_label = tkinter.Label(self.master, text="저장할 파일 이름")
        self.fileName = tkinter.Entry(self.master)
        self.fileName_label.pack(pady=5)
        self.fileName.configure(font=("", 13))
        self.fileName.pack()


        self.delay = 1
        self.update()

        self.master.mainloop()

    def color_filter(self):
        self.flag = 1

    def mosaic_filter(self):
        self.flag = 2



    def filter_lys(self):
        self.flag = 3
    def filter_yhy(self):
        self.flag = 4
    def filter_kju(self):
        self.flag = 5





    def back(self):
        self.flag = 0

    def key_press(self, e):
        cap_img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        if os.path.isfile(file_path+f'{self.fileName.get()}.png'):
            while os.path.isfile(file_path+f'{self.fileName.get()} ({self.capNum}).png'):   # 파일 이름 존재 여부 체크
                # print("파일 이미 있음")
                self.capNum += 1
            cv2.imwrite(file_path + f'{self.fileName.get()} ({self.capNum}).png', cap_img)

        else:
            cv2.imwrite(file_path+f'{self.fileName.get()}.png', cap_img)
        self.capNum = 1  # 캡쳐시마다 번호증가




    def update(self):
        # Get a frame from the video source
        global frame
        frame = temp_queue.get()

        if self.flag == 1:
            # blur = cv2.blur(frame, ksize=(5, 5))
            reverse = 255 - frame
            frame = reverse

        elif self.flag == 2:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 2)     # 불러온 데이터 기반으로 객체 검출
            # minNeighbors : n개의 사각형이 중복되어야 검출
            # scaleFactor : 화면 확대 비율

            # count = 0
            for (x, y, w, h) in faces:      # x, y : 시작 위치(좌상단)
                # print(x, y, w, h)
                # cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                # 모자이크 처리할 영역 추출
                roi = frame[y:y + h, x:x + w]   # 얼굴 영역

                # 추출한 영역 축소 후 확대 (모자이크 효과)
                factor = 10 # 모자이크 픽셀 크기 조절
                small_roi = cv2.resize(roi, (w // factor, h // factor))
                mosaic_roi = cv2.resize(small_roi, (w, h), interpolation=cv2.INTER_NEAREST)

                # 모자이크 처리된 영역을 원본 이미지에 적용
                frame[y:y + h, x:x + w] = mosaic_roi


        try:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)
            self.master.after(self.delay, self.update)
        except Exception as ex:
            # print(ex)
            pass



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


def get_frame(a):
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
        decimg = cv2.imdecode(data, 1)
        decimg = cv2.cvtColor(decimg, cv2.COLOR_BGR2RGB)
        temp_queue.put(decimg)

        key = cv2.waitKey(1)


    client_socket.close()

t = threading.Thread(target=get_frame, args=(1, ))
t.daemon = True
t.start()

Client(tkinter.Tk())
