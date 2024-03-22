import socketserver
import threading
import time

import sys

# HOST = '192.168.31.147'
HOST = '192.168.31.128'
PORT = 9900
lock = threading.Lock()


member = ['김영기', '강병헌', '김중규', '정재현', '허민재', '이윤서', '윤하얀', '전준용',
          '윤석현', '박희창', '진정현', '김지욱', '성재민', '김자연']
admin = ['admin']
ban_list = []


# update_time = 0

class UserManager:
    def __init__(self):
        self.users = {}     # client side를 통해 접속한 유저 객체를 담는 함수
        self.blocked_user = []

    def addUser(self, username, conn, addr):
        if username in self.users:
            conn.send('already exist.\n'.encode())
            return None


        lock.acquire()      # thread의 lock 객체는 공유데이터를 다룰 때 쓰레드 독립성을 보장
        self.users[username] = (conn, addr)     # 동기화해야하는 작업 lock 사이에 작성 ex) atm 돈 인출
        lock.release()      # 독립성 보장해야하는 작업이 끝나면 release로  풀어준다.
        self.sendMessageToAll('[%s] 입장' % username, 1)

        users = "[update]"
        for ul in self.users.keys():
            users += ul+" "
        self.sendMessageToAll(users)

        return username

    def removeUser(self, username):
        if username not in self.users:
            return
        lock.acquire()
        del self.users[username]
        lock.release()

        users = "[update]"
        for ul in self.users.keys():
            users += ul + " "
        self.sendMessageToAll(users)

        self.sendMessageToAll('[%s] 퇴장.' % username, 1)



    def messageHandler(self, username, msg, chatTime, all_chatTime):

        # if all_chatTime < time.time() and self.per:
        if all_chatTime < time.time():
            if msg[0] != '/' and time.time() - chatTime >= 0.5 and username not in ban_list:
                self.sendMessageToAll('[%s] %s' % (username, msg))
                return 'chat'       # --------- 3. 변경
            elif time.time() - chatTime < 0.5:
                self.sendMessageToPersonal("도배금지", username)

            elif msg[0] + msg[1] == '/w':
                if msg.split()[1] not in self.users.keys():
                    self.sendMessageToPersonal(f"{msg.split()[1]}는 현재 서버에 없습니다.", username, 1)
                elif msg.split()[1] == username:
                    self.sendMessageToPersonal("자신에게는 귓속말이 불가능합니다.", username)
                else:
                    sendMsg = msg.replace("/w", "").replace(f'{msg.split(' ')[1]}', "").strip()
                    self.sendMessageToPersonal(f"{username}>>> {sendMsg}", username, 4)
                    self.sendMessageToPersonal(f"{username}<<< {sendMsg}", msg.split(' ')[1], 4)


        stop_chat = 3  # 전체 채팅 금지 시간
        if username in admin:
            if msg.strip() == '/quit':
                self.removeUser(username)
                return -1

            if '/o' in msg and msg.index('/o') == 0:
                ban_user = msg.replace('/o', "").strip()
                if ban_user not in ban_list and ban_user in self.users.keys():
                    self.sendMessageToAll(f"{ban_user}님이 강제퇴장 당하셨습니다.", 3)
                    ban_list.append(ban_user)
                    if ban_user in self.users.keys():
                        self.sendMessageToAll(f"[{ban_user}] 퇴장.", 1)
                        self.users[ban_user][0].close()
                        del self.users[ban_user]

                    time.sleep(0.05)
                    users = "[update]"
                    for ul in self.users.keys():
                        users += ul + " "
                    self.sendMessageToAll(users)

                else:
                    self.sendMessageToPersonal(f"유효하지 않습니다. 다시 입력해주세요.", username)



            elif '/i' in msg and msg.index('/i') == 0:
                ban_user = msg.replace('/i', "").strip()
                if ban_user in member and ban_user in ban_list:
                    self.sendMessageToAll(f"{ban_user}님의 강제퇴장이 해제되었습니다.")
                    ban_list.remove(ban_user)
                    # return ban_user

            elif '/n' in msg and msg.index('/n') == 0:
                self.sendMessageToAll("[%s] %s" % ('공지사항', msg.replace('/n', "").strip()), 2)

            elif '/b' in msg and msg.index('/b') == 0:
                self.sendMessageToAll(f"{stop_chat}초 간 채팅이 금지됩니다.", 1)
                return f'stop_chat {stop_chat}'



        return ""



    def sendMessageToAll(self, msg, case=0):        # 전체메시지
        for conn, addr in self.users.values():
            conn.send((msg + f"        c{case}").encode())
            # conn.send(msg.encode())

    def sendMessageToPersonal(self, msg, username, case=0):
        self.users.get(username)[0].send((msg + f"        c{case}").encode())
        # self.users.get(username)[0].send(msg.encode())


class MyTcpHandler(socketserver.BaseRequestHandler):
    userman = UserManager()

    def handle(self):       # 서버에 들어온 클라이언트(request) 다룸
        global slang_list
        slang_list = []

        global all_chatTime
        all_chatTime = time.time()

        # 김지욱
        self.per = True


        print(self,"self memory")
        print('client [%s] 연결' % self.client_address[0])
        self.chatTime = 0
        update_time = 0

        try:
            print(self)
            username = self.registerUsername()      # 유저 아이디
            print(username,":username")
            # msg = self.request.recv(1024)           # 첫 메시지 입력받기

            print(self.request)
            print(self.client_address)
            print(self.server)


            while True:

                msg = self.request.recv(1024)           # 2번째 이후 메시지들
                print(msg.decode())

                # 비속어 필터링
                if time.time() - update_time >= 60:
                    # update_time = time.time()
                    # slang_list = []
                    with open("slangs.txt", "r", encoding='utf-8') as f:
                        while True:
                            line = f.readline()
                            slang_list.append(line.strip())
                            if not line:  # 파일 읽기가 종료된 경우
                                break

                temp_msg = msg.decode('utf-8')
                for sl in slang_list:
                    if sl in temp_msg:
                        temp_msg = temp_msg.replace(sl, '*'*len(sl))
                        msg = temp_msg.encode()

                return_msg = self.userman.messageHandler(username, msg.decode(), self.chatTime, all_chatTime)
                if return_msg == -1:
                    self.request.close()
                    break

                elif return_msg == 'chat':      # 채팅을 친 경우
                    self.chatTime = time.time()

                # elif return_msg in member:      # 강제퇴장 or 강제퇴장 해제를 했을 경우
                #     if return_msg not in ban_list:  # 강제퇴장
                #         ban_list.append(return_msg)
                #
                #     else:   # 강제퇴장 해제
                #         ban_list.remove(return_msg)

                elif 'stop_chat' in return_msg:
                    if all_chatTime < time.time():
                        all_chatTime = time.time() + float(return_msg.replace('stop_chat', "").strip())

        except Exception as e:
            print("에러 메시지--------------------------------\n", e)


        print('[%s]종료' % self.client_address[0])
        self.userman.removeUser(username)
    def registerUsername(self):
        while True:
            self.request.send('ID'.encode())
            username = self.request.recv(1024)
            username = username.decode().strip()

            if username in ban_list:
                self.request.send("강제퇴장당한 멤버입니다.".encode())
                continue
            elif username in member or username in admin:
                if self.userman.addUser(username, self.request, self.client_address):

                    return username
            else:
                self.request.send("ID 다시 입력:".encode())
                continue
class ChatingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    # ThreadingMixIn : 쓰레드 자동 분배
    pass
def runServer():
    try:
        server = ChatingServer((HOST, PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('서버종료')
        server.shutdown()
        server.server_close()


runServer()



