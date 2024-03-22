import socket       # 통신 소켓 -> TCP / UDP
from threading import Thread    # 동시 처리를 위해 thread 사용
import tkinter      # 파이썬에 내장된 GUI 개발 라이브러리


tk = tkinter.Tk()       # 메인프레임 선언
tk.geometry("1000x1000")    # 해상도 설정
entry = tkinter.Entry(tk)   # 텍스트 입력 박스 생성
entry2 = tkinter.Listbox(tk, height=15, width=50)   # 대화창 목록 리스트 박스 생성

# 4. 우측하단 접속 리스트
user_listbox = tkinter.Listbox()
user_listbox.place(x=600, y=600, width=200, height=300)
user_list = []

user_count_label = tkinter.Label(text="현재 접속 수: ")

# user_count = tkinter.Label(text="3")
# user_count.place(x=685, y=575)

HOST = '192.168.31.128'    # 내가 접속할 서버의 ip주소

# localhost : 내 로컬 환경 ip를 의미 == 127.0.0.1
PORT = 9900        # 서버의 포트 번호 (서로 같아야 연결 가능)
def rcvMsg(sock):
    while True: # 무한루프
        try:
            global user_list
            global user_count_label

            data = sock.recv(1024)      # 1024 단위로 자른 데이터를 받는다.
            if not data:        # 데이터가 없으면
                break           # 탈출
            print(data.decode())    # 전달받은 데이터를 콘솔에 출력한다. decode 로 풀어서 출력

            msg = data.decode()

            if msg.startswith('[update]'):
                user_list = (msg.replace('[update]', "")[:-2].strip()).split()
                user_count_label = tkinter.Label(text=f"현재 접속 수: {len(user_list)} 명")
                user_count_label.place(x=600, y=575)

                user_listbox.delete(0, "end")
                for ul in user_list:
                    print("--------------ul--",ul)
                    user_listbox.insert(0, ul)
                continue

            case_list = ["c0","c1","c2","c3","c4"]
            if msg[-2:] in case_list:
                case = msg[-2:]
                print("case  -------------",case)
                msg = msg.rstrip(f"{case}").strip()
                print("msg ---------------",msg)
            else:
                case = 0



            entry2.insert(-1, msg+"\n")


            # 일반 0 / 퇴장,입장,채팅얼리기 1 / 공지 2 / 강퇴 3 / 귓속말 4
            if case == "c1":
                entry2.itemconfig(0, fg='dimgray')
                # if "입장" in msg:
                #     user_listbox.insert(0, msg.split()[0].strip("[]"))
                #     # user_list.append(msg.split()[0].strip("[]"))
                #
                # elif "퇴장" in msg:
                #     user_listbox.delete(len(user_list) -1 - user_list.index(msg.split()[0].strip("[]")))
                #     # user_list.remove(msg.split()[0].strip("[]"))

            elif case == "c2":
                entry2.itemconfig(0, fg="blue")
            elif case == "c3":
                entry2.itemconfig(0, fg="red")
            elif case == "c4":
                entry2.itemconfig(0, fg="green")
            else:
                pass


            entry2.update() # 업데이트 : 인서트 결과를 화면에 반영한다.
            entry2.see(0)

            user_listbox.update()
            user_listbox.see(0)


        except:     # 예외처리
            tk.destroy()    # form 종료 : c#의 form.dispose() + form.close()
            pass

def runChat():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:     # socket 객체 sock 생성
        sock.connect((HOST, PORT))  # 소켓을 통해 connect 메서드 호출
        t = Thread(target=rcvMsg, args=(sock,))     # 쓰레드를 생성하고 쓰레드로 rcvMsg 함수를 구동시키고, 매개변수는 sock 객체
        t.daemon = True#데몬스레드로 설정해서 메인스레드가 종료되면 자동으로 함꼐 종료, 프로세스 묶이는 문제 방지
        t.start()   # 쓰레드 시작

        def okClick():
            sock.send(entry.get().encode())     # entry 박스 값을 소켓에 인코딩 후 전송

        def onEnter(event):
            okClick()
            entry.delete(0,tkinter.END) # entry 박스 값 지우기

        def logout():
            tk.destroy()

        def msgClick(event):
            index = entry2.curselection()[0]  # 튜플로 리턴 오기때문에 인덱싱0번
            value = entry2.get(index)
            # print(value, '------------------value')
            if '>>>' in value:
                user = value[0:value.find('>>>')]
                entry.delete(0, "end")
                entry.insert(0, f"/w {user} ")

                tk.after(1, entry.focus_set)
            elif '<<<' in value:
                user = value[0:value.find('<<<')]
                entry.delete(0, "end")
                entry.insert(0, f"/w {user} ")

                tk.after(1, entry.focus_set)
            else:
                pass

        def add_ban_list():
            if len(admin_textbox.get()) != 0:
                sock.send(("/o " + admin_textbox.get()).encode())
                admin_textbox.delete(0, "end")

        def remove_ban_list():
            if len(admin_textbox.get()) != 0:
                sock.send(("/i " + admin_textbox.get()).encode())
                admin_textbox.delete(0, "end")

        def stop_chat():
            sock.send("/b".encode())

        def notice():
            if len(notice_textbox.get()) != 0:
                sock.send(("/n "+notice_textbox.get()).encode())
                notice_textbox.delete(0, "end")


        def userClick(event):
            index = user_listbox.curselection()[0]  # 튜플로 리턴 오기때문에 인덱싱0번
            value = user_listbox.get(index)
            # print(value, '------------------value')
            entry.delete(0, "end")
            entry.insert(0, f"/w {value} ")

            tk.after(1, entry.focus_set)

        entry2.pack(side=tkinter.LEFT, fill=tkinter.BOTH, padx=5, pady=5)
        # pack 함수 : 배치를 위한 함수


        label = tkinter.Label(tk, text="채팅.")
        entry.pack()
        label.pack()
        btn = tkinter.Button(tk, text="OK", command=okClick)
        btn.pack()

        btn_logout = tkinter.Button(tk, text="나가기", command=logout)
        btn_logout.pack(padx=5, pady=5)

        entry.bind("<Return>", onEnter)     # return == enter키 를 의미

        #1. 메시지 클릭 -> /w 자동입력
        entry2.bind("<<ListboxSelect>>", msgClick)

        # 3. 관리자 권한
        admin_textbox = tkinter.Entry(tk)
        admin_textbox.pack(padx=5, pady=20)

        # 강제퇴장
        add_ban_btn = tkinter.Button(tk, text="강제퇴장",command=add_ban_list)
        add_ban_btn.pack(pady=5)

        # 강제퇴장 해제
        remove_ban_btn = tkinter.Button(tk, text="강제퇴장 해제",command=remove_ban_list)
        remove_ban_btn.pack(pady=5)

        # 채팅창 얼리기 풀기
        stop_chat_btn = tkinter.Button(tk, text="채팅금지", command=stop_chat)
        stop_chat_btn.pack(pady=5)

        # 공지사항
        notice_textbox = tkinter.Entry(tk)
        notice_textbox.pack(padx=5, pady=5)

        notice_btn = tkinter.Button(tk, text="공지", command=notice)
        notice_btn.pack(pady=5)



        # 1. 메시지 클릭 -> /w 자동입력
        user_listbox.bind("<<ListboxSelect>>", userClick)




        tk.mainloop()   # mainloop : 위에서 만든 tk_form을 구동시킨다.
        # mainloop()는 스레드를 점유한다.

runChat()