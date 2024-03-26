import socket
import os
import threading
import tkinter
from tkinter import filedialog

tk = tkinter.Tk()
tk.geometry("500x500")


def load_image():
    image_path = filedialog.askopenfilename(filetypes=[("image files", "*.png"), ("image files", "*.jpg")])
    label_image.configure(text=image_path)
load_image_btn = tkinter.Button(tk, text="이미지 불러오기", command=load_image)
load_image_btn.pack(pady=10)

label_image = tkinter.Label(tk, text="")
label_image.pack(pady=10)

def send_image(connection, image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        connection.sendall(image_data)


def main(x):

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("192.168.31.128", 1111))  # ip, port 바인딩

    while 1:
        server_socket.listen()  # 서버 주체 : 클라이언트의 접속 여부 확인
        print("서버 오픈")

        connection, address = server_socket.accept()  # 서버 주체 : 클라이언트 연결 승인
        print("연결 클라이언트 주소:", address)

        image_path = f"{label_image.cget('text')}"
        send_image(connection, image_path)
        connection.close()



t=threading.Thread(target=main,args=(1,))
t.start()
tk.mainloop()

