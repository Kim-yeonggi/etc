import tkinter
import socket

tk = tkinter.Tk()
tk.geometry("500x500")

label_ip = tkinter.Label(tk, text="IP")
textBox_ip = tkinter.Entry(tk, width=50)

label_port = tkinter.Label(tk, text="PORT")
textBox_port = tkinter.Entry(tk, width=50)

label_name = tkinter.Label(tk, text="저장할 이미지 이름 설정")
textBox_name = tkinter.Entry(tk, width=50)


img = ""
def receive_image(connection, save_path):
    global img
    with open(save_path, 'ab') as image_file:
        while True:
            data = connection.recv(1024)
            if not data:
                break
            img += str(data)
            image_file.write(data)

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        HOST = textBox_ip.get()
        PORT = textBox_port.get()

        client_socket.connect((HOST, int(PORT)))
        save_path = textBox_name.get()
        receive_image(client_socket, save_path)
        print("완료")
        client_socket.close()

    except Exception as ex:
        print(ex)




label_ip.pack(pady=5)
textBox_ip.pack(pady=5)

label_port.pack(pady=5)
textBox_port.pack(pady=5)

label_name.pack(pady=5)
textBox_name.pack(pady=5)

save_image_button = tkinter.Button(tk, text="이미지 가져오기", command=main)
save_image_button.pack(pady=10)

tk.mainloop()
