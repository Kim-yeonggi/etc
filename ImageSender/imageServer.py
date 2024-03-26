import socket
import os
import threading
import tkinter
from tkinter import filedialog


image_path = ""

def send_image(connection, image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        connection.sendall(image_data)

def main(a):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 1111))     # ip, port 바인딩
    server_socket.listen()      # 서버 주체 : 클라이언트의 접속 여부 확인
    print("서버 오픈")
    connection, address = server_socket.accept()    # 서버 주체 : 클라이언트 연결 승인 / 클라이언트가 접속할 때까지 대기
    print("연결 클라이언트 주소:", address)

    # image_path = f"{connection.recv(1024).decode()}.png"

    send_image(connection, image_path)
    # connection.close()
    # server_socket.close()

t= threading.Thread(target=main, args=(1,))
t.start()

root = tkinter.Tk()

def btn_click():
    global image_path
    image_path = tkinter.filedialog.askopenfilename(filetypes=[("image files", "*.png"), ("image files", "*.jpg")])

btn = tkinter.Button(root, text="이미지 선택", command=btn_click)
btn.pack(pady=5)
root.mainloop()