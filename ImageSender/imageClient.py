import socket

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
    client_socket.connect(('localhost', 1111))
    save_path = 'samoyed2.png'
    receive_image(client_socket, save_path)
    print("완료")
    client_socket.close()

main()