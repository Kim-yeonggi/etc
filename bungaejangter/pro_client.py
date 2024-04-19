# 할 것 : 서버 연결, (addProduct카테고리 수정 v) , myFrame 완성 및 서버 연결

import re
import tkinter as tk
import tkinter.font
import tkinter.ttk as ttk
import pymysql
import win32api
import socket
import platform
from PIL import Image, ImageTk
import webbrowser
import cv2
from tkinter import filedialog
import io
import pickle
import numpy as np
import os
import atexit
import datetime
import tkinter.messagebox


def handle_exit(msg):
    print(msg)


def on_closing(window):
    global complete
    msg = ["!disconnect"]
    sock.send(pickle.dumps(msg))
    complete = 0
    window.destroy()


def on_closing_make(frame):
    msg = "!disconnect"
    frame.destroy()





# 데이터베이스 왔다갔다 하는거 비동기 async


# HOST = "172.30.1.79"
HOST = "192.168.31.23"
#HOST = "localhost"
PORT = 9950
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((HOST,PORT))


# mysql
# con = pymysql.connect(host="localhost", user='root', password="0000", port=3306, db="team5",charset='utf8')
# con = pymysql.connect(host=HOST, user='team5', password="1234", port=3307, db="team5",charset='utf8')
#con = pymysql.connect(host=HOST, user='team5', password="1234", port=3306, db="team5", charset='utf8')  # 샹떼pc방
#
# cur = con.cursor()

key = 0
email = ["@naver.com", "@daum.com", "@gmail.com"]

phone = ["KT", "SKT", "LG"]
# 정렬기준 리스트
search_sort = ["정확도순", "최신순", "저가순", "고가순", "거리순"]
# 검색 필터 리스트
search2_sort = ["선택", "카테고리", "상품상태", "해시태그", "가격", "무료배송", "교환가능", "동네"]
id_check = 0  # 중복체크

make_check = True  # 회원가입 중복 금지

s_sale = ["판매 중", "예약됨", "판매완료"]
search_sort2 = ["선택", "카테고리", "상품상태", "해시태그", "가격", "무료배송", "교환가능", "동네"]
sales_dic = {}

complete_img_filepath = "./imgs/complete.png"


# 광고 클릭
def adopen(url):
    webbrowser.open_new(url)


def openFrame(frame):
    frame.tkraise()


def truncate_text(text, max_length=22):
    if len(text) > max_length:
        return text[:max_length - 3] + "..."
    else:
        return text


def truncate_text_search(text, max_length=5):
    if len(text) > max_length:
        return text[:max_length - 2] + "..."
    else:
        return text


def truncate_text_recent(text, max_length=16):
    if len(text) > max_length:
        return text[:max_length - 2] + "..."
    else:
        return text


def change_productSale(state, dict):
    sendMsg = ["change_productSale", state, dict]
    sock.send(pickle.dumps(sendMsg))


user_id = ""
def loadStoreNameFunc():
    global user_id
    print("아이디 불러오기")
    sendMsg = ["loadStoreName"]
    sock.send(pickle.dumps(sendMsg))
    recvMsg = pickle.loads(sock.recv(1024))
    if recvMsg[0] == "loadStoreName":
        user_id = recvMsg[1]



class login:
    def __init__(self, window):
        self.window = window
        # self.window.geometry("500x750+700+100")
        self.window.geometry("500x750+700+100")
        self.window.resizable(width=False, height=False)
        # self.window.overrideredirect(True)
        self.window.bind("<Key>", self.key)

        global complete
        self.window.protocol("WM_DELETE_WINDOW", lambda window=self.window: on_closing(window=window))

        self.login_font = tkinter.font.Font(family="맑은 고딕", size=20, weight="bold")
        self.basic_font = tkinter.font.Font(family="맑은 고딕", size=14)
        self.overlab_font = tkinter.font.Font(family="맑은 고딕", size=10)
        self.combo_font = tkinter.font.Font(family="맑은 고딕", size=11)
        self.logo_img = tk.PhotoImage(file="imgs/home_top/logoBtn.png")
        self.back_img = tk.PhotoImage(file="imgs/back.png")

        # 로그인 창
        self.login_win = tk.Frame(self.window, width=500, height=750, bg="white")

        # 로고
        self.login_logo_label = tk.Label(self.login_win, width=170, height=40, bg="white", image=self.logo_img)
        self.login_logo_label.place(x=-10, y=10)

        self.login_label = tk.Label(self.login_win, text="로그인", font=self.login_font, bg="white")
        self.login_label.place(x=30, y=90)

        self.id_label = tk.Label(self.login_win, text="ID", font=self.basic_font, bg="white")
        self.id_label.place(x=30, y=190)
        self.id_entry = tk.Entry(self.login_win, font=self.basic_font, width=43, bd=0, highlightthickness=0,
                                 bg="gainsboro")
        self.id_entry.place(x=30, y=230)

        self.pw_label = tk.Label(self.login_win, text="Password", font=self.basic_font, bg="white")
        self.pw_label.place(x=30, y=300)
        self.pw_entry = tk.Entry(self.login_win, show="*", font=self.basic_font, width=43, bd=0, highlightthickness=0,
                                 bg="gainsboro")
        self.pw_entry.place(x=30, y=340)
        self.login_btn = tk.Button(self.login_win, text="로그인", font=self.basic_font, fg="white", bg="#d80c18",
                                   cursor="hand2",
                                   bd=0, width=39, activebackground="#a60a14", activeforeground="white",
                                   command=lambda: [self.login_check(self.id_entry.get(), self.pw_entry.get())])

        # self.login_btn.bind("<Return>", lambda: self.login_check(self.id_entry.get(), self.pw_entry.get()))
        self.login_btn.place(x=30, y=500)
        self.find_btn = tk.Button(self.login_win, text="아이디/비밀번호 찾기", fg="gray", cursor="hand2", bd=0,
                                  highlightthickness=0, bg="white", command=lambda: [self.openFrame_id(self.find_win)])
        self.find_btn.place(x=30, y=550)
        self.make_btn = tk.Button(self.login_win, text="회원가입", fg="#d80c18", bg="white", cursor="hand2", bd=0,
                                  highlightthickness=0, activeforeground="#a60a14", command=self.make)
        self.make_btn.place(x=410, y=550)

        self.login_win.place(x=0, y=0)

        # 아이디 비밀번호 찾기
        self.find_win = tk.Frame(self.window, width=500, height=750, bg="white")

        # 로고
        self.find_logo_label = tk.Label(self.find_win, width=170, height=40, image=self.logo_img, bg="white")
        self.find_logo_label.place(x=330, y=10)

        self.back_btn = tk.Button(self.find_win, font=self.basic_font, cursor="hand2", bd=0, bg="white",
                                  image=self.back_img, width=25, height=29,
                                  highlightthickness=0, command=lambda: [self.openFrame(self.login_win)])
        self.back_btn.place(x=30, y=20)
        self.id_btn = tk.Button(self.find_win, text="ID찾기", font=self.basic_font, bg="white", cursor="hand2", bd=0,
                                anchor="n",
                                highlightthickness=0, command=lambda: [self.openFrame_id(self.id_find)])
        self.id_btn.place(x=30, y=80)
        self.pw_btn = tk.Button(self.find_win, text="PW재설정", font=self.basic_font, bg="white", cursor="hand2",
                                bd=0, anchor="n",
                                highlightthickness=0, command=lambda: [self.openFrame_pw(self.pw_find)])
        self.pw_btn.place(x=113, y=80)

        self.pw_find = tk.Frame(self.find_win, width=500, height=640, bg="white")
        self.pw_find.place(x=0, y=110)
        self.pw_name = tk.Label(self.pw_find, text="이름", font=self.basic_font, bg="white")
        self.pw_name.place(x=30, y=70)
        self.pw_name_en = tk.Entry(self.pw_find, font=self.basic_font, width=43, bd=0, highlightthickness=0,
                                   bg="gainsboro")
        self.pw_name_en.place(x=30, y=120)
        self.pw_birth = tk.Label(self.pw_find, text="생년월일", font=self.basic_font, bg="white")
        self.pw_birth.place(x=30, y=180)
        self.pw_birth_en = tk.Entry(self.pw_find, font=self.basic_font, width=43, bd=0, highlightthickness=0,
                                    bg="gainsboro")
        self.pw_birth_en.place(x=30, y=230)
        self.pw_id = tk.Label(self.pw_find, text="ID", font=self.basic_font, bg="white")
        self.pw_id.place(x=30, y=290)
        self.pw_id_en = tk.Entry(self.pw_find, font=self.basic_font, width=43, bd=0, highlightthickness=0,
                                 bg="gainsboro")
        self.pw_id_en.place(x=30, y=340)
        self.pw_find_btn = tk.Button(self.pw_find, text="재설정", font=self.basic_font, fg="white", bg="#d80c18",
                                     cursor="hand2", bd=0,
                                     width=39, activebackground="#a60a14", activeforeground="white",
                                     command=lambda: [self.pw_find_func(self.pw_id_en.get(), self.pw_name_en.get(),
                                                                        self.pw_birth_en.get())])
        self.pw_find_btn.bind("<Return>", lambda e: self.pw_find_func(self.pw_id_en.get(), self.pw_name_en.get(),
                                                                      self.pw_birth_en.get()))
        self.pw_find_btn.place(x=30, y=500)

        self.id_find = tk.Frame(self.find_win, width=500, height=640, bg="white")
        self.id_find.place(x=0, y=110)
        self.id_name = tk.Label(self.id_find, text="이름", font=self.basic_font, bg="white")
        self.id_name.place(x=30, y=70)
        self.id_name_en = tk.Entry(self.id_find, font=self.basic_font, width=43, bd=0, highlightthickness=0,
                                   bg="gainsboro")
        self.id_name_en.place(x=30, y=120)
        self.id_birth = tk.Label(self.id_find, text="생년월일", font=self.basic_font, bg="white")
        self.id_birth.place(x=30, y=180)
        self.id_birth_en = tk.Entry(self.id_find, font=self.basic_font, width=43, bd=0, highlightthickness=0,
                                    bg="gainsboro")
        self.id_birth_en.place(x=30, y=230)
        self.id_find_btn = tk.Button(self.id_find, text="찾기", font=self.basic_font, fg="white", bg="#d80c18",
                                     cursor="hand2", bd=0,
                                     width=39,
                                     activebackground="#a60a14", activeforeground="white",
                                     command=lambda: [self.id_find_func(self.id_name_en.get(), self.id_birth_en.get())])
        self.id_find_btn.place(x=30, y=500)

        self.find_win.place(x=0, y=0)
        self.openFrame(self.login_win)

    # 아이디 찾기 창
    def id_find_func(self, name, birth):
        sendMsg = ["id_find", name, birth]
        sock.send(pickle.dumps(sendMsg))
        recvMsg = pickle.loads(sock.recv(1024))
        if name == "" or birth == "":
            win32api.MessageBox(0, "입력되지 않은 칸이 있습니다.", "에러", 16)
        elif recvMsg[0] == "id_find":
            if not recvMsg[1]:
                win32api.MessageBox(0, "다시 입력해 주세요.", "에러", 16)
            else:
                self.id = recvMsg[1]
                self.id_check = tk.Frame(self.window, width=500, height=750, bg="white")

                # 로고
                self.id_check_logo_label = tk.Label(self.id_check, width=170, height=40, image=self.logo_img,
                                                    bg="white")
                self.id_check_logo_label.place(x=-10, y=10)

                self.id_check_label = tk.Label(self.id_check, text=f"아이디는 {self.id} 입니다.", font=self.basic_font,
                                               bg="white")
                self.id_check_label.place(x=130, y=200)
                self.pw_find_btn = tk.Button(self.id_check, text="비밀번호 재설정", font=self.basic_font, fg="white",
                                             bg="#d80c18", cursor="hand2", bd=0, width=39,
                                             activebackground="#a60a14", activeforeground="white",
                                             command=lambda: [self.openFrame_id_pw(self.find_win)])
                self.pw_find_btn.place(x=30, y=500)
                self.login_btn = tk.Button(self.id_check, text="로그인 화면으로", font=self.basic_font, fg="white",
                                           bg="#d80c18", cursor="hand2", bd=0, width=39,
                                           activebackground="#a60a14", activeforeground="white",
                                           command=lambda: [self.openFrame(self.login_win)])
                self.login_btn.place(x=30, y=550)
                self.id_check.place(x=0, y=0)
                self.id_name_en.delete(0, "end")
                self.id_birth_en.delete(0, "end")
                self.openFrame(self.id_check)

    # 비밀번호 재설정 창
    def pw_find_func(self, id, name, birth):
        sendMsg = ["pw_find", id, name, birth]
        sock.send(pickle.dumps(sendMsg))
        recvMsg = pickle.loads(sock.recv(1024))

        if id == "" or name == "" or birth == "":
            win32api.MessageBox(0, "입력되지 않은 칸이 있습니다.", "에러", 16)
        elif recvMsg[0] == "pw_find":
            if not recvMsg[1]:
                win32api.MessageBox(0, "다시 입력해 주세요.", "에러", 16)
            else:
                self.pw_check = tk.Frame(self.window, width=500, height=750, bg="white")

                # 로고
                self.pw_check_logo_label = tk.Label(self.pw_check, width=170, height=40, image=self.logo_img,
                                                    bg="white")
                self.pw_check_logo_label.place(x=-10, y=10)

                self.pw_input_label = tk.Label(self.pw_check, text="비밀번호", font=self.basic_font, bg="white")
                self.pw_input_label.place(x=30, y=200)
                self.pw_input_en = tk.Entry(self.pw_check, font=self.basic_font, width=43, bd=0, highlightthickness=0,
                                            bg="gainsboro")
                self.pw_input_en.place(x=30, y=250)
                self.pw_check_label = tk.Label(self.pw_check, text="비밀번호 확인", font=self.basic_font, bg="white")
                self.pw_check_label.place(x=30, y=300)
                self.pw_check_en = tk.Entry(self.pw_check, show='*', font=self.basic_font, width=43, bd=0,
                                            highlightthickness=0, bg="gainsboro")
                self.pw_check_en.place(x=30, y=350)
                self.pw_check_btn = tk.Button(self.pw_check, text="재설정", font=self.basic_font, fg="white", bg="#d80c18",
                                              cursor="hand2", bd=0, width=39,
                                              activebackground="#a60a14", activeforeground="white",
                                              command=lambda: [
                                                  self.pw_reset(self.pw_input_en.get(), self.pw_check_en.get(), id,
                                                                name)])
                self.pw_check_btn.place(x=30, y=600)
                self.pw_check.place(x=0, y=0)
                self.openFrame(self.pw_check)

    # 비밀번호 재설정 버튼
    def pw_reset(self, pw1, pw2, id, name):
        sendMsg = ["pw_reset", id, name]
        sock.send(pickle.dumps(sendMsg))
        recvMsg = pickle.loads(sock.recv(1024))

        if recvMsg[0] == "pw_reset":
            if recvMsg[1] != pw1:  # 기존 비밀번호와 같지 않을때
                if pw1 != "" and pw2 != "" and pw1 == pw2:
                    sendMsg = ["update_pw", pw1, id]
                    sock.send(pickle.dumps(sendMsg))
                    recvMsg = pickle.loads(sock.recv(1024))

                    if recvMsg[0] == "update_pw" and recvMsg[1]:
                        win32api.MessageBox(0, "비밀번호가 재설정되었습니다.", "알림", 0)
                        self.openFrame(self.login_win)
                    elif recvMsg[0] == "new_pw" and not recvMsg[1]:
                        win32api.MessageBox(0, "오류가 발생했습니다\n다시 한 번 시도해주세요", "알림", 0)

                elif pw1 == "" or pw2 == "":
                    win32api.MessageBox(0, "입력되지않은 비밀번호가 있습니다.", "에러", 16)
                else:
                    win32api.MessageBox(0, "비밀번호가 동일하지 않습니다.", "에러", 16)
            else:
                win32api.MessageBox(0, "동일한 비밀번호입니다.", "에러", 16)

    # 회원가입 창
    def make(self):
        global make_check
        if make_check == True:
            make_check = False  # 중복으로 열리지 않게
            self.make_win = tk.Toplevel(self.window, width=500, height=750, bg="white")

            # 로고
            self.make_win_logo_label = tk.Label(self.make_win, width=170, height=40, image=self.logo_img, bg="white")
            self.make_win_logo_label.place(x=330, y=10)

            # self.make_win.geometry("500x750+700+100")
            self.make_win.geometry("500x750+700+10")
            self.make_win.title("회원가입")
            self.make_back_btn = tk.Button(self.make_win, bg="white", font=self.basic_font, bd=0, image=self.back_img,
                                           cursor="hand2",
                                           highlightthickness=0, command=lambda: [self.back(self.make_win)])
            self.make_back_btn.place(x=30, y=20)
            self.make_name_label = tk.Label(self.make_win, text="이름", bg="white", font=self.basic_font)
            self.make_name_label.place(x=30, y=80)
            self.make_name_entry = tk.Entry(self.make_win, font=self.basic_font, bg="gainsboro", width=43, bd=0,
                                            highlightthickness=0)
            self.make_name_entry.place(x=30, y=120)
            self.make_birth_label = tk.Label(self.make_win, text="생년월일", bg="white", font=self.basic_font)
            self.make_birth_label.place(x=30, y=160)
            self.make_birthy_entry = tk.Entry(self.make_win, font=self.basic_font, bg="gainsboro", width=11, bd=0,
                                              highlightthickness=0)
            self.make_birthy_entry.place(x=30, y=200)
            self.make_birthm_entry = tk.Entry(self.make_win, font=self.basic_font, bg="gainsboro", width=11, bd=0,
                                              highlightthickness=0)
            self.make_birthm_entry.place(x=170, y=200)
            self.make_birthd_entry = tk.Entry(self.make_win, font=self.basic_font, bg="gainsboro", width=11, bd=0,
                                              highlightthickness=0)
            self.make_birthd_entry.place(x=310, y=200)

            self.make_id_label = tk.Label(self.make_win, text="ID", bg="white", font=self.basic_font)
            self.make_id_label.place(x=30, y=240)
            self.make_id_entry = tk.Entry(self.make_win, font=self.basic_font, bg="gainsboro", width=30, bd=0,
                                          highlightthickness=0)
            self.make_id_entry.place(x=30, y=280)

            self.overlab_btn = tk.Button(self.make_win, text="중복확인", width=15, font=self.overlab_font, fg="white",
                                         bg="#d80c18",
                                         cursor="hand2", bd=0, activebackground="#a60a14",
                                         activeforeground="white",
                                         command=lambda: [self.overlab_check(self.make_id_entry.get())])
            self.overlab_btn.place(x=350, y=280)

            self.make_pw_label = tk.Label(self.make_win, text="Password", bg="white", font=self.basic_font)
            self.make_pw_label.place(x=30, y=320)
            self.make_pw_entry = tk.Entry(self.make_win, show="*", font=self.basic_font, bg="gainsboro", width=43, bd=0,
                                          highlightthickness=0)
            self.make_pw_entry.place(x=30, y=360)

            self.make_email_label = tk.Label(self.make_win, text="Email", bg="white", font=self.basic_font)
            self.make_email_label.place(x=30, y=400)
            self.make_email_entry = tk.Entry(self.make_win, font=self.basic_font, bg="gainsboro", width=22, bd=0,
                                             highlightthickness=0)
            self.make_email_entry.place(x=30, y=440)
            self.make_email_combo = ttk.Combobox(self.make_win, values=email, font=self.combo_font)
            self.make_email_combo.set("선택")
            self.make_email_combo.place(x=280, y=440)
            self.make_phone_label = tk.Label(self.make_win, text="연락처", bg="white", font=self.basic_font)
            self.make_phone_label.place(x=30, y=480)
            self.make_phone_combo = ttk.Combobox(self.make_win, values=phone, font=self.combo_font, width=10)
            self.make_phone_combo.set("선택")
            self.make_phone_combo.place(x=30, y=520)
            self.make_phone_entry = tk.Entry(self.make_win, font=self.basic_font, bg="gainsboro", width=31, bd=0,
                                             highlightthickness=0)
            self.make_phone_entry.place(x=150, y=520)
            self.make_addr_label = tk.Label(self.make_win, text="주소", bg="white", font=self.basic_font)
            self.make_addr_label.place(x=30, y=560)
            self.make_addr_entry = tk.Entry(self.make_win, font=self.basic_font, bg="gainsboro", width=43, bd=0,
                                            highlightthickness=0)
            self.make_addr_entry.place(x=30, y=600)

            self.usermake_btn = tk.Button(self.make_win, text="회원가입", width=39, font=self.basic_font, fg="white",
                                          bg="#d80c18",
                                          cursor="hand2", bd=0, activebackground="#a60a14",
                                          activeforeground="white",
                                          command=lambda: [
                                              self.mysql_add(self.make_id_entry.get(), self.make_pw_entry.get(),
                                                             self.make_name_entry.get(),
                                                             self.make_birthy_entry.get() + self.make_birthm_entry.get() + self.make_birthd_entry.get(),
                                                             self.make_email_entry.get() + self.make_email_combo.get(),
                                                             self.make_phone_combo.get(),
                                                             self.make_phone_entry.get(),
                                                             self.make_addr_entry.get())])
            self.usermake_btn.place(x=30, y=680)
            # self.make_win.overrideredirect(True)

    # 회원가입 버튼
    def mysql_add(self, id, pw, name, birth, email, agency, phone, addr):
        count_name = 0
        count_email = 0
        count_agency = 0
        p = re.compile('[ㄱ-힣]')
        for i in range(len(name)):
            r = p.search(name[i])
            if r != None:  # 한글이 있으면
                count_name += 1
###################################################
        if "선택" in email or email.count("@") > 1:  # 도메인을 선택 안했거나 입력한 이메일에 @가 포함되어 있는 경우
            count_email += 1
#################################################
        if "선택" == agency:
            count_agency += 1
        if count_name == len(name) and birth.isdigit() and len(
                birth) == 8 and count_email == 0 and count_agency == 0 and phone.isdigit() and pw != "" and addr != "":
            if id_check == 2:
                sendMsg = ["signUp", f"'{id}','{pw}','{name}','{birth}','{email}','{agency}','{phone}','{addr}',''"]
                encoded_Msg = pickle.dumps(sendMsg)
                sock.send(encoded_Msg)
                recvMsg = sock.recv(1024)
                decode_Msg = pickle.loads(recvMsg)
                if decode_Msg[0] == "signUp":
                    if decode_Msg[1]:
                        win32api.MessageBox(0, "등록되었습니다.", "알림", 0)
                        self.make_win.destroy()
                    else:
                        win32api.MessageBox(0, "등록에 실패하였습니다.", "알림", 0)
            else:
                win32api.MessageBox(0, "중복체크 하십시오.", "알림", 0)
        elif count_name != len(name):
            win32api.MessageBox(0, "잘못된 이름입니다.", "에러", 16)
        elif not birth.isdigit() or len(birth) != 8:
            win32api.MessageBox(0, "잘못된 생년월일입니다.", "에러", 16)
        elif pw == "":
            win32api.MessageBox(0, "비밀번호를 입력해주세요.", "에러", 16)
        elif count_email != 0:
            win32api.MessageBox(0, "잘못된 이메일입니다.", "에러", 16)
        elif count_agency != 0:
            win32api.MessageBox(0, "통신사를 선택하세요.", "에러", 16)
        elif not phone.isdigit():
            win32api.MessageBox(0, "잘못된 전화번호입니다.", "에러", 16)
        elif addr == "":
            win32api.MessageBox(0, "주소를 입력해주세요.", "에러", 16)

    # 중복 확인 버튼
    def overlab_check(self, id):
        """
        list=[]
        list.extend(["overlab",id])
        overlab = json.dumps(list)
        sock.send(overlab.encode())"""

        global id_check
        id_check = 0
        count_id = 0
        p = re.compile('[ㄱ-힣]')
        for i in range(len(id)):
            r = p.search(id[i])
            if r != None:  # 한글이 포함되어 있으면 +1
                count_id += 1
        sendMsg = ["id_check", f"{id}"]
        sock.send(pickle.dumps(sendMsg))
        recvMsg = sock.recv(1024)
        decoded_Msg = pickle.loads(recvMsg)
        if decoded_Msg[0] == "id_check":
            if count_id == 0 and id.isalnum():  # id에 한글이 없고 영어와 숫자로 이루어져 있다면
                if decoded_Msg[1]:
                    win32api.MessageBox(0, "이미 있는 아이디입니다.", "에러", 16)
                    id_check = 1
                else:
                    win32api.MessageBox(0, "생성가능한 아이디입니다.", "알림", 0)
                    id_check = 2
            else:
                win32api.MessageBox(0, "잘못된 아이디입니다.", "에러", 16)
        return id_check

    # 로그인 버튼
    def login_check(self, id, pw):
        sendMsg = ["logIn", id, pw]
        sock.send(pickle.dumps(sendMsg))

        resvMsg = sock.recv(1024)
        decoded_resvMsg = pickle.loads(resvMsg)

        if decoded_resvMsg[0] == "logIn":
            if decoded_resvMsg[1]:
                self.window.destroy()
                window = Home(tkinter.Tk())
                window.window.mainloop()
            else:
                win32api.MessageBox(0, "아이디/비밀번호를 다시 입력해주세요.", "에러", 16)

    # 프레임 띄우기
    def openFrame(self, frame):
        frame.tkraise()

    # 첫화면에서 아이디/비밀번호 찾기를 눌렀을때
    def openFrame_id(self, frame):
        frame.tkraise()
        openFrame(self.id_find)
        self.id_btn.configure(font=("맑은 고딕", 14, "underline"))
        self.pw_btn.configure(font=self.basic_font)

    # 아이디/비밀번호 찾기 프레임에서 PW 재설정을 눌렀을때
    def openFrame_pw(self, frame):
        frame.tkraise()
        self.pw_btn.configure(font=("맑은 고딕", 14, "underline"))
        self.id_btn.configure(font=self.basic_font)

    # 아이디찾고, 비밀번호 재설정을 눌렀을때
    def openFrame_id_pw(self, frame):
        frame.tkraise()
        openFrame(self.pw_find)
        self.pw_btn.configure(font=("맑은 고딕", 14, "underline"))
        self.id_btn.configure(font=self.basic_font)
        self.pw_id_en.insert(0, self.id)

    # 뒤로가기
    def back(self, frame):
        global make_check
        frame.destroy()
        make_check = True

    # 키 입력
    def key(self, e):
        global key
        keyname = e.keysym
        if keyname == "Escape":
            self.window.destroy()


class ScrollFrame(tkinter.Frame):
    def __init__(self, parent, frame):
        super().__init__(parent)  # create a frame (self)

        self.canvas = tkinter.Canvas(frame, border=0, background="#ffffff", width=500)  # place canvas on self
        self.canvas.configure(height=616)
        self.viewPort = tkinter.Frame(self.canvas,
                                      background="#ffffff",
                                      border=0)  # place a frame on the canvas, this frame will hold the child widgets
        self.vsb = tkinter.Scrollbar(self, orient="vertical", command=self.canvas.yview)  # place a scrollbar on self
        self.canvas.configure(yscrollcommand=self.vsb.set, border=0)  # attach scrollbar action to scroll of canvas

        self.vsb.pack(side="right", fill="y")  # pack scrollbar to right of self
        self.canvas.pack(side="left", fill="both")  # pack canvas to left of self and expand to fil
        self.canvas_window = self.canvas.create_window((0, 0), window=self.viewPort, anchor="n",
                                                       # add view port frame to canvas
                                                       tags="self.viewPort")

        self.viewPort.bind("<Configure>",
                           self.onFrameConfigure)  # bind an event whenever the size of the viewPort frame changes.
        self.canvas.bind("<Configure>",
                         self.onCanvasConfigure)  # bind an event whenever the size of the canvas frame changes.

        self.viewPort.bind('<Enter>', self.onEnter)  # bind wheel events when the cursor enters the control
        self.viewPort.bind('<Leave>', self.onLeave)  # unbind wheel events when the cursorl leaves the control

        self.onFrameConfigure(
            None)  # perform an initial stretch on render, otherwise the scroll region has a tiny border until the first resize

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox(
            "all"))  # whenever the size of the frame changes, alter the scroll region respectively.

    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window,
                               width=canvas_width)  # whenever the size of the canvas changes alter the window region respectively.

    def onMouseWheel(self, event):  # cross platform scroll wheel event
        widet = self.checkCursor(event)
        if str(widet).split('!')[-1].strip("!") != "text":
            if platform.system() == 'Windows':
                self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
            elif platform.system() == 'Darwin':
                self.canvas.yview_scroll(int(-1 * event.delta), "units")
            else:
                if event.num == 4:
                    self.canvas.yview_scroll(-1, "units")
                elif event.num == 5:
                    self.canvas.yview_scroll(1, "units")

    def checkCursor(self, event):
        widget = event.widget.winfo_containing(event.x_root, event.y_root)
        if widget:
            return widget

    def onEnter(self, event):  # bind wheel events when the cursor enters the control
        if platform.system() == 'Linux':
            self.canvas.bind_all("<Button-4>", self.onMouseWheel)
            self.canvas.bind_all("<Button-5>", self.onMouseWheel)
        else:
            self.canvas.bind_all("<MouseWheel>", self.onMouseWheel)

    def onLeave(self, event):  # unbind wheel events when the cursorl leaves the control
        if platform.system() == 'Linux':
            self.canvas.unbind_all("<Button-4>")
            self.canvas.unbind_all("<Button-5>")
        else:
            self.canvas.unbind_all("<MouseWheel>")


class Home(tkinter.Frame):
    def openFrame(self, frame):  # place로 할것
        self.search_en.delete("0", "end")
        openFrame(self.search_bot)
        frame.tkraise()

    def __init__(self, root):
        tkinter.Frame.__init__(self, root)

        self.window = root
        self.window.title("번개장터")
        self.window.protocol("WM_DELETE_WINDOW", lambda window=self.window: on_closing(window=window))
        self.window.geometry("500x750+700+100")
        # self.window.geometry("500x750+700+10")
        # self.window.overrideredirect(True)
        self.window.bind('<Escape>', lambda e: self.close_win(e))

        global complete
        self.window.protocol("WM_DELETE_WINDOW", lambda window=self.window: on_closing(window=window))

        # 최근 검색어 라벨 딕셔너리
        self.recent_label_dic = {}
        # 모든 검색어 리스트
        self.recent_all = []
        # 검색어 횟수 딕셔너리
        self.count_dic = {}
        # 최근 본 상품 리스트
        self.recent_sale = []
        # 찜 딕셔너리
        self.like_dic = {}
        # 찜 이미지 변경
        #&&&&&&&&&&&&&&&&&&&&&&&&&&
        self.like_bool = True
        #&&&&&&&&&&&&&&&&&&&&&&&&&&
        # 채팅 리스트
        self.chat_storage = []
        # 중복 금지
        self.make_check = True
        loadStoreNameFunc()

        # 각 화면 인스턴스 생성

        # 홈 프레임
        self.homeFrame = tkinter.Frame(self.window, width=500, height=750, border=0)
        self.homeFrame.place(x=0, y=0)

        # 홈 상단 프레임
        self.mainFrame_top = tkinter.Frame(self.homeFrame, width=500, height=15, bg='white', border=0)
        # self.mainFrame_top.pack()
        self.mainFrame_top.place(x=0, y=0)

        self.logoButtonsLabel = tkinter.Label(self.mainFrame_top, bg='white', width=100, height=4)
        self.logoButtonsLabel.pack()

        self.logo_img = tkinter.PhotoImage(file="./imgs/home_top/logoBtn.png")
        self.logoButton = tkinter.Label(self.logoButtonsLabel, text="번개장터", image=self.logo_img, width=170, height=40,
                                        bg='white')
        self.logoButton.bind("<Button-1>", self.refresh_recentCategoryFrame)

        self.searchButton_img = tkinter.PhotoImage(file="./imgs/home_top/searchButton.png")
        self.searchButton = tkinter.Button(self.logoButtonsLabel, text="검색", image=self.searchButton_img, bg='white',
                                           border=0, command=lambda: [self.openFrame_search_win(self.search_window)])

        self.noticeButton_img = tkinter.PhotoImage(file="./imgs/home_top/noticeButton.png")
        self.noticeButton = tkinter.Button(self.logoButtonsLabel, text="알림", image=self.noticeButton_img, bg='white',
                                           border=0)

        self.logoButton.place(x=-10, y=10)
        self.searchButton.place(x=400, y=15)
        self.noticeButton.place(x=450, y=15)

        # 중앙 프레임
        self.homeFrame_center = tkinter.Frame(self.homeFrame, border=0)
        self.homeFrame_center.place(x=0, y=65)

        self.scrollFrame = ScrollFrame(self, self.homeFrame_center)  # add a new scrollable frame.
        self.scrollFrame.configure(height=616)
        self.scrollFrame.configure(bg='white', width=50)

        # 광고
        self.mainLabel_AD = tkinter.Label(self.scrollFrame.viewPort, bg='darkgray', borderwidth=0)
        self.adImg = tkinter.PhotoImage(file='./imgs/home_center/ad.png')
        self.mainLabel_AD.configure(image=self.adImg)
        self.mainLabel_AD.pack()
        # self.mainLabel_AD.place(x=0, y=0)

        # 메뉴 버튼들 모음 레이블
        self.mainLabel_Btns = tkinter.Label(self.scrollFrame.viewPort, width=100, height=5, bg='white')
        self.mainLabel_Btns.pack(pady=20)
        # self.mainLabel_Btns.place(x=0, y=310)

        # 전체메뉴 버튼
        self.totalMenuLabel = tkinter.Label(self.mainLabel_Btns, width=9, height=6, bg='white', border=0)
        self.totalMenuLabel.pack(side='left', padx=22)
        self.totalMenuButton = tkinter.Button(self.totalMenuLabel, bg='white', border=0)
        self.totalMenuButton_img = tkinter.PhotoImage(file="./imgs/home_center/category.png")
        self.totalMenuButton.configure(image=self.totalMenuButton_img, border=0)
        self.totalMenuButton.bind("<Button-1>", self.main_category)
        self.totalMenuButton.pack()
        self.totalMenuText = tkinter.Label(self.totalMenuLabel, text="전체메뉴", bg='white', fg='#4c4c4c',
                                           font=("맑은 고딕", 10, "bold"))
        self.totalMenuText.pack()

        # 찜 버튼
        self.wishLabel = tkinter.Label(self.mainLabel_Btns, width=9, height=6, bg='white', border=0)
        self.wishLabel.pack(side='left', padx=22)
        self.wishButton = tkinter.Button(self.wishLabel, bg='white', border=0)
        self.wishButton_img = tkinter.PhotoImage(file="./imgs/home_center/wish.png")
        self.wishButton.configure(image=self.wishButton_img, border=0)
        self.wishButton.pack()
        self.wishText = tkinter.Label(self.wishLabel, text="찜", bg='white', fg='#4c4c4c', font=("맑은 고딕", 10, "bold"))
        self.wishText.pack()

        # 찜/최근 본 상품 프레임
        self.main_recent_win = tk.Frame(self.window, width=500, height=750)
        self.main_recent_win.place(x=0, y=0)
        # 상단
        self.main_recent_top = tk.Frame(self.main_recent_win, width=500, height=105, bg="white")
        self.back_img = tk.PhotoImage(file="imgs/back.png")
        self.recent_back = tk.Label(self.main_recent_top, width=35, height=39, bd=0, bg="white", image=self.back_img,
                                    cursor="hand2")
        self.recent_back.bind("<Button-1>", lambda event: self.lower(event, self.main_recent_win))
        self.recent_back.image = self.back_img
        self.recent_back.place(x=10, y=13)
        self.top_label = ttk.Label(self.main_recent_top, text="관심상품", font=("맑은 고딕", 16, "bold"), background="white")
        self.top_label.place(x=50, y=15)
        self.like_btn = tk.Button(self.main_recent_top, text="찜", border=0, background="white")
        self.like_btn.configure(font=("맑은 고딕", 16, "bold"), anchor="n",
                                command=lambda: self.openFrame_like(self.main_like_bot))
        self.like_btn.place(x=100, y=67)
        self.recent_btn = tk.Button(self.main_recent_top, text="최근 본 상품", border=0, background="white")
        self.recent_btn.configure(font=("맑은 고딕", 16, "bold"), anchor="n",
                                  command=lambda: self.openFrame_recent(self.main_recent_bot))
        self.recent_btn.place(x=300, y=67)

        # 찜 하단
        self.main_like_bot = tk.Frame(self.main_recent_win, width=500, height=650, bg="white")
        self.main_like_scroll = ScrollFrame(self, self.main_like_bot)
        self.like_in_scroll = tk.Frame(self.main_like_scroll.viewPort, width=500, bd=0, bg="white")

        self.main_like_bot.place(x=0, y=105)

        # 최근 본 상품 버튼
        self.recentProductLabel = tkinter.Label(self.mainLabel_Btns, width=9, height=6, bg='white', border=0)
        self.recentProductLabel.pack(side='left', padx=22)
        self.recentProductButton = tkinter.Button(self.recentProductLabel, bg='white', border=0)
        self.recentProductButton_img = tkinter.PhotoImage(file="./imgs/home_center/recentProduct.png")
        self.recentProductButton.configure(image=self.recentProductButton_img, border=0)
        self.recentProductButton.pack()
        self.recentProductText = tkinter.Label(self.recentProductLabel, text="최근본상품", bg='white', fg='#4c4c4c',
                                               font=("맑은 고딕", 10, "bold"))
        self.recentProductText.pack()

        # 최근 본 상품 하단
        self.main_recent_bot = tk.Frame(self.main_recent_win, width=500, height=650, bg="white")
        self.main_recent_scroll = ScrollFrame(self, self.main_recent_bot)
        self.recent_in_scroll = tk.Frame(self.main_recent_scroll.viewPort, width=500, bd=0, bg="white")

        self.main_recent_top.place(x=0, y=0)
        self.main_recent_bot.place(x=0, y=105)

        # if self.y + 300 < 616:
        self.main_recent_scroll.canvas.configure(height=650)
        # self.main_recent_scroll.viewPort.configure(height=650)
        self.recent_in_scroll.configure(height=650)

        # 내 상품 버튼
        self.myProductLabel = tkinter.Label(self.mainLabel_Btns, width=9, height=6, bg='white')
        self.myProductLabel.pack(side='left', padx=22)
        self.myProductButton = tkinter.Button(self.myProductLabel, bg="white")
        self.myProductButton_img = tkinter.PhotoImage(file="./imgs/home_center/myFeed.png")
        self.myProductButton.configure(image=self.myProductButton_img, border=0)
        self.myProductButton.pack()
        self.myProductText = tkinter.Label(self.myProductLabel, text="내피드", bg='white', fg='#4c4c4c',
                                           font=("맑은 고딕", 10, "bold"))
        self.myProductText.pack()
        self.myProductButton.bind("<Button-1>", self.openMyFeed)

        # 최근 본 상품과 비슷한 제품들 (카테고리)
        # 최근 카테고리 불러오기
        self.recentCategory_List = self.loadRecentCategory()

        # 제품1 정보 : self.self.recentCategory_List[0]
        # 제품2 정보 : self.self.recentCategory_List[1]
        # 제품3 정보 : self.self.recentCategory_List[2]

        # 최근 본 상품과 비슷한 제품 전체 프레임
        self.recentCategoryFrame = tkinter.Frame(self.scrollFrame.viewPort, width=500, height=150, bg="white", border=0)
        self.recentCategoryFrame.pack()

        # 타이틀 프레임
        self.recentCategoryFrame_title = tkinter.Frame(self.recentCategoryFrame, bg='white', border=0, width=500,
                                                       height=34)
        self.recentCategoryFrame_title.pack()

        self.recentCategoryLabel = tkinter.Label(self.recentCategoryFrame_title, )
        self.recentCategoryLabel.configure(text="최근에 본 상품과 비슷해요", bg='white', font=("맑은 고딕", 15, "bold"))
        self.recentCategoryLabel.place(x=13, y=0)

        self.recentCategoryButton_more = tkinter.Label(self.recentCategoryFrame_title, )
        self.recentCategoryButton_more.configure(text="더보기 〉", bg='white', font=("맑은 고딕", 12, "bold"), fg="#686868")
        self.recentCategoryButton_more.place(x=422, y=4)

        try:
            # 제품 프레임
            self.recentCategoryFrame_center = tkinter.Frame(self.recentCategoryFrame, bg='white', border=0, width=500,
                                                            height=263)
            self.recentCategoryFrame_center.pack(pady=10)

            # 제품1
            self.recentCatgoryTuple_product1 = self.recentCategory_List[0]

            self.recentCategoryLabel_product1 = tkinter.Frame(self.recentCategoryFrame_center, bg='white', border=0,
                                                              width=143, height=263)
            # self.recentCategoryLabel_product1.bind("<Button-1>", lambda event, sinfo_list=self.recentCatgoryTuple_product1: self.main_sales_click(event, sinfo_list))
            self.recentCategoryLabel_product1.bind("<Button-1>", lambda event, sinfo_list=self.recentCatgoryTuple_product1:
                                                self.main_sales_click(event, sinfo_list))

            self.recentCategoryLabel_product1.pack(side='left', padx=10)

            self.rcl_product1Label_img = tkinter.Label(self.recentCategoryLabel_product1, bg='white', border=0)
            # self.rcl_product1Img = tkinter.PhotoImage(file="./imgs/home_center/testProduct.png")

            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            self.rcl_product1Img_binary = Image.open(io.BytesIO(self.recentCatgoryTuple_product1[11]))
            self.rcl_product1Img_binary = self.rcl_product1Img_binary.resize((143, 176))
            self.rcl_product1Img = ImageTk.PhotoImage(self.rcl_product1Img_binary)
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

            self.rcl_product1Label_img.configure(image=self.rcl_product1Img)
            self.rcl_product1Label_img.place(x=0, y=0)

            self.rcl_product1Label_price = tkinter.Label(self.recentCategoryLabel_product1, bg='white', border=0)
            self.rcl_product1Label_price.configure(font=("맑은 고딕", 14, "bold"),
                                                   text=f"{format(int(self.recentCatgoryTuple_product1[5]), ',')}원")
            self.rcl_product1Label_price.place(x=0, y=182)

            #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            self.rcl_product1Label_like_img = tk.PhotoImage(file="imgs/sale_info/like.PNG")
            self.rcl_product1Label_like = tk.Label(self.recentCategoryLabel_product1, background="white", border=0)
            self.rcl_product1Label_like.configure(image=self.rcl_product1Label_like_img, width=25, height=29)
            self.rcl_product1Label_like.bind("<Button-1>",self.like_click)
            self.rcl_product1Label_like.place(x=113, y=182)
            #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

            self.product1_name = self.recentCatgoryTuple_product1[1]
            self.product1_name = truncate_text(self.product1_name)
            self.rcl_product1Label_name = tkinter.Label(self.recentCategoryLabel_product1, bg='white', border=0)
            self.rcl_product1Label_name.configure(fg="#676767", font=("맑은 고딕", 11, "bold"), text=f"{self.product1_name}"
                                                  , wraplength=143, justify='left')
            self.rcl_product1Label_name.place(x=0, y=210)

            # 제품2
            self.recentCatgoryTuple_product2 = self.recentCategory_List[1]

            self.recentCategoryLabel_product2 = tkinter.Frame(self.recentCategoryFrame_center, bg='white', border=0,
                                                              width=143, height=263)
            self.recentCategoryLabel_product2.bind("<Button-1>", lambda event, sinfo_list=self.recentCatgoryTuple_product2:
                                                self.main_sales_click(event, sinfo_list))
            self.recentCategoryLabel_product2.pack(side='left', padx=10)

            self.rcl_product2Label_img = tkinter.Label(self.recentCategoryLabel_product2, bg='white', border=0)
            # self.rcl_product2Img = tkinter.PhotoImage(file="./imgs/home_center/testProduct2.png")

            self.rcl_product2Img_binary = Image.open(io.BytesIO(
                self.recentCatgoryTuple_product2[11]))  # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            self.rcl_product2Img_binary = self.rcl_product2Img_binary.resize((143, 176))
            self.rcl_product2Img = ImageTk.PhotoImage(self.rcl_product2Img_binary)

            self.rcl_product2Label_img.configure(image=self.rcl_product2Img)
            self.rcl_product2Label_img.place(x=0, y=0)

            self.rcl_product2Label_price = tkinter.Label(self.recentCategoryLabel_product2, bg='white', border=0)
            self.rcl_product2Label_price.configure(font=("맑은 고딕", 14, "bold"),
                                                   text=f"{format(int(self.recentCatgoryTuple_product2[5]), ',')}원")
            self.rcl_product2Label_price.place(x=0, y=182)
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            self.rcl_product2Label_like_img = tk.PhotoImage(file="imgs/sale_info/like.PNG")
            self.rcl_product2Label_like = tk.Label(self.recentCategoryLabel_product2, background="white", border=0)
            self.rcl_product2Label_like.configure(image=self.rcl_product2Label_like_img, width=25, height=29)
            self.rcl_product2Label_like.bind("<Button-1>", self.like_click)
            self.rcl_product2Label_like.place(x=113, y=182)
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            self.product2_name = self.recentCatgoryTuple_product2[1]
            self.product2_name = truncate_text(self.product2_name)
            self.rcl_product2Label_name = tkinter.Label(self.recentCategoryLabel_product2, bg='white', border=0)
            self.rcl_product2Label_name.configure(fg="#676767", font=("맑은 고딕", 11, "bold"), text=f"{self.product2_name}"
                                                  , wraplength=143, justify='left')
            self.rcl_product2Label_name.place(x=0, y=210)

            # 제품3
            self.recentCatgoryTuple_product3 = self.recentCategory_List[2]

            self.recentCategoryLabel_product3 = tkinter.Frame(self.recentCategoryFrame_center, bg='white', border=0,
                                                              width=143, height=263)
            self.recentCategoryLabel_product3.bind("<Button-1>", lambda event, sinfo_list=self.recentCatgoryTuple_product3:
                                                self.main_sales_click(event, sinfo_list))
            self.recentCategoryLabel_product3.pack(side='left', padx=10)

            self.rcl_product3Label_img = tkinter.Label(self.recentCategoryLabel_product3, bg='white', border=0)
            # self.rcl_product3Img = tkinter.PhotoImage(file="./imgs/home_center/testProduct3.png")

            self.rcl_product3Img_binary = Image.open(io.BytesIO(
                self.recentCatgoryTuple_product3[11]))  # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            self.rcl_product3Img_binary = self.rcl_product3Img_binary.resize((143, 176))
            self.rcl_product3Img = ImageTk.PhotoImage(self.rcl_product3Img_binary)

            self.rcl_product3Label_img.configure(image=self.rcl_product3Img)
            self.rcl_product3Label_img.place(x=0, y=0)

            self.rcl_product3Label_price = tkinter.Label(self.recentCategoryLabel_product3, bg='white', border=0)
            self.rcl_product3Label_price.configure(font=("맑은 고딕", 14, "bold"),
                                                   text=f"{format(int(self.recentCatgoryTuple_product3[5]), ',')}원")
            self.rcl_product3Label_price.place(x=0, y=182)
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            self.rcl_product3Label_like_img = tk.PhotoImage(file="imgs/sale_info/like.PNG")
            self.rcl_product3Label_like = tk.Label(self.recentCategoryLabel_product3, background="white", border=0)
            self.rcl_product3Label_like.configure(image=self.rcl_product2Label_like_img, width=25, height=29)
            self.rcl_product3Label_like.bind("<Button-1>", self.like_click)
            self.rcl_product3Label_like.place(x=113, y=182)
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            self.product3_name = self.recentCatgoryTuple_product3[1]
            self.product3_name = truncate_text(self.product3_name)
            self.rcl_product3Label_name = tkinter.Label(self.recentCategoryLabel_product3, bg='white', border=0)
            self.rcl_product3Label_name.configure(fg="#676767", font=("맑은 고딕", 11, "bold"), text=f"{self.product3_name}"
                                                  , wraplength=143, justify='left')
            self.rcl_product3Label_name.place(x=0, y=210)
        except:
            print(Exception)

        self.scrollFrame.pack(side="top", fill="both", expand=True)

        # 하단 프레임
        self.mainFrame_bottom = tkinter.Frame(self.homeFrame, width=500, height=70, bg='white', border=0)
        self.mainFrame_bottom.place(x=0, y=685)

        # 홈 버튼
        self.homeLabel = tkinter.Frame(self.mainFrame_bottom, width=9, height=5, bg='white', border=0)
        self.homeLabel.pack(side='left', padx=32, pady=5)
        self.homeButton = tkinter.Button(self.homeLabel, bg='white', border=0)
        self.homeButton_img = tkinter.PhotoImage(file="./imgs/home_bottom/goHome_ac.png")
        self.homeButton.configure(image=self.homeButton_img)
        self.homeButton.pack()
        self.homeText = tkinter.Label(self.homeLabel, text="홈", bg='white', border=0, font=("맑은 고딕", 9, "bold"))
        self.homeText.pack()

        # 관심 버튼
        self.interestLabel = tkinter.Frame(self.mainFrame_bottom, width=9, height=5, bg='white', border=0)
        self.interestLabel.pack(side='left', padx=32, pady=5)
        self.interestButton = tkinter.Button(self.interestLabel, bg='white', border=0)
        self.interestButton_img = tkinter.PhotoImage(file="./imgs/home_bottom/interest_deac.png")
        self.interestButton.configure(image=self.interestButton_img)
        self.interestButton.pack()
        self.interestText = tkinter.Label(self.interestLabel, text="관심", bg='white', border=0, fg="#b5b5b5",
                                          font=("맑은 고딕", 9, "bold"))
        self.interestText.pack()

        # 등록 버튼
        self.addProductLabel = tkinter.Frame(self.mainFrame_bottom, width=9, height=5, bg='white', border=0)
        self.addProductLabel.pack(side='left', padx=32, pady=5)
        self.addProductButton = tkinter.Button(self.addProductLabel, bg='white', border=0)
        self.addProductButton_img = tkinter.PhotoImage(file="./imgs/home_bottom/addProduct_deac.png")
        self.addProductButton.configure(image=self.addProductButton_img)
        self.addProductButton.pack()
        self.addProductText = tkinter.Label(self.addProductLabel, text="등록", bg='white', border=0, fg="#b5b5b5",
                                            font=("맑은 고딕", 9, "bold"))
        self.addProductText.pack()

        self.addProductButton.bind("<Button-1>", self.openAddProduct)
        self.addProductLabel.bind("<Button-1>", self.openAddProduct)
        self.addProductText.bind("<Button-1>", self.openAddProduct)

        # 번개톡 버튼
        self.chatListLabel = tkinter.Frame(self.mainFrame_bottom, width=9, height=5, bg='white', border=0)
        self.chatListLabel.pack(side='left', padx=32, pady=5)
        self.chatListButton = tkinter.Button(self.chatListLabel, bg='white', border=0)
        self.chatListButton_img = tkinter.PhotoImage(file="./imgs/home_bottom/chatList_deac.png")
        self.chatListButton.configure(image=self.chatListButton_img)
        self.chatListButton.pack()
        self.chatListText = tkinter.Label(self.chatListLabel, text="번개톡", bg='white', border=0, fg="#b5b5b5",
                                          font=("맑은 고딕", 9, "bold"))
        self.chatListText.pack()

        # MY 버튼
        self.MYLabel = tkinter.Frame(self.mainFrame_bottom, width=9, height=5, bg='white', border=0)
        self.MYLabel.pack(side='left', padx=32, pady=5)
        self.MYButton = tkinter.Button(self.MYLabel, bg='white', border=0)
        self.MYButton_img = tkinter.PhotoImage(file="./imgs/home_bottom/MY_deac.png")
        self.MYButton.configure(image=self.MYButton_img)
        self.MYButton.pack()
        self.MYText = tkinter.Label(self.MYLabel, text="MY", bg='white', border=0, fg="#b5b5b5",
                                    font=("맑은 고딕", 9, "bold"))
        self.MYText.pack()

        # MY 프레임
        self.myFrame_out = tkinter.Frame(self.window, bg='white')
        # self.myFrame_out.place(x=0, y=0)
        self.myFrame_out.pack()

        self.myScrollFrame = ScrollFrame(self, self.myFrame_out)  # add a new scrollable frame.
        self.myScrollFrame.configure(bg='white', width=500)

        self.myFrame = tkinter.Frame(self.myScrollFrame.viewPort, width=500, height=685, bg='#f6f6f6')
        # self.myFrame = tkinter.Frame(self.window, width=500, height=685, bg='#000000')
        # self.myFrame.place(x=0, y=0)
        self.myFrame.pack()

        # 하트 알림 설정 버튼(기능 X)
        self.myTopBtnsFrame = tkinter.Frame(self.myFrame, width=120, height=29, bg="#f6f6f6")
        self.myTopBtnsFrame.place(x=340, y=20)

        self.myWishImg = tkinter.PhotoImage(file="./imgs/my/my_wish.png")
        self.myNotiImg = tkinter.PhotoImage(file="./imgs/my/my_noti.png")
        self.mySettingImg = tkinter.PhotoImage(file="./imgs/my/my_set.png")
        self.myWishButton = tkinter.Label(self.myTopBtnsFrame, image=self.myWishImg, bg="#f6f6f6", bd=0)
        self.myNotiButton = tkinter.Label(self.myTopBtnsFrame, image=self.myNotiImg, bg="#f6f6f6", bd=0)
        self.mySettingButton = tkinter.Label(self.myTopBtnsFrame, image=self.mySettingImg, bg="#f6f6f6", bd=0)
        self.myWishButton.pack(side="left", padx=10)
        self.myNotiButton.pack(side="left", padx=10)
        self.mySettingButton.pack(side="left", padx=10)

        # 내 상점 프로필
        self.myStoreFrame = tkinter.Frame(self.myFrame, bg='white', width=454, height=140, bd=0)
        self.myStoreFrame.place(x=23, y=69)

        self.myStoreLabelImg = tkinter.PhotoImage(file="./imgs/my/myStore.png")
        self.myStoreLabel = tkinter.Label(self.myStoreFrame, image=self.myStoreLabelImg, bg="#f6f6f6", bd=0)
        self.myStoreLabel.place(x=0, y=0)

        self.myStoreProfileImg = tkinter.PhotoImage(file='./imgs/my/myStore_profile.png')
        self.myStoreProfile = tkinter.Label(self.myStoreFrame, image=self.myStoreProfileImg, bg='white', bd=0)
        self.myStoreProfile.place(x=31, y=31)

        self.myStoreName = tkinter.Label(self.myStoreFrame, bg='white', bd=0, text=f"{user_id}",
                                         font=("맑은 고딕", 17, "bold"))
        self.myStoreName.place(x=127, y=31)
        self.myStoreToInfo = tkinter.Label(self.myStoreFrame, bg='white', bd=0, text="내 상점 보기", fg="#686868",
                                           font=("맑은 고딕", 13, "bold"))
        self.myStoreToInfo.place(x=127, y=75)

        # my 중앙(하단) 프레임
        self.myMainFrame = tkinter.Frame(self.myFrame, bg='white', width=500, height=1000)
        self.myMainFrame.place(x=0, y=235)

        self.myMainLabelImg = tkinter.PhotoImage(file="./imgs/my/myMain.png")
        self.myMainLabel = tkinter.Label(self.myMainFrame, image=self.myMainLabelImg, bg="#f6f6f6", bd='0')
        self.myMainLabel.place(x=0, y=0)

        # 판매 구매 버튼
        self.spRadio = tkinter.IntVar()
        self.spRadioImg_saleAc = tkinter.PhotoImage(file="./imgs/my/my_sale_ac.png")
        self.spRadioImg_saleDeac = tkinter.PhotoImage(file="./imgs/my/my_sale_deac.png")
        self.spRadioImg_purAc = tkinter.PhotoImage(file="./imgs/my/my_pur_ac.png")
        self.spRadioImg_purDeac = tkinter.PhotoImage(file="./imgs/my/my_pur_deac.png")

        self.myMainSPRadioButton_sale = tkinter.Radiobutton(self.myMainFrame, bg='white',
                                                            image=self.spRadioImg_saleDeac,
                                                            selectimage=self.spRadioImg_saleAc,
                                                            indicatoron=False, variable=self.spRadio, value=0, bd=0)
        self.myMainSPRadioButton_pur = tkinter.Radiobutton(self.myMainFrame, bg='white',
                                                           image=self.spRadioImg_purDeac,
                                                           selectimage=self.spRadioImg_purAc,
                                                           indicatoron=False, variable=self.spRadio, value=1, bd=0)
        self.myMainSPRadioButton_sale.place(x=162, y=20)
        self.myMainSPRadioButton_pur.place(x=250, y=20)

        self.myMainSPRadioButton_sale.bind("<Button-1>", self.openMySaleFrame)
        self.myMainSPRadioButton_pur.bind("<Button-1>", self.openMyPurFrame)

        # 판매 프레임
        self.mySaleFrame = tkinter.Frame(self.myMainFrame, width=500, height=250, bd=0, bg='white')
        self.mySaleFrame.place(x=0, y=90)

        # 올해 번 금액
        self.myTotalSalesFrame = tkinter.Frame(self.mySaleFrame, width=452, height=102, bg="#f6f6f6")
        self.myTotalSalesFrame.place(x=25, y=0)

        self.myTotalSalesLabel_img = tkinter.PhotoImage(file='./imgs/my/totalSale.png')
        self.myTotalSalesLabel = tkinter.Label(self.myTotalSalesFrame, image=self.myTotalSalesLabel_img, bg='white')
        self.myTotalSalesLabel.place(x=0, y=0)

        self.myTotalSalesValue = 0
        self.myTotalSalesLabel_money = tkinter.Label(self.myTotalSalesFrame, font=("맑은 고딕", 20, "bold"), bg="white",
                                                     text=f"{self.myTotalSalesValue}원", bd=0)
        self.myTotalSalesLabel_money.place(x=20, y=42)
        self.myTotalSalesLabel = tkinter.Label(self.myTotalSalesFrame, fg="darkgray", font=("맑은 고딕", 12), bg="white",
                                               text="올해 번 금액", )
        self.myTotalSalesLabel.place(x=20, y=18)

        self.myTotalSalesLabel_monthImg = tkinter.PhotoImage(file="./imgs/my/month.png")
        self.myTotalSalesLabel_month = tkinter.Label(self.myTotalSalesFrame, bg="white", text="월 별 통계",
                                                     font=("맑은 고딕", 11, "bold"),
                                                     image=self.myTotalSalesLabel_monthImg)
        self.myTotalSalesLabel_month.place(x=320, y=26)

        self.my_ProductLabel_img = tkinter.PhotoImage(file="./imgs/my/my_saleProduct.png")
        self.my_SalesLabel_img = tkinter.PhotoImage(file="./imgs/my/my_sell.png")
        self.my_DeliveryLabel_img = tkinter.PhotoImage(file="./imgs/my/my_delivery.png")

        # 내 상품 관리
        self.myProductFrame = tkinter.Frame(self.mySaleFrame, width=80, height=90, bg="white")
        self.myProductFrame.place(x=50, y=135)

        self.my_ProductLabel = tkinter.Label(self.myProductFrame, image=self.my_ProductLabel_img, bd=0, bg="white")
        self.my_ProductLabel.pack()
        self.my_ProductText = tkinter.Label(self.myProductFrame, text="내상품관리", bd=0, bg="white", font=("맑은 고딕", 11))
        self.my_ProductText.pack()
        self.myProductFrame.bind("<Button-1>", self.openMyFeed)
        self.my_ProductLabel.bind("<Button-1>", self.openMyFeed)
        self.my_ProductText.bind("<Button-1>", self.openMyFeed)

        # 판매내역
        self.mySalesFrame = tkinter.Frame(self.mySaleFrame, width=80, height=90, bg="white")
        self.mySalesFrame.place(x=210, y=135)

        self.my_sellLabel = tkinter.Label(self.mySalesFrame, image=self.my_SalesLabel_img, bd=0, bg="white")
        self.my_sellLabel.pack()
        self.my_sellText = tkinter.Label(self.mySalesFrame, text="판매내역", bd=0, bg="white", font=("맑은 고딕", 11))
        self.my_sellText.pack()

        self.mySalesFrame.bind("<Button-1>", self.openMySellList)
        self.my_sellLabel.bind("<Button-1>", self.openMySellList)
        self.my_sellText.bind("<Button-1>", self.openMySellList)

        # 배송신청/관리
        self.myDeliveryFrame = tkinter.Frame(self.mySaleFrame, width=80, height=90, bg="white")
        self.myDeliveryFrame.place(x=370, y=135)

        self.my_DeliveryLabel = tkinter.Label(self.myDeliveryFrame, image=self.my_DeliveryLabel_img, bd=0, bg="white")
        self.my_DeliveryLabel.pack()
        self.my_DeliveryText = tkinter.Label(self.myDeliveryFrame, text="배송관리", bd=0, bg="white", font=("맑은 고딕", 11))
        self.my_DeliveryText.pack()

        # 구매 프레임
        self.myPurFrame = tkinter.Frame(self.myMainFrame, width=500, height=150, bd=0, bg='white')
        self.myPurFrame.place(x=0, y=90)

        self.my_WishlistLabel_img = tkinter.PhotoImage(file="./imgs/my/my_wishlist.png")
        self.my_PurListLabel_img = tkinter.PhotoImage(file="./imgs/my/my_pur.png")
        self.my_RecentLabel_img = tkinter.PhotoImage(file="./imgs/my/my_recent.png")

        # 찜한 상품
        self.my_WishFrame = tkinter.Frame(self.myPurFrame, width=80, height=90, bg="white")
        self.my_WishFrame.place(x=50, y=25)

        self.my_WishlistLabel = tkinter.Label(self.my_WishFrame, image=self.my_WishlistLabel_img, bd=0, bg="white")
        self.my_WishlistLabel.pack()
        self.my_WishlistText = tkinter.Label(self.my_WishFrame, text="찜", bd=0, bg="white", font=("맑은 고딕", 11))
        self.my_WishlistText.pack()

        # 구매내역
        self.myPurListFrame = tkinter.Frame(self.myPurFrame, width=80, height=90, bg="white")
        self.myPurListFrame.place(x=210, y=25)

        self.my_PurListLabel = tkinter.Label(self.myPurListFrame, image=self.my_PurListLabel_img, bd=0, bg="white")
        self.my_PurListLabel.pack()
        self.my_PurListText = tkinter.Label(self.myPurListFrame, text="구매내역", bd=0, bg="white", font=("맑은 고딕", 11))
        self.my_PurListText.pack()

        # 최근본상품
        self.myRecentFrame = tkinter.Frame(self.myPurFrame, width=80, height=90, bg="white")
        self.myRecentFrame.place(x=370, y=25)

        self.my_RecentLabel = tkinter.Label(self.myRecentFrame, image=self.my_RecentLabel_img, bd=0, bg="white")
        self.my_RecentLabel.pack()
        self.my_RecentText = tkinter.Label(self.myRecentFrame, text="최근본상품", bd=0, bg="white", font=("맑은 고딕", 11))
        self.my_RecentText.pack()

        # 기타 프레임
        self.myETCFrame = tkinter.Frame(self.myMainFrame, width=500, height=350, bg="white")
        self.myETCFrame.place(x=0, y=350)

        for i in range(3):
            self.myETCFrame_underline = tkinter.Label(self.myETCFrame, bg='#e5e5e5', width=65, height=1, border=0)
            self.myETCFrame_underline.place(x=25, y=41 + 59 * i)

        # 받은 가격제안
        self.myRecvPriceLabel = tkinter.Label(self.myETCFrame, width=41, height=2, bg="white", anchor='w',
                                              text="받은 가격제안", font=("맑은 고딕", 14,))
        self.myRecvPriceLabel.place(x=25, y=0)

        # 개인정보수정
        self.myEditInfoLabel = tkinter.Label(self.myETCFrame, width=41, height=2, bg="white", anchor='w',
                                             text="개인정보수정", font=("맑은 고딕", 14,))
        self.myEditInfoLabel.place(x=25, y=59)
        self.myEditInfoLabel.bind("<Button-1>", lambda event, window=self.window: self.openEditInform(event, window))

        # 로그아웃
        self.myLogoutLabel = tkinter.Label(self.myETCFrame, width=41, height=2, bg="white", anchor='w',
                                           text="로그아웃", font=("맑은 고딕", 14,))
        self.myLogoutLabel.place(x=25, y=118)

        self.myLogoutLabel.bind("<Button-1>", self.logout)

        self.mySaleFrame.lift()

        self.myScrollFrame.canvas.configure(height=685)
        self.myFrame.configure(height=800)
        self.myScrollFrame.pack(side="top", fill="both", expand=True)

        # 번개톡
        self.main_talk = tk.Frame(self.window, width=500, height=685, bg="white", bd=0)
        self.main_talk.place(x=0, y=0)

        # 상단
        self.main_talk_top = tk.Frame(self.main_talk, width=500, height=40, bd=0, bg="white")
        self.main_talk_top.place(x=0, y=0)

        # 설정
        self.main_talk_setting = ttk.Label(self.main_talk_top, border=0, background="white", text="설정")
        self.main_talk_setting.config(font=("맑은 고딕", 10, "underline"))
        self.main_talk_setting.place(x=440, y=11)

        # 중단
        self.main_talk_mid = tk.Frame(self.main_talk, width=500, height=710, bd=0)
        self.main_talk_mid.place(x=0, y=40)
        self.main_talk_scroll = ScrollFrame(self, self.main_talk_mid)
        self.main_talk_scroll_view = tk.Frame(self.main_talk_scroll.viewPort, width=490, height=700, bg="white", bd=0)
        self.main_talk_scroll_view.pack()

        # 전체 대화 라벨
        self.main_talk_allchat_img = tk.PhotoImage(file="imgs/talk/allchatlabel.PNG")
        self.main_talk_allchat_label = ttk.Label(self.main_talk_scroll_view, image=self.main_talk_allchat_img, border=0,
                                                 background="white")
        self.main_talk_allchat_label.place(x=15, y=30)

        # 번개톡 광고
        self.main_talk_ad_img = tk.PhotoImage(file="imgs/talk/ad.PNG")
        self.main_talk_ad = ttk.Label(self.main_talk_scroll_view, image=self.main_talk_ad_img, border=0,
                                      background="white")
        self.main_talk_ad.bind("<Button-1>", lambda e: adopen(
            "https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000193133&t_page=%ED%86%B5%ED%95%A9%EA%B2%80%EC%83%89%EA%B2%B0%EA%B3%BC%ED%8E%98%EC%9D%B4%EC%A7%80&t_click=%EA%B2%80%EC%83%89%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_search_name=%EB%B8%8C%EB%A7%81%EA%B7%B8%EB%A6%B0&t_number=1&dispCatNo=1000001000900020001&trackingCd=Result_1"))
        self.main_talk_ad.place(x=0, y=100)


        # 찜 프레임 오픈
        self.wishLabel.bind("<Button-1>", self.main_like_click)
        self.wishButton.bind("<Button-1>", self.main_like_click)
        self.wishText.bind("<Button-1>", self.main_like_click)

        self.my_WishFrame.bind("<Button-1>", self.main_like_click)
        self.my_WishlistLabel.bind("<Button-1>", self.main_like_click)
        self.my_WishlistText.bind("<Button-1>", self.main_like_click)

        # 최근 본 상품 프레임 오픈
        self.recentProductLabel.bind("<Button-1>", self.main_recent_click)
        self.recentProductButton.bind("<Button-1>", self.main_recent_click)

        self.myRecentFrame.bind("<Button-1>", self.main_recent_click)
        self.my_RecentLabel.bind("<Button-1>", self.main_recent_click)
        self.my_RecentText.bind("<Button-1>", self.main_recent_click)



        # 프레임 오픈 기능 바인드 모음
        # 홈 프레임 오픈
        self.homeButton.bind("<Button-1>", lambda event, frame=self.homeFrame, button=self.homeButton: (
            self.openMainFrames(event, frame, button), self.refresh_recentCategoryFrame(event)))
        self.homeLabel.bind("<Button-1>", lambda event, frame=self.homeFrame, button=self.homeButton: (
            self.openMainFrames(event, frame, button), self.refresh_recentCategoryFrame(event)))
        self.homeText.bind("<Button-1>", lambda event, frame=self.homeFrame, button=self.homeButton: (
            self.openMainFrames(event, frame, button), self.refresh_recentCategoryFrame(event)))

        # 상품 등록 프레임 오픈
        self.addProductButton.bind("<Button-1>", self.openAddProduct)
        self.addProductLabel.bind("<Button-1>", self.openAddProduct)
        self.addProductText.bind("<Button-1>", self.openAddProduct)

        # MyFrame 오픈
        self.MYLabel.bind("<Button-1>",
                          lambda event, frame=self.myFrame_out, button=self.MYButton: self.openMainFrames(event, frame,
                                                                                                          button))
        self.MYButton.bind("<Button-1>",
                           lambda event, frame=self.myFrame_out, button=self.MYButton: self.openMainFrames(event, frame,
                                                                                                           button))
        self.MYText.bind("<Button-1>",
                         lambda event, frame=self.myFrame_out, button=self.MYButton: self.openMainFrames(event, frame,
                                                                                                         button))
##########################################
        # 번개톡 오픈
        self.chatListLabel.bind("<Button-1>",self.main_bot_talk)
        self.chatListButton.bind("<Button-1>",self.main_bot_talk)
        self.chatListText.bind("<Button-1>",self.main_bot_talk)
############################################
        # 메인 프레임 오픈을 위한 사전작업
        self.mainButtonImg_list = ["goHome", "interest", "chatList", "MY"]
        self.mainButton_list = [self.homeButton, self.interestButton, self.chatListButton, self.MYButton]
        self.mainButtonLabel_list = [self.homeText, self.interestText, self.chatListText, self.MYText]
        self.mainButtonImg_list2 = ["", "", "", ""]

        # 처음 로그인 하면 홈 프레임이 가장 위로 오도록 설정
        self.homeFrame.lift()

        # 검색 윈도우
        self.search_window = tk.Frame(self.window, width=500, height=750)
        openFrame(self.homeFrame)

        self.basic_font = tkinter.font.Font(family="맑은 고딕", size=14)
        self.search_window.place(x=0, y=0)
        # 검색 상단 프레임
        self.search_top = tk.Frame(self.search_window, bg="white", width=500, height=100)
        self.search_top.pack()

        # 이전 버튼
        self.back_img = tkinter.PhotoImage(file="imgs/back.png")
        self.back_btn = tk.Button(self.search_top, width=25, height=29, bg="white",
                                  cursor="hand2", bd=0, image=self.back_img,
                                  highlightthickness=0)
        self.back_btn.bind("<Button-1>", lambda event: openFrame(self.homeFrame))
        self.back_btn.place(x=20, y=23)
        # 검색 창 라벨
        self.search_en_label = tk.Label(self.search_top, bg="gainsboro", bd=0, highlightthickness=0)
        self.search_en_label.place(x=65, y=20, height=36, width=360)
        # 검색 창 엔트리
        self.search_en = tk.Entry(self.search_en_label, bg="gainsboro", bd=0,
                                  highlightthickness=0)
        self.search_en.configure(font=("맑은 고딕", 13, "bold", "underline"))
        self.search_en.insert(0, "검색어를 입력해주세요")
        self.search_en.bind("<Button-1>", self.search_en_click)
        self.search_en.bind("<Return>", self.recent_search)
        self.search_en.bind("<Key>", self.relation_search)
        self.search_en.place(x=10, y=5, height=25, width=300)

        self.x_btn_img = tk.PhotoImage(file="imgs/searchx.png")
        self.search_en_x_btn = tk.Button(self.search_top, width=20, height=20, image=self.x_btn_img, bg="gainsboro",
                                         bd=0, highlightthickness=0, command=self.del_en)

        # 홈 버튼
        self.home_img = tkinter.PhotoImage(file="imgs/home.png")
        self.home_btn = tk.Button(self.search_top, image=self.home_img, bg="white",
                                  cursor="hand2", bd=0, highlightthickness=0,
                                  command=lambda: [self.openFrame(self.homeFrame)])
        self.home_btn.place(x=450, y=27)

        # 검색 하단 프레임
        self.search_bot = tk.Frame(self.search_window, bg="white", width=500, height=650)
        self.search_bot.place(x=0, y=100)

        # 최근 검색어 라벨
        self.recent_search_label = tkinter.Label(self.search_bot, text="최근 검색어", bg="white",
                                                 font=("맑은 고딕", 19, "bold"))
        self.recent_search_label.place(x=15, y=15)
        # 최근 검색어 전체 프레임
        self.recent_frame = tk.Label(self.search_bot, bg="white")
        self.recent_frame.place(x=15, y=65, width=470, height=110)
        # 최근 검색어 프레임
        self.recent_frame_mini = tk.Frame(self.recent_frame, bg="white")
        self.recent_frame_mini.pack(anchor="w", pady=15)
        # 광고 라벨
        self.search_img = tk.PhotoImage(file="imgs/search_ad.PNG")
        self.add_label = tk.Label(self.search_bot, width=470, height=95, image=self.search_img, bg="white")
        self.add_label.bind("<Button-1>", lambda e: adopen(
            "https://play.google.com/store/apps/details?id=com.nianticlabs.pokemongo"))  # pc용 url
        self.add_label.place(x=15, y=210)
        # 인기 검색어 라벨
        self.add_label = tk.Label(self.search_bot, text="요즘 많이 찾는 검색어", font=("맑은 고딕", 19, "bold"), bg="white")
        self.add_label.place(x=15, y=340)
        # 인기 검색어 프레임
        self.rank_frame = tk.Frame(self.search_bot, width=400, bg="white")
        self.rank_frame.place(x=15, y=410)

        # 검색창에 입력시 나올 프레임
        self.relation_frame = tk.Frame(self.search_window, bg="white", width=500, height=650)
        self.relation_frame.place(x=0, y=100)
        # 연관 검색어 나올 프레임
        self.category_frame = tk.Frame(self.relation_frame, width=300, height=570, bg="white")
        self.category_frame.place(x=0, y=80)
        self.category_label = tk.Label(self.relation_frame, text="연관 검색어", font=("맑은 고딕", 19, "bold"), bg="white")
        self.category_label.place(x=15, y=15)

        # 검색어를 엔터했을때 or 검색어를 클릭했을때 나올 프레임
        self.search_frame3 = tk.Frame(self.search_window, bg="white", width=500, height=650)
        self.search_frame3.pack()
        # 정렬 기준
        self.search_sort = ttk.Combobox(self.search_frame3, values=search_sort, font=("맑은 고딕", 12))
        self.search_sort.current(0)
        self.search_sort.pack(anchor="w", padx=10)
        # 검색기준
        self.search_sort2 = ttk.Combobox(self.search_frame3, values=search_sort2, font=("맑은 고딕", 12))
        self.search_sort2.current(0)
        self.search_sort2.place(x=260, y=0)

        # 제품들 나올 스크롤프레임

        self.sale_scroll = ScrollFrame(self, self.search_frame3)
        self.sale_frame = tk.Frame(self.sale_scroll.viewPort, width=500, bd=0, bg="white")
        self.sale_frame.pack()

        # self.ScrollFrame.canvas.configure(height=100)

        openFrame(self.search_bot)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 내 상품관리(내 피드)
        self.myFeedFrame = tkinter.Frame(self.window, width=500, height=685, bg="white")
        self.myFeedFrame.place(x=0, y=0)  # 삭제혹은수정
        self.myFeedFrame.lower()
        # self.myFeedFrame.lift()

        # 내 상품관리 상단
        self.myFeedFrame_top = tkinter.Frame(self.myFeedFrame, width=500, height=50, bg="white", bd=0)
        self.myFeedFrame_top.place(x=0, y=0)

        self.myFeedBackLabel = tkinter.Label(self.myFeedFrame_top, bg='white', border=0,
                                             text="〈", font=("맑은 고딕", 17, 'bold'))
        self.myFeedBackLabel.place(x=20, y=7)
        self.myFeedBackLabel.bind("<Button-1>", lambda event, frame=self.myFeedFrame: self.lower(event, frame))

        self.myFeedNameLabel = tkinter.Label(self.myFeedFrame_top, bg='white', border=0,
                                             text="내 상품관리", font=("맑은 고딕", 15, 'bold'))
        self.myFeedNameLabel.place(x=50, y=10)

        #  내 상품관리 중앙 메인
        self.myFeedMainFrame = tkinter.Frame(self.myFeedFrame, width=500, height=635, bg='white')
        self.myFeedScrollFrame = ScrollFrame(self, self.myFeedMainFrame)
        self.myFeedMainFrame_inner = tkinter.Frame(self.myFeedScrollFrame.viewPort, width=500, height=635, bg="white")
        self.myFeedMainFrame.place(x=0, y=50)
        self.myFeedScrollFrame.pack()
        self.myFeedMainFrame_inner.pack()
        self.myFeedScrollFrame.canvas.configure(height=635)
        self.myFeedMainFrame_inner.configure(height=1000)

        # self.myFeedproductFrame = tkinter.Frame(self.myFeedMainFrame_inner, width=200, height=290, bg="white", bd=0)
        # self.myFeedproductFrame.place(x=25, y=10)
        #
        # # self.tempImg = tkinter.PhotoImage(file="./imgs/testProduct.png")
        # self.temp_img = Image.open("./imgs/testProduct.png")
        # self.temp_re = self.temp_img.resize((200, 200))
        # self.tkimg = ImageTk.PhotoImage(self.temp_re)
        #
        # self.myFeedproductLabel_img = tkinter.Label(self.myFeedproductFrame, bg="white", image=self.tkimg)
        # self.myFeedproductLabel_img.place(x=0, y=0)
        # self.myFeedproductLabel_price = tkinter.Label(self.myFeedproductFrame, height=1, bg="gray", bd=0, padx=0,
        #                                               text=f"{format(10000, ",")}원", font=("맑은 고딕", 14, "bold"))
        # self.myFeedproductLabel_price.place(x=0, y=210)
        # self.myFeedproductLabel_name = tkinter.Label(self.myFeedproductFrame, width=1, height=2, bg="white",
        #                                              text=f"{"상품명\n상품명"}", font=("맑은 고딕", 11, "bold"))
        # self.myFeedproductLabel_name.place(x=0, y=240)

        # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 판매 내역
        self.mySellListFrame = tkinter.Frame(self.window, width=500, height=685, bg="white")
        self.mySellListFrame.place(x=0, y=0)  # 삭제혹은수정
        self.mySellListFrame.lower()
        # self.myFeedFrame.lift()

        # 판매 내역
        self.mySellListFrame_top = tkinter.Frame(self.mySellListFrame, width=500, height=50, bg="white", bd=0)
        self.mySellListFrame_top.place(x=0, y=0)

        self.mySellListBackLabel = tkinter.Label(self.mySellListFrame_top, bg='white', border=0,
                                             text="〈", font=("맑은 고딕", 17, 'bold'))
        self.mySellListBackLabel.place(x=20, y=7)
        self.mySellListBackLabel.bind("<Button-1>", lambda event, frame=self.mySellListFrame: self.lower(event, frame))

        self.mySellListNameLabel = tkinter.Label(self.mySellListFrame_top, bg='white', border=0,
                                             text="내 상품관리", font=("맑은 고딕", 15, 'bold'))
        self.mySellListNameLabel.place(x=50, y=10)

        #  판매 내역 중앙 메인
        self.mySellListMainFrame = tkinter.Frame(self.mySellListFrame, width=500, height=635, bg='white')
        self.mySellListScrollFrame = ScrollFrame(self, self.mySellListMainFrame)
        self.mySellListMainFrame_inner = tkinter.Frame(self.mySellListScrollFrame.viewPort, width=500, height=635, bg="white")
        self.mySellListMainFrame.place(x=0, y=50)
        self.mySellListScrollFrame.pack()
        self.mySellListMainFrame_inner.pack()
        self.mySellListScrollFrame.canvas.configure(height=635)
        self.mySellListMainFrame_inner.configure(height=1000)

    def openMyFeed(self, e):
        self.myFeedFrame.lift()
        for widget in self.myFeedMainFrame_inner.winfo_children():
            widget.place_forget()

        sendMsg = ["refreshMyFeed", user_id]
        sock.send(pickle.dumps(sendMsg))

        data_len = pickle.loads(sock.recv(2048))
        recvMsg = b''
        if data_len[0] == "refreshMyFeed":
            while data_len[1] > len(recvMsg):
                temp_data = sock.recv(8192)
                recvMsg += temp_data

            recvMsg = pickle.loads(recvMsg)

        try:
            for i in range(len(recvMsg)):
                self.x = 30 + 200 * (i % 2)
                self.y = 20 + 315 * (i // 2)
                if i%2 == 1:
                    self.x += (40)
                self.myFeedproductFrame = tk.Frame(self.myFeedMainFrame_inner, width=200, height=290, bg="white")
                if recvMsg[i][-1] == "판매완료":
                    tk_img = tkinter.PhotoImage(file=complete_img_filepath)
                else:
                    image = Image.open(io.BytesIO(recvMsg[i][11]))
                    image = image.resize((200, 200))
                    tk_img = ImageTk.PhotoImage(image)

                self.myFeedproductLabel_img = tk.Label(self.myFeedproductFrame, width=200, height=200, bd=0)
                self.myFeedproductLabel_img.config(image=tk_img)
                self.myFeedproductLabel_img.image = tk_img
                self.myFeedproductLabel_price = tk.Label(self.myFeedproductFrame, height=1, bg="white", text=f"{format(int(recvMsg[i][5]), ",")}원",
                                           font=("맑은 고딕", 14, "bold"), anchor="w")


                self.myFeedproductLabel_name = ttk.Label(self.myFeedproductFrame, width=22, text=f"{truncate_text(recvMsg[i][1])}", font=("맑은 고딕", 11))
                self.myFeedproductLabel_name.configure(background="white")
                self.myFeedproductLabel_name.configure(wraplength=200, anchor="w")
                self.myFeedproduct_addr = tk.Label(self.myFeedproductFrame, height=1, text=f"{recvMsg[i][9]}", font=("맑은 고딕", 10), fg="gray",
                                          bg="white")
                self.myFeedproduct_addr.place(x=0, y=265)
                self.myFeedproductLabel_name.place(x=0, y=240)
                self.myFeedproductLabel_price.place(x=0, y=210)

                self.myFeedproductLabel_img.place(x=0, y=0)
                self.myFeedproductFrame.place(x=self.x, y=self.y)
                # 상품 클릭시
                self.myFeedproductFrame.bind("<Button-1>", lambda event, sinfo_list=recvMsg[i]: self.sale_click(event, sinfo_list))
                sales_dic[str(self.myFeedproductFrame).split(".!")[-1]] = recvMsg[i]
                if self.y + 330 < 635:
                    self.myFeedMainFrame_inner.configure(height=635)
                else:
                    self.myFeedMainFrame_inner.configure(height=self.y + 330)

        except Exception as ex:
            print(ex, "내 피드 불러오기 실패")

    def openMySellList(self, e):
        self.mySellListFrame.lift()
        for widget in self.mySellListMainFrame_inner.winfo_children():
            widget.place_forget()

        sendMsg = ["refreshMySellList", user_id]
        sock.send(pickle.dumps(sendMsg))

        data_len = pickle.loads(sock.recv(2048))
        recvMsg = b''
        if data_len[0] == "refreshMySellList":
            while data_len[1] > len(recvMsg):
                temp_data = sock.recv(8192)
                recvMsg += temp_data

            recvMsg = pickle.loads(recvMsg)

        try:
            for i in range(len(recvMsg)):
                self.x = 30 + 200 * (i % 2)
                self.y = 20 + 315 * (i // 2)
                if i%2 == 1:
                    self.x += (40)
                self.mySellListproductFrame = tk.Frame(self.mySellListMainFrame_inner, width=200, height=290, bg="white")
                if recvMsg[i][-1] == "판매완료":
                    tk_img = tkinter.PhotoImage(file=complete_img_filepath)
                else:
                    image = Image.open(io.BytesIO(recvMsg[i][11]))
                    image = image.resize((200, 200))
                    tk_img = ImageTk.PhotoImage(image)

                self.mySellListproductLabel_img = tk.Label(self.mySellListproductFrame, width=200, height=200, bd=0)
                self.mySellListproductLabel_img.config(image=tk_img)
                self.mySellListproductLabel_img.image = tk_img
                self.mySellListproductLabel_price = tk.Label(self.mySellListproductFrame, height=1, bg="white", text=f"{format(int(recvMsg[i][5]), ",")}원",
                                           font=("맑은 고딕", 14, "bold"), anchor="w")


                self.mySellListproductLabel_name = ttk.Label(self.mySellListproductFrame, width=22, text=f"{truncate_text(recvMsg[i][1])}", font=("맑은 고딕", 11))
                self.mySellListproductLabel_name.configure(background="white")
                self.mySellListproductLabel_name.configure(wraplength=200, anchor="w")
                self.mySellListproduct_addr = tk.Label(self.mySellListproductFrame, height=1, text=f"{recvMsg[i][9]}", font=("맑은 고딕", 10), fg="gray",
                                          bg="white")
                self.mySellListproduct_addr.place(x=0, y=265)
                self.mySellListproductLabel_name.place(x=0, y=240)
                self.mySellListproductLabel_price.place(x=0, y=210)

                self.mySellListproductLabel_img.place(x=0, y=0)
                self.mySellListproductFrame.place(x=self.x, y=self.y)
                # 상품 클릭시
                self.mySellListproductFrame.bind("<Button-1>", lambda event, sinfo_list=recvMsg[i]: self.sale_click(event, sinfo_list))
                sales_dic[str(self.mySellListproductFrame).split(".!")[-1]] = recvMsg[i]
                if self.y + 330 < 635:
                    self.mySellListMainFrame_inner.configure(height=635)
                else:
                    self.mySellListMainFrame_inner.configure(height=self.y + 330)

        except Exception as ex:
            print(ex, "내 피드 불러오기 실패")


    # 비슷한 카테고리 제품 불러오기
    def loadRecentCategory(self):
        product_list = []
        sendMsg = ["loadRecentCategory"]
        sock.send(pickle.dumps(sendMsg))

        recvMsg = b''
        data_len = pickle.loads(sock.recv(2048))
        #print(data_len)
        if data_len[0] == "loadRecentCategory":
            while data_len[1] > len(recvMsg):
                temp_data = sock.recv(2048)
                recvMsg += temp_data

            recvMsg = pickle.loads(recvMsg)
        #print(list(recvMsg), "+++++recvMsg")

        for i in list(recvMsg):
            if "판매완료" in i:
                continue
            product_list.append(i)
        return product_list

    def refresh_recentCategoryFrame(self, e):
        # 최근 본 상품과 비슷한 제품들 (카테고리)
        # 최근 카테고리 불러오기
        self.recentCategory_List = self.loadRecentCategory()

        # 제품1 정보 : self.self.recentCategory_List[0]
        # 제품2 정보 : self.self.recentCategory_List[1]
        # 제품3 정보 : self.self.recentCategory_List[2]

        self.recentCategoryFrame_center.forget()

        try:
            # 제품 프레임
            self.recentCategoryFrame_center = tkinter.Frame(self.recentCategoryFrame, bg='white', border=0, width=500,
                                                            height=263)
            self.recentCategoryFrame_center.pack(pady=10)

            # 제품1
            self.recentCatgoryTuple_product1 = self.recentCategory_List[0]

            self.recentCategoryLabel_product1 = tkinter.Frame(self.recentCategoryFrame_center, bg='white', border=0,
                                                              width=143, height=263)
            self.recentCategoryLabel_product1.bind("<Button-1>", lambda event, sinfo_list=self.recentCatgoryTuple_product1:
                                                self.main_sales_click(event, sinfo_list))
            self.recentCategoryLabel_product1.pack(side='left', padx=10)

            self.rcl_product1Label_img = tkinter.Label(self.recentCategoryLabel_product1, bg='white', border=0)
            # self.rcl_product1Img = tkinter.PhotoImage(file="./imgs/home_center/testProduct.png")

            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            self.rcl_product1Img_binary = Image.open(io.BytesIO(self.recentCatgoryTuple_product1[11]))
            self.rcl_product1Img_binary = self.rcl_product1Img_binary.resize((143, 176))
            self.rcl_product1Img = ImageTk.PhotoImage(self.rcl_product1Img_binary)
            # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

            self.rcl_product1Label_img.configure(image=self.rcl_product1Img)
            self.rcl_product1Label_img.place(x=0, y=0)

            self.rcl_product1Label_price = tkinter.Label(self.recentCategoryLabel_product1, bg='white', border=0)
            self.rcl_product1Label_price.configure(font=("맑은 고딕", 14, "bold"),
                                                   text=f"{format(int(self.recentCatgoryTuple_product1[5]), ',')}원")
            self.rcl_product1Label_price.place(x=0, y=182)
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            self.rcl_product1Label_like_img = tk.PhotoImage(file="imgs/sale_info/like.PNG")
            self.rcl_product1Label_like = tk.Label(self.recentCategoryLabel_product1, background="white", border=0)
            self.rcl_product1Label_like.configure(image=self.rcl_product1Label_like_img, width=25, height=29)
            self.rcl_product1Label_like.bind("<Button-1>", self.like_click)
            self.rcl_product1Label_like.place(x=113, y=182)
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            self.product1_name = self.recentCatgoryTuple_product1[1]
            self.product1_name = truncate_text(self.product1_name)
            self.rcl_product1Label_name = tkinter.Label(self.recentCategoryLabel_product1, bg='white', border=0)
            self.rcl_product1Label_name.configure(fg="#676767", font=("맑은 고딕", 11, "bold"), text=f"{self.product1_name}"
                                                  , wraplength=143, justify='left')
            self.rcl_product1Label_name.place(x=0, y=210)

            # 제품2
            self.recentCatgoryTuple_product2 = self.recentCategory_List[1]

            self.recentCategoryLabel_product2 = tkinter.Frame(self.recentCategoryFrame_center, bg='white', border=0,
                                                              width=143, height=263)
            self.recentCategoryLabel_product2.bind("<Button-1>", lambda event, sinfo_list=self.recentCatgoryTuple_product2:
                                                self.main_sales_click(event, sinfo_list))
            self.recentCategoryLabel_product2.pack(side='left', padx=10)

            self.rcl_product2Label_img = tkinter.Label(self.recentCategoryLabel_product2, bg='white', border=0)
            # self.rcl_product2Img = tkinter.PhotoImage(file="./imgs/home_center/testProduct2.png")

            self.rcl_product2Img_binary = Image.open(io.BytesIO(
                self.recentCatgoryTuple_product2[11]))  # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            self.rcl_product2Img_binary = self.rcl_product2Img_binary.resize((143, 176))
            self.rcl_product2Img = ImageTk.PhotoImage(self.rcl_product2Img_binary)

            self.rcl_product2Label_img.configure(image=self.rcl_product2Img)
            self.rcl_product2Label_img.place(x=0, y=0)

            self.rcl_product2Label_price = tkinter.Label(self.recentCategoryLabel_product2, bg='white', border=0)
            self.rcl_product2Label_price.configure(font=("맑은 고딕", 14, "bold"),
                                                   text=f"{format(int(self.recentCatgoryTuple_product2[5]), ',')}원")
            self.rcl_product2Label_price.place(x=0, y=182)
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            self.rcl_product2Label_like_img = tk.PhotoImage(file="imgs/sale_info/like.PNG")
            self.rcl_product2Label_like = tk.Label(self.recentCategoryLabel_product2, background="white", border=0)
            self.rcl_product2Label_like.configure(image=self.rcl_product2Label_like_img, width=25, height=29)
            self.rcl_product2Label_like.bind("<Button-1>", self.like_click)
            self.rcl_product2Label_like.place(x=113, y=182)
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            self.product2_name = self.recentCatgoryTuple_product2[1]
            self.product2_name = truncate_text(self.product2_name)
            self.rcl_product2Label_name = tkinter.Label(self.recentCategoryLabel_product2, bg='white', border=0)
            self.rcl_product2Label_name.configure(fg="#676767", font=("맑은 고딕", 11, "bold"), text=f"{self.product2_name}"
                                                  , wraplength=143, justify='left')
            self.rcl_product2Label_name.place(x=0, y=210)

            # 제품3
            self.recentCatgoryTuple_product3 = self.recentCategory_List[2]

            self.recentCategoryLabel_product3 = tkinter.Frame(self.recentCategoryFrame_center, bg='white', border=0,
                                                              width=143, height=263)
            self.recentCategoryLabel_product3.bind("<Button-1>", lambda event, sinfo_list=self.recentCatgoryTuple_product3:
                                                self.main_sales_click(event, sinfo_list))
            self.recentCategoryLabel_product3.pack(side='left', padx=10)

            self.rcl_product3Label_img = tkinter.Label(self.recentCategoryLabel_product3, bg='white', border=0)
            # self.rcl_product3Img = tkinter.PhotoImage(file="./imgs/home_center/testProduct3.png")

            self.rcl_product3Img_binary = Image.open(io.BytesIO(
                self.recentCatgoryTuple_product3[11]))  # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            self.rcl_product3Img_binary = self.rcl_product3Img_binary.resize((143, 176))
            self.rcl_product3Img = ImageTk.PhotoImage(self.rcl_product3Img_binary)

            self.rcl_product3Label_img.configure(image=self.rcl_product3Img)
            self.rcl_product3Label_img.place(x=0, y=0)

            self.rcl_product3Label_price = tkinter.Label(self.recentCategoryLabel_product3, bg='white', border=0)
            self.rcl_product3Label_price.configure(font=("맑은 고딕", 14, "bold"),
                                                   text=f"{format(int(self.recentCatgoryTuple_product3[5]), ',')}원")
            self.rcl_product3Label_price.place(x=0, y=182)
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            self.rcl_product3Label_like_img = tk.PhotoImage(file="imgs/sale_info/like.PNG")
            self.rcl_product3Label_like = tk.Label(self.recentCategoryLabel_product3, background="white", border=0)
            self.rcl_product3Label_like.configure(image=self.rcl_product3Label_like_img, width=25, height=29)
            self.rcl_product3Label_like.bind("<Button-1>", self.like_click)
            self.rcl_product3Label_like.place(x=113, y=182)
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            self.product3_name = self.recentCatgoryTuple_product3[1]
            self.product3_name = truncate_text(self.product3_name)
            self.rcl_product3Label_name = tkinter.Label(self.recentCategoryLabel_product3, bg='white', border=0)
            self.rcl_product3Label_name.configure(fg="#676767", font=("맑은 고딕", 11, "bold"), text=f"{self.product3_name}"
                                                  , wraplength=143, justify='left')
            self.rcl_product3Label_name.place(x=0, y=210)
        except:
            pass


    # my 화면
    def openMySaleFrame(self, e):
        self.mySaleFrame.lift()
        self.myPurFrame.lower()
        self.myETCFrame.place_configure(y=350)

    def openMyPurFrame(self, e):
        self.myPurFrame.lift()
        self.mySaleFrame.lower()
        self.myETCFrame.place_configure(y=250)

    # def loadStoreNameFunc(self):
    #     print("아이디 불러오기")
    #     sendMsg = ["loadStoreName"]
    #     sock.send(pickle.dumps(sendMsg))
    #     recvMsg = pickle.loads(sock.recv(1024))
    #     if recvMsg[0] == "loadStoreName":
    #         print(recvMsg)
    #         return recvMsg[1]

    def loadMySale(self):
        print("금액 불러오기")
        sendMsg = ["loadSale", ""]
        sock.send(pickle.dumps(sendMsg))
        recvMsg = pickle.loads(sock.recv(1024))
        #print(recvMsg)
        if recvMsg[0] == "loadSale":
            if recvMsg[1] == "fail":
                tkinter.messagebox.showerror("에러", "올해 번 금액을 불러오는데 실패했습니다.")
            #print(recvMsg)
            return recvMsg[2]

    def openEditInform(self, e, window):
        self.editInformWindow = EditInform(window)
        openFrame(self.editInformWindow.editMainFrame)

    def logout(self, e):
        sock.send(pickle.dumps(["!disconnect"]))
        self.window.destroy()



    def lower(self, e, frame):
        frame.lower()
#######################################
    # 메인 하단 번개톡 버튼
    def main_bot_talk(self,e):
        self.openMainFrames(e, self.main_talk, self.chatListButton)
        try:
            talk_fetchall = ()
            sendMsg = ["chat_list"]
            sock.send(pickle.dumps(sendMsg))
            data_len = pickle.loads(sock.recv(1024))
            if data_len[0] == "chat_list":
                recvMsg = b''
                while data_len[1] > len(recvMsg):
                    temp_data = sock.recv(1024)
                    recvMsg += temp_data

                talk_fetchall = pickle.loads(recvMsg)
        except Exception as ex:
            print(ex)
        for i in range(len(talk_fetchall)):
            self.x = 0
            self.y = 200 + 100 * i
            # 각각의 톡 프레임
            self.main_talk_frame = tk.Frame(self.main_talk_scroll_view, width=500, height=90, bd=0, background="white")
            self.main_talk_frame.bind("<Button-1>", self.lightningtalk_info)
            self.main_talk_frame.place(x=0, y=self.y)
            # 상대의 프로필사진
            self.main_talk_profile_img = tk.PhotoImage(file="imgs/talk/profile.PNG")
            self.main_talk_profile = ttk.Label(self.main_talk_frame, image=self.main_talk_profile_img, border=0,
                                               background="white")
            self.main_talk_profile.image = self.main_talk_profile_img
            self.main_talk_profile.place(x=17, y=17)

            self.main_talk.user_list = talk_fetchall[i]
            self.main_talk.user_label = ttk.Label(self.main_talk_frame, text=f"{self.main_talk.user_list[0][0]}", border=0,
                                                  background="white")
            self.main_talk.user_label.config(font=("맑은 고딕", 15, "bold"))
            self.main_talk.user_label.place(x=85, y=12)
            # 내용
            self.main_talk_contents = ttk.Label(self.main_talk_frame, text="내용", border=0, background="white")
            self.main_talk_contents.config(font=("맑은 고딕", 11), foreground="gray")
            self.main_talk_contents.place(x=85, y=50)
            # 상품 이미지
            main_talk_sale_img = Image.open(io.BytesIO(self.main_talk.user_list[0][11]))
            main_talk_sale_img = main_talk_sale_img.resize((35, 35))
            info_tk_img = ImageTk.PhotoImage(main_talk_sale_img)
            self.main_talk_sale = ttk.Label(self.main_talk_frame, border=0, background="white")
            self.main_talk_sale.config(image=info_tk_img)
            self.main_talk_sale.image = info_tk_img
            self.main_talk_sale.place(x=400, y=25)

            self.main_talk_sale_name = tk.Label(self.main_talk_frame, text=self.main_talk.user_list[0][1])
################################################
    # 찜 화면과 최근 본 상품 화면
    def openFrame_like(self, frame):
        frame.tkraise()
        self.like_btn.configure(font=("맑은 고딕", 16, "bold", "underline"))
        self.recent_btn.configure(font=("맑은 고딕", 16, "bold"))

    def openFrame_recent(self, frame):
        frame.tkraise()
        self.like_btn.configure(font=("맑은 고딕", 16, "bold"))
        self.recent_btn.configure(font=("맑은 고딕", 16, "bold", "underline"))

    #  로그인한 계정의 첫번째 검색창
    def openFrame_search_win(self, frame):
        frame.tkraise()
        openFrame(self.search_bot)
        for widget in self.recent_frame_mini.winfo_children():
            widget.forget()
        for widget in self.rank_frame.winfo_children():
            widget.forget()
        # 많이 검색된 단어
        for i in range(len(self.search_top_count())):
            #print(self.search_top_count())
            self.top_border = tk.Frame(self.rank_frame, bg="gainsboro")
            self.top_label = tk.Label(self.top_border, width=13, height=2,
                                      text=f"{self.search_top_count()[i][0]}", font=("맑은 고딕", 13), bg="white",
                                      bd=0, highlightthickness=0, padx=7)
            self.top_label.bind("<Button-1>", self.label_click)
            self.rank_label = tk.Label(self.top_label, text=f"{i + 1}. ", font=("맑은 고딕", 13), bg="white", bd=0,
                                       highlightthickness=0, padx=7)
            self.rank_label.place(x=5, y=11)
            self.top_label.pack(pady=1, padx=1)
            self.top_border.pack(pady=2, padx=8)
        try:
            recent_search = []
            sendMsg = ["recent_search"]
            sock.send(pickle.dumps(sendMsg))
            data_len = pickle.loads(sock.recv(1024))
            if data_len[0] == "recent_search":
                data = b""
                while len(data) < data_len[1]:
                    packet = sock.recv(4096)
                    if not packet:
                        break
                    data += packet
                recent_search = tuple(pickle.loads(data))
        except Exception as ex:
            print("--------------------- 검색어 관련 상품")
            print(ex)
        for i in range(len(recent_search)):
            # 최근 검색어
            if recent_search[i][0] not in self.recent_label_dic.keys():
                self.recent_label_dic[recent_search[i][0]] = tk.Label(self.recent_frame_mini, width=11, height=2,
                                                                      text=recent_search[i][0], font=("맑은 고딕", 13),
                                                                      anchor="w", bg="white", relief="ridge",
                                                                      borderwidth=1,
                                                                      highlightthickness=0, padx=12)
                self.recent_label_dic[recent_search[i][0]].bind("<Button-1>", self.label_click)
                self.recent_label_dic[recent_search[i][0]].place(x=0, y=0)
                self.del_img = tk.PhotoImage(file="imgs/del.png")
                self.recent_del_btn = tk.Label(self.recent_label_dic[recent_search[i][0]], width=12, height=12,
                                               bg="white", bd=0,
                                               image=self.del_img,
                                               cursor="hand2")
                self.recent_del_btn.bind("<Button-1>",
                                         lambda event, button=self.recent_del_btn: self.del_recent(event, button))
                self.recent_del_btn.place(x=110, y=17)
            else:
                self.recent_label_dic[recent_search[i][0]].destroy()
                del self.recent_label_dic[recent_search[i][0]]
                self.recent_label_dic[recent_search[i][0]] = tk.Label(self.recent_frame_mini, width=11, height=2,
                                                                      text=recent_search[i][0], font=("맑은 고딕", 13),
                                                                      anchor="w", bg="white", relief="ridge",
                                                                      borderwidth=1,
                                                                      highlightthickness=0, padx=12)
                self.recent_label_dic[recent_search[i][0]].bind("<Button-1>", self.label_click)
                self.recent_label_dic[recent_search[i][0]].place(x=0, y=0)
                self.del_img = tk.PhotoImage(file="imgs/del.png")
                self.recent_del_btn = tk.Label(self.recent_label_dic[recent_search[i][0]], width=12, height=12,
                                               bg="white", bd=0,
                                               image=self.del_img, cursor="hand2")
                self.recent_del_btn.bind("<Button-1>",
                                         lambda event, button=self.recent_del_btn: self.del_recent(event, button))
                self.recent_del_btn.place(x=110, y=17)
            self.recent_label_list = list(self.recent_label_dic.values())
        for i in range(len(self.recent_label_list)):
            i += 1
            self.recent_label_list[-i].pack(side='left', padx=9)
        # 전체삭제
        if len(self.recent_frame_mini.winfo_children()) >= 1:
            self.all_del_btn = tk.Button(self.recent_frame, text="전체 삭제", fg="gray", cursor="hand2",
                                         font=("맑은 고딕", 10, "underline"),
                                         bd=0, highlightthickness=0, bg="white", command=self.all_del)
            self.all_del_btn.place(x=5, y=90)

    # 메인 화면의 제품 클릭
    # def main_sales_click(self, e, sinfo_list):
    def main_sales_click(self, e, sinfo_list=[]):
        ms_click = ()
        s_id = sinfo_list[0]
        s_name = sinfo_list[1]
        # s_id = "kim1234"
        try:
            # sendMsg = ["main_sales_click", e.widget.winfo_children()[2].cget('text')[:-3]]
            sendMsg = ["main_sales_click", s_id, s_name]
            sock.send(pickle.dumps(sendMsg))

            data_len = pickle.loads(sock.recv(1024))
            if data_len[0] == "main_sales_click":

                data = b""
                while len(data) < data_len[1]:
                    packet = sock.recv(4096)
                    if not packet:
                        break
                    data += packet

                ms_click = pickle.loads(data)

        except Exception as ex:
            print("--------------------- main sales click")
            print(ex)

        sales_dic[str(e.widget).split(".!")[-1]] = list(ms_click[0])
        # 제품명이 생략되어있다면
        if e.widget.winfo_children()[2].cget("text")[-3:] == "...":
            for i in range(len(self.recent_sale)):
                if e.widget.winfo_children()[2].cget("text")[:-3] in self.recent_sale[i].winfo_children()[2].cget(
                        "text"):
                    e.widget.winfo_children()[2].configure(text=self.recent_sale[i].winfo_children()[2].cget("text"))
        self.recent_count = 0
        if len(self.recent_sale) == 0:
            self.recent_sale.insert(0, e.widget)
        else:
            for i in range(len(self.recent_sale)):
                if e.widget.winfo_children()[2].cget("text") == self.recent_sale[i].winfo_children()[2].cget("text"):
                    del self.recent_sale[i]
                    self.recent_sale.insert(0, e.widget)
                    self.recent_count += 1
            if self.recent_count == 0:
                self.recent_sale.insert(0, e.widget)
        self.click_label = str(e.widget).split(".!")[-1]
        if self.click_label in sales_dic.keys():
            # 메인 화면 상품 상세 페이지
            self.sale_info = tk.Frame(self.window, width=500, height=750, bd=0, bg="white")
            self.sale_info.place(x=0, y=0)
            # 상품 상세 페이지 상단
            self.sale_info_top = tk.Label(self.sale_info, width=500, height=3, bd=0, bg="white")
            self.sale_info_top.place(x=0, y=0)
            # 이전 버튼
            self.info_back_img = tk.PhotoImage(file="imgs/back.png")
            self.info_back = tk.Label(self.sale_info_top, width=25, height=29, image=self.info_back_img, bg="white",
                                      cursor="hand2")
            self.info_back.bind("<Button-1>", lambda event: self.lower(event, self.sale_info))
            # 홈 버튼
            self.info_home_img = tk.PhotoImage(file="imgs/home.png")
            self.info_home = tk.Label(self.sale_info_top, width=25, height=29, image=self.info_home_img, bg="white",
                                      cursor="hand2")
            self.info_home.bind("<Button-1>", lambda event: self.openFrame(self.homeFrame))
            self.info_search_img = tk.PhotoImage(file="imgs/home_top/searchButton.png").subsample(1, 1)
            self.info_search = tk.Label(self.sale_info_top, width=25, height=29, image=self.info_search_img, bg="white",
                                        cursor="hand2")
            self.info_search.bind("<Button-1>", lambda event: self.openFrame(self.search_window))
            self.info_search.place(x=450, y=8)
            self.info_home.place(x=400, y=8)
            self.info_back.place(x=18, y=8)

            # 상품 중앙 페이지
            self.sale_info_mid = tk.Frame(self.sale_info, bd=0)
            self.sale_info_mid.place(x=0, y=45)
            self.sale_info_scroll = ScrollFrame(self, self.sale_info_mid)
            self.sale_info_frame = tk.Frame(self.sale_info_scroll.viewPort, height=1500, bd=0, bg="white")
            self.sale_info_frame.pack()

            self.info_image_list = []
            self.info_image_list_index = 0
            self.j = 11
            while self.j < 15:
                if sales_dic[self.click_label][self.j] != None:
                    self.info_image_list.append(sales_dic[self.click_label][self.j])
                self.j += 1

            info_image_list_first = Image.open(io.BytesIO(self.info_image_list[self.info_image_list_index]))
            info_image_list_first = info_image_list_first.resize((370, 300))
            info_tk_img = ImageTk.PhotoImage(info_image_list_first)
            # 상품 이미지
            self.info_image = tk.Label(self.sale_info_frame, bd=0, bg="gainsboro")
            self.info_image.config(image=info_tk_img)
            self.info_image.image = info_tk_img
            self.info_image.pack()


            # 상품명
            self.info_name = ttk.Label(self.sale_info_frame, border=0, text=f"{sales_dic[self.click_label][1]}",
                                       background="white")
            self.info_name.configure(font=("맑은 고딕", 14), wraplength=500, anchor="w")
            self.info_name.pack(anchor="w", padx=15, pady=10)
            # self.info_name.place(x=20,y=310)
            # 가격
            self.info_price = ttk.Label(self.sale_info_frame, border=0,
                                        text=f"{format(int(sales_dic[self.click_label][5]), ',')}원",
                                        anchor="w", background="white")
            self.info_price.configure(font=("맑은 고딕", 17, "bold"))
            self.info_price.pack(anchor="w", padx=15)
            # self.info_price.place(x=20,y=340)
            # 가격 제안
            self.info_price_offer_img = tk.PhotoImage(file="imgs/sale_info/price offer.png")
            self.info_price_offer = ttk.Label(self.sale_info_frame, border=0, image=self.info_price_offer_img,
                                              background="white")
            self.info_price_offer.pack(anchor="w", padx=12, pady=3)
            # 주소, 등록시간
            self.info_addr = ttk.Label(self.sale_info_frame, border=0, text=f"{sales_dic[self.click_label][9]}",
                                       anchor="w", background="white")
            self.info_addr.configure(font=("맑은 고딕", 11), foreground="gray")
            self.info_addr.pack(anchor="w", padx=12, pady=3)
            # self.info_addr.place(x=20,y=380)
            # 번개케어, 결제혜택
            self.info_fill_img = tk.PhotoImage(file="imgs/sale_info/care.PNG")
            self.info_fill = ttk.Label(self.sale_info_frame, border=0, image=self.info_fill_img, background="white")
            self.info_fill.pack(anchor="w", padx=15, pady=3)

            # 상세정보 라벨
            self.info_detail_label = ttk.Label(self.sale_info_frame, border=0, text="상세 정보", anchor="w",
                                               background="white")
            self.info_detail_label.configure(font=("맑은 고딕", 14, "bold"))
            self.info_detail_label.pack(anchor="w", padx=15, pady=10)
            # self.info_detail_label.place(x=20,y=420)

            # 카테고리 라벨
            self.info_detail_category_label = tk.Label(self.sale_info_frame, border=0, background="white", text="카테고리")
            self.info_detail_category_label.configure(font=("맑은 고딕", 13), width=20, height=1, anchor="w",
                                                      foreground="gray")
            self.info_detail_category_label.pack(anchor="w", padx=15, pady=3)
            # 카테고리 정보
            self.info_detail_category = tk.Label(self.info_detail_category_label, border=0, background="white",
                                                 text=f"{sales_dic[self.click_label][2]}")
            self.info_detail_category.configure(anchor="e", font=("맑은 고딕", 11))
            self.info_detail_category.bind("<Button-1>", self.info_category_click)
            self.info_detail_category.place(x=90, y=2)
            # 상품상태 라벨
            self.info_detail_state_label = tk.Label(self.sale_info_frame, bd=0, bg="white", text="상품상태")
            self.info_detail_state_label.configure(font=("맑은 고딕", 13), width=20, height=1, anchor="w",
                                                   foreground="gray")
            self.info_detail_state_label.pack(anchor="w", padx=15, pady=3)
            # 상품상태 정보
            self.info_detail_state = tk.Label(self.info_detail_state_label, border=0, background="white",
                                              text=f"{sales_dic[self.click_label][3]}")
            self.info_detail_state.configure(anchor="e", font=("맑은 고딕", 11))
            self.info_detail_state.place(x=90, y=2)
            # 수량 라벨
            self.info_detail_count_label = tk.Label(self.sale_info_frame, bd=0, bg="white", text="수량")
            self.info_detail_count_label.configure(font=("맑은 고딕", 13), width=20, height=1, anchor="w",
                                                   foreground="gray")
            self.info_detail_count_label.pack(anchor="w", padx=15, pady=3)
            # 수량 정보
            self.info_detail_count = tk.Label(self.info_detail_count_label, border=0, background="white",
                                              text=f"{sales_dic[self.click_label][7]}")
            self.info_detail_count.configure(anchor="e", font=("맑은 고딕", 11))
            self.info_detail_count.place(x=90, y=2)

            # 상세정보 내용
            self.info_detail = ttk.Label(self.sale_info_frame, border=0, text=f"{sales_dic[self.click_label][10]}",
                                         anchor="w", background="white")
            self.info_detail.configure(font=("맑은 고딕", 14), wraplength=500)
            self.info_detail.pack(anchor="w", padx=15, pady=20)
            # self.info_detail.place(x=20,y=460)

            # 배송비 라벨
            self.info_delivery_label = ttk.Label(self.sale_info_frame, border=0, text="배송비", anchor="w",
                                                 background="white")
            self.info_delivery_label.configure(font=("맑은 고딕", 13, "bold"))
            self.info_delivery_label.pack(anchor='w', padx=15, pady=5)

            # 배송비
            self.info_delivery = ttk.Label(self.sale_info_frame, border=0, text=f"{sales_dic[self.click_label][6]}원",
                                           anchor="w", background="white")
            self.info_delivery.configure(font=("맑은 고딕", 13))
            self.info_delivery.pack(anchor='w', padx=15)

            # 스크롤에 height를 배송비 좌표를 구해 y를 한 50정도 +해서 배치하고
            # 해시태그의 시작지점을 배송비의 아래 오른쪽 적당한 곳에 설정
            # 해시태그
            self.tag_frame = ttk.Label(self.sale_info_frame, background="white", border=0, anchor="w", width=500)
            self.tag_frame.configure(font=("맑은 고딕", 12))
            for i in range(len(sales_dic[self.click_label][4].split(","))):
                self.hashtag = sales_dic[self.click_label][4].split(",")[i]
                self.tag_x = 0 + 80 * (i % 4)
                self.tag_y = 0 + 50 * (i // 4)
                self.info_tag = tk.Label(self.tag_frame, bd=1, text=f"{self.hashtag}", bg="whitesmoke")
                self.info_tag.configure(font=("맑은 고딕", 12), fg="gray", padx=2)
                self.info_tag.bind("<Button-1>", self.hashtag_click)
                self.info_tag.place(x=self.tag_x, y=self.tag_y)
            self.tag_frame.pack(anchor='w', padx=15, pady=20)
################################################
            if len(self.info_image_list) >= 2:
                # 이미지 변경할 화살표
                # 왼쪽
                self.info_image_left_img = tk.PhotoImage(file="imgs/sale_info/image_left.png")
                self.info_image_left = ttk.Label(self.sale_info_frame, image=self.info_image_left_img, border=0,
                                                 background="white")
                self.info_image_left.bind("<Button-1>", self.info_image_change_left)
                self.info_image_left.place(x=15, y=125)
                # 오른쪽
                self.info_image_right_img = tk.PhotoImage(file="imgs/sale_info/image_right.png")
                self.info_image_right = ttk.Label(self.sale_info_frame, image=self.info_image_right_img,
                                                  border=0, background="white")
                self.info_image_right.bind("<Button-1>", self.info_image_change_right)
                self.info_image_right.place(x=450, y=125)

####################################################
            if user_id != s_id:
                # 구매자용 상품 하단 페이지
                self.sale_info_bot = tk.Frame(self.sale_info, width=500, height=70, bd=0, bg="white")
                self.sale_info_bot.place(x=0, y=680)
                # 번개톡
                self.info_talk_img = tk.PhotoImage(file="imgs/sale_info/talk.PNG")
                self.info_talk = tk.Label(self.sale_info_bot, width=125, height=45, image=self.info_talk_img)
                self.info_talk.bind("<Button-1>", self.info_talk_click)
                self.info_talk.place(x=110, y=8)
                # 결재
                self.info_pay_img = tk.PhotoImage(file="imgs/sale_info/pay.PNG")
                self.info_pay = tk.Label(self.sale_info_bot, width=190, height=45, image=self.info_pay_img)
                self.info_pay.bind("<Button-1>", lambda event: self.pay_click(event, self.sale_info_frame))
                self.info_pay.place(x=270, y=8)
                # 찜버튼
                self.info_like_img = tk.PhotoImage(file="imgs/sale_info/like.PNG")
                self.info_like = tk.Label(self.sale_info_bot, width=25, height=29, image=self.info_like_img, bg="white")
#################################################
                self.info_like.bind("<Button-1>", self.sale_info_like_click)
                self.info_like.place(x=26, y=16)
            else:
                # 판매자용 상품 하단 페이지
                self.sale_info_bot2 = tk.Frame(self.sale_info, width=500, height=70, bd=0, bg="white")
                self.sale_info_bot2.place(x=0,y=680)
                # up하기
                self.info2_up_img = tk.PhotoImage(file="imgs/sale_info/seller/up.PNG")
                self.info2_up = ttk.Label(self.sale_info_bot2, border=0, background="white",image=self.info2_up_img)
                self.info2_up.place(x=10,y=14)
                # 광고하기
                self.info2_ad_img = tk.PhotoImage(file="imgs/sale_info/seller/ad.PNG")
                self.info2_ad = ttk.Label(self.sale_info_bot2, border=0, background="white", image=self.info2_ad_img)
                self.info2_ad.place(x=122, y=14)
                # 배송신청
                self.info2_delivery_img = tk.PhotoImage(file="imgs/sale_info/seller/delivery.PNG")
                self.info2_delivery = ttk.Label(self.sale_info_bot2, border=0, background="white", image=self.info2_delivery_img)
                self.info2_delivery.place(x=253, y=14)
                # 상태 변경
                self.info2_state_img = tk.PhotoImage(file="imgs/sale_info/seller/state.PNG")
                self.info2_state = ttk.Label(self.sale_info_bot2, border=0, background="white", image=self.info2_state_img)
                self.info2_state.bind("<Button-1>", self.seller_state_change)
                self.info2_state.place(x=370, y=10)



        # if self.recent:
        #    self.recent.forget(self.recent)

        self.sale_info_scroll.pack(side="top", fill="both", expand=True)
        openFrame(self.sale_info)

    # 번개톡 화면의 대화창 클릭
    def lightningtalk_info(self, e):
        try:
            sendMsg = ["chat_window_frame", e.widget.winfo_children()[-1].cget("text")]
            sock.send(pickle.dumps(sendMsg))
            data_len = pickle.loads(sock.recv(1024))
            if data_len[0] == "chat_window_frame":
                recvMsg = b''
                while data_len[1] > len(recvMsg):
                    temp_data = sock.recv(1024)
                    recvMsg += temp_data
                chat_check = pickle.loads(recvMsg)
        except Exception as ex:
            print(ex)
        #print(chat_check[1][1])
        self.talk_info_frame = tk.Frame(self.window, width=500, height=750, bd=0, bg="white")
        self.talk_info_frame.place(x=0, y=0)
        # 상단
        self.talk_info_top = tk.Frame(self.talk_info_frame, width=500, height=125, bd=0, bg="white")
        self.talk_info_top.place(x=0, y=0)
        # 뒤로가기
        self.talk_info_back_img = tk.PhotoImage(file="imgs/back.png")
        self.talk_info_back = ttk.Label(self.talk_info_top, image=self.talk_info_back_img, border=0,
                                        background="white")
        self.talk_info_back.bind("<Button-1>", lambda event: self.lower(event, self.talk_info_frame))
        self.talk_info_back.place(x=10, y=15)

        # 상대 접속 상태
        self.talk_info_user_state = ttk.Label(self.talk_info_top, text="유저 상태", border=0, background="white")
        self.talk_info_user_state.config(font=("맑은 고딕", 10), foreground="gray")
        self.talk_info_user_state.place(x=45, y=32)
        # 점점점
        self.talk_info_dot_img = tk.PhotoImage(file="imgs/talk/dot.PNG")
        self.talk_info_dot = ttk.Label(self.talk_info_top, image=self.talk_info_dot_img, border=0,
                                       background="white")
        self.talk_info_dot.place(x=450, y=12)
        # 상품 이미지
        self.talk_info_sale = ttk.Label(self.talk_info_top, border=0, background="white")
        self.talk_info_sale.config(image=e.widget.winfo_children()[3].cget("image"))
        self.talk_info_sale.place(x=10, y=65)
        # 상품 가격
        self.talk_info_sale_price = ttk.Label(self.talk_info_top, border=0, background="white")
        self.talk_info_sale_price.config(text=f"{chat_check[0][5]}원", font=("맑은 고딕", 12, "bold"))
        self.talk_info_sale_price.place(x=60, y=62)
        # 상품명
        self.talk_info_sale_name = ttk.Label(self.talk_info_top, border=0, background="white")
        self.talk_info_sale_name.config(text=chat_check[0][1], font=("맑은 고딕", 10), foreground="gray")
        self.talk_info_sale_name.place(x=60, y=85)
        # 배송비
        self.talk_info_sale_delivery = ttk.Label(self.talk_info_top, border=0, background="white",
                                                 font=("맑은 고딕", 9), foreground="gray")
        if chat_check[0][6] != "0":
            self.talk_info_sale_delivery.config(text=f"{chat_check[0][6]}원")
        else:
            self.talk_info_sale_delivery.config(text="무료배송")
        self.talk_info_sale_delivery.place(x=60, y=105)
        # 결제버튼
        self.talk_info_pay_img = tk.PhotoImage(file="imgs/talk/pay.PNG")
        self.talk_info_pay = ttk.Label(self.talk_info_top, image=self.talk_info_pay_img, border=0,
                                       background="white")
        self.talk_info_pay.bind("<Button-1>", self.talk_pay_btn)
        self.talk_info_pay.place(x=400, y=62)
        # 중단
        self.talk_info_mid = tk.Frame(self.talk_info_frame, width=500, height=700, bd=0, bg="white")
        self.talk_info_mid.place(x=0, y=125)
        self.talk_info_scroll = ScrollFrame(self, self.talk_info_mid)
        self.talk_info_scroll_view = tk.Frame(self.talk_info_scroll.viewPort, width=500, height=700, bd=0,
                                              bg="white")
        self.talk_info_scroll_view.pack()

        # 상대 프로필
        self.talk_info_user_profile_img = tk.PhotoImage(file="imgs/talk/profile.PNG").zoom(7).subsample(4, 4)
        self.talk_info_user_profile = ttk.Label(self.talk_info_scroll_view, image=self.talk_info_user_profile_img,
                                                border=0, background="white")
        self.talk_info_user_profile.pack(pady=15)
        # 아이디
        self.talk_info_user_id = ttk.Label(self.talk_info_scroll_view, border=0, background="white")
        self.talk_info_user_id.config(font=("맑은 고딕", 17, "bold"))
        self.talk_info_user_id.pack()

        # 날짜
        self.talk_info_day = tk.Label(self.talk_info_scroll_view, bd=0, bg="white", width=70, height=2)
        self.talk_info_day.config(
            text=f"------------------------------------   {datetime.datetime.now().strftime("%Y년 %m월 %d일")}  -----------------------------------")
        self.talk_info_day.config(font=("맑은 고딕", 10), foreground="gray")
        self.talk_info_day.pack(pady=15)
############################################### 대략
        #print(chat_check[1], "chat_check")
        past_chat = pickle.loads(chat_check[1][2])
        #print(past_chat)

        # print(past_chat,"past_chat")
        # 내 상품이 아닌 경우
        if user_id != e.widget.winfo_children()[1].cget("text"):
            print("if")
            try:
                # 대화하는 상대
                self.talk_info_user = ttk.Label(self.talk_info_top, text=chat_check[1][1], border=0, background="white")
                self.talk_info_user.config(font=("맑은 고딕", 15, 'bold'))
                self.talk_info_user.place(x=45, y=0)
                self.talk_info_user_id.config(text=self.talk_info_user.cget("text"))
                for i in range(len(past_chat)):
                    self.past_chat_frame = tk.Frame(self.talk_info_scroll_view, border=0, background="white")
                    self.past_chat_frame.pack(padx=15, pady=10, anchor="e")

                    self.past_chat_label = tk.Label(self.past_chat_frame, text=past_chat[i].split('/')[0], bd=0,
                                                    bg="whitesmoke")
                    self.past_chat_label.config(font=("맑은 고딕", 14, "bold"), fg="black", padx=10, pady=10,
                                                wraplength=200,
                                                justify="left")
                    self.past_chat_label.pack(anchor="e")

                    self.past_time = ttk.Label(self.past_chat_frame, text=past_chat[i].split('/')[1])
                    self.past_time.config(background="white")
                    self.past_time.pack(anchor="e")
            except Exception as ex:
                print(ex)
        else:
            print("else")
            try:
                # 대화하는 상대
                self.talk_info_user = ttk.Label(self.talk_info_top, text=chat_check[1][1], border=0, background="white")
                self.talk_info_user.config(font=("맑은 고딕", 15, 'bold'))
                self.talk_info_user.place(x=45, y=0)
                self.talk_info_user_id.config(text=self.talk_info_user.cget("text"))
                for i in range(len(past_chat)):
                    self.past_chat_frame = tk.Frame(self.talk_info_scroll_view, border=0, background="white")
                    self.past_chat_frame.pack(padx=15, pady=10, anchor="w")

                    self.past_chat_label = tk.Label(self.past_chat_frame, text=past_chat[i].split('/')[0], bd=0,
                                                    bg="whitesmoke")
                    self.past_chat_label.config(font=("맑은 고딕", 14, "bold"), fg="black", padx=10, pady=10,
                                                wraplength=200,
                                                justify="left")
                    self.past_chat_label.pack(anchor="w")

                    self.past_time = ttk.Label(self.past_chat_frame, text=past_chat[i].split('/')[1])
                    self.past_time.config(background="white")
                    self.past_time.pack(anchor="w")
            except Exception as ex:
                print(ex)
###################################################
        # 하단
        self.talk_info_bot = tk.Frame(self.talk_info_frame, width=500, height=40, bd=0, bg="white")
        self.talk_info_bot.place(x=0, y=710)
        # 상품 선택
        self.talk_sale_choice_img = tk.PhotoImage(file="imgs/talk/sale_choice.PNG")
        self.talk_sale_choice = ttk.Label(self.talk_info_bot, image=self.talk_sale_choice_img, border=0,
                                          background="white")
        self.talk_sale_choice.place(x=10, y=2)
        # 텍스트 입력
        self.talk_en_label = tk.Label(self.talk_info_bot, width=50, height=2, bd=0, background="white")
        self.talk_en_label.place(x=55, y=2)
        self.talk_en = tk.Entry(self.talk_en_label, width=30, bd=0, background="white")
        self.talk_en.insert(0, "메시지를 입력하세요.")
        self.talk_en.bind("<Button-1>", self.talk_en_click)
        self.talk_en.bind("<Return>", self.talk_en_enter)
        self.talk_en.config(font=("맑은 고딕", 13), fg="gray")
        self.talk_en.place(x=6, y=2)
        # 이모티콘
        self.talk_emoticon_img = tk.PhotoImage(file="imgs/talk/emoticon.PNG")
        self.talk_emoticon = ttk.Label(self.talk_info_bot, image=self.talk_emoticon_img, border=0, background="white")
        self.talk_emoticon.place(x=420, y=3)
        # 사진
        self.talk_picture_img = tk.PhotoImage(file="imgs/talk/picture.PNG")
        self.talk_picture = ttk.Label(self.talk_info_bot, image=self.talk_picture_img, border=0, background="white")
        self.talk_picture.place(x=460, y=2)
        self.talk_info_scroll.pack(side="top", fill="both", expand=True)
        openFrame(self.talk_info_frame)

    def talk_en_enter(self, e):
        if self.talk_en.get() != "":
            self.my_talk_frame = tk.Frame(self.talk_info_scroll_view, border=0, background="white")
            self.my_talk_frame.pack(padx=15, pady=10, anchor="e")

            self.my_talk_label = tk.Label(self.my_talk_frame, text=self.talk_en.get(), bd=0, bg="whitesmoke")
            self.my_talk_label.config(font=("맑은 고딕", 14, "bold"), fg="black", padx=10, pady=10, wraplength=200,
                                      justify="left")
            self.my_talk_label.pack(anchor="e")

            self.talk_time = ttk.Label(self.my_talk_frame, text=datetime.datetime.now().strftime("%p %H:%M"))
            self.talk_time.config(background="white")
            self.talk_time.pack(anchor="e")

            self.chat_storage.append(self.my_talk_label.cget("text") + "/" + self.talk_time.cget("text"))
            try:
                sendMsg = ["chat_storage", self.talk_info_user.cget("text"), self.talk_info_sale_name.cget("text"),
                           self.chat_storage]
                sock.send(pickle.dumps(sendMsg))
            except Exception as ex:
                print(ex)

        self.talk_en.delete(0, "end")

    def talk_en_click(self, e):
        if self.talk_en.get() == "메시지를 입력하세요.":
            self.talk_en.delete(0, "end")

    # 채팅 안전결제
    def talk_pay_btn(self, e):
        # idx : 1 s_id ; 5 s_price ; 6 s_name ; 7 s_delivery
        s_dict = {"s_id": e.widget.master.winfo_children()[1].cget("text"),
                  "s_price": e.widget.master.winfo_children()[5].cget("text").replace(",", "").strip("원"),
                  "s_name": e.widget.master.winfo_children()[6].cget("text"),
                  "s_delivery": e.widget.master.winfo_children()[7].cget("text")}
        if s_dict["s_delivery"] in ["무료배송", "직거래"]:
            s_dict["s_delivery"] = "0"
        else:
            s_dict["s_delivery"] = s_dict["s_delivery"].replace(",", "").strip("원")
        #print(s_dict)


        #print(e.widget.master.winfo_children()[6].cget("text"))
        sendMsg = ['talk_pay', e.widget.master.winfo_children()[6].cget("text")]
        sock.send(pickle.dumps(sendMsg))
        data_len = pickle.loads(sock.recv(1024))
        if data_len[0] == "talk_pay":
            recvMsg = b''
            while data_len[1] > len(recvMsg):
                temp = sock.recv(4096)
                recvMsg += temp
            recvMsg = pickle.loads(recvMsg)
        # self.talk_sale_list = list(cur.fetchall()[0])
        self.talk_sale_list = list(recvMsg[0])
        self.pay_toplevel = tk.Toplevel()
        self.pay_toplevel.geometry("500x750+700+100")
        # 상단
        self.pay_top2 = tk.Frame(self.pay_toplevel, width=500, height=50, bg="white")
        self.pay_top2.pack()
        self.pay_back_img = tk.PhotoImage(file="imgs/back.png")
        self.back2 = tk.Label(self.pay_top2, width=25, height=29, bg="white", bd=0, image=self.pay_back_img)
        self.back2.bind("<Button-1>", lambda event: self.back_click(event, self.pay_toplevel))
        self.back2.place(x=15, y=10)
        # 하단 스크롤
        self.pay_scroll = ScrollFrame(self, self.pay_toplevel)
        self.pay_scroll_frame = tk.Frame(self.pay_scroll.viewPort, width=500, height=1080, bg="white")
        self.pay_scroll_frame.pack()
        # 결제하기 라벨
        self.pay_label_img = tk.PhotoImage(file="imgs/pay/paylabel.PNG")
        self.pay_label = tk.Label(self.pay_scroll_frame, width=90, height=40, bg="white", image=self.pay_label_img)
        self.pay_label.place(x=15, y=10)
        # 상품 이미지
        pay_image = Image.open(io.BytesIO(self.talk_sale_list[11]))
        pay_image = pay_image.resize((50, 48))
        pay_tk_img = ImageTk.PhotoImage(pay_image)
        self.product_image = tk.Label(self.pay_scroll_frame)
        self.product_image.config(image=pay_tk_img)
        self.product_image.image = pay_tk_img
        self.product_image.place(x=15, y=61)
        self.product_price = ttk.Label(self.pay_scroll_frame, text=f"{self.talk_sale_list[5]}원")
        self.product_price.configure(font=("맑은 고딕", 14, "bold"), background="white")
        self.product_price.place(x=70, y=61)
        self.product_name = ttk.Label(self.pay_scroll_frame, text=self.talk_sale_list[1])
        self.product_name.configure(font=("맑은 고딕", 10), background="white", foreground="gray")
        self.product_name.place(x=70, y=91)
        self.Transaction_method_img = tk.PhotoImage(file="imgs/pay/Transaction method.PNG")
        self.Transaction_method = ttk.Label(self.pay_scroll_frame, image=self.Transaction_method_img,
                                            background="white")
        self.Transaction_method.place(x=15, y=150)
        self.pay_line = tk.Label(self.pay_scroll_frame, width=500, height=1, bg="whitesmoke")
        self.pay_line.place(x=0, y=190)
        self.delivery_place_label_img = tk.PhotoImage(file="imgs/pay/delivery_place.PNG")
        self.delivery_place_label = ttk.Label(self.pay_scroll_frame, background="white",
                                              image=self.delivery_place_label_img)
        self.delivery_place_label.place(x=15, y=240)
        # 배송지 등록
        self.delivery_place_border_img = tk.PhotoImage(file="imgs/pay/delivery_entry.PNG")
        self.delivery_place_border = ttk.Label(self.pay_scroll_frame, image=self.delivery_place_border_img,
                                               border=0, background="white")
        self.delivery_place_border.place(x=15, y=275)
        self.delivery_place_en = tk.Entry(self.delivery_place_border, bg="white", bd=0, width=35,
                                          font=("맑은 고딕", 15), fg="gray")
        self.delivery_place_en.insert(0, "배송지를 입력해주세요")
        self.delivery_place_en.bind("<Button-1>", self.delivery_place_en_click)
        self.delivery_place_en.bind("<Leave>", self.delivery_place_en_key)
        self.delivery_place_en.place(x=25, y=19)
        # 배송 요청사항
        self.delivery_request_img = tk.PhotoImage(file="imgs/pay/delivery_entry.PNG")
        self.delivery_request_border = ttk.Label(self.pay_scroll_frame, image=self.delivery_place_border_img,
                                                 border=0,
                                                 background="white")
        self.delivery_request_border.place(x=15, y=342)
        self.delivery_request_en = tk.Entry(self.delivery_request_border, bg="white", bd=0, width=35,
                                            font=("맑은 고딕", 15), fg="gray")
        self.delivery_request_en.insert(0, "배송 요청사항")
        self.delivery_request_en.bind("<Button-1>", self.delivery_request_en_click)
        self.delivery_request_en.bind("<Leave>", self.delivery_request_en_key)
        self.delivery_request_en.place(x=25, y=19)
        # 결제금액
        self.payprice_label_img = tk.PhotoImage(file="imgs/pay/payprice_label.PNG")
        self.payprice_label = ttk.Label(self.pay_scroll_frame, image=self.payprice_label_img, border=0,
                                        background="white")
        self.payprice_label.place(x=16, y=440)
        self.payprice_img = tk.PhotoImage(file="imgs/pay/paypriceframe.PNG")
        self.payprice = ttk.Label(self.pay_scroll_frame, image=self.payprice_img, border=0, background="white")
        self.payprice.place(x=15, y=480)
        # 상품금액
        self.pay_product_price = tk.Label(self.payprice, text=f"{self.talk_sale_list[5]}원", bd=0, bg="white")
        self.pay_product_price.configure(font=("맑은 고딕", 14, "bold"), anchor="e")
        self.price_x = 385 -10 * len(self.talk_sale_list[5])
        self.price_y = 32
        self.pay_product_price.place(x=self.price_x, y=self.price_y)

        # 배송비
        self.pay_product_delivery = ttk.Label(self.payprice, text=f"+{self.talk_sale_list[6]}원", border=0,
                                              background="white")
        self.pay_product_delivery.configure(font=("맑은 고딕", 13), anchor="e")
        if len(self.talk_sale_list[6]) == 4:
            self.pay_product_delivery.place(x=340, y=70)
        else:
            self.pay_product_delivery.place(x=368, y=70)
        # 수수료

        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        # 만원 이상부터
        if len(self.talk_sale_list[5]) > 4:
            self.fee = int(round(int(self.talk_sale_list[5]) * (3.7 / 100), -2))
            self.pay_product_fee = ttk.Label(self.payprice, text=f"+{self.fee}원", border=0, background="white")
            self.pay_product_fee.configure(font=("맑은 고딕", 13), anchor="e")
            self.fee_x = 351
            self.fee_y = 109
            if len(str(self.fee)) == 3:
                self.pay_product_fee.place(x=self.fee_x, y=self.fee_y)
            elif len(str(self.fee)) == 4:
                self.pay_product_fee.place(x=self.fee_x - 10, y=self.fee_y)
            elif len(str(self.fee)) == 5:
                self.pay_product_fee.place(x=self.fee_x - 20, y=self.fee_y)
        else:
            self.fee = 0
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


        # 총 결제금액
        self.total = round(int(self.talk_sale_list[5]) + int(self.talk_sale_list[6]) + int(self.fee), -2)
        self.total_price = ttk.Label(self.payprice, text=f"{self.total}원", border=0, background="white")
        self.total_price.configure(font=("맑은 고딕", 14, "bold"), anchor="e")
        self.total_x = 385 - 10 * len(str(self.total))
        self.total_y = 177
        self.total_price.place(x=self.total_x, y=self.total_y)

        self.pay_line2 = tk.Label(self.pay_scroll_frame, width=500, height=1, bg="whitesmoke")
        self.pay_line2.place(x=0, y=740)
        # 이용약관
        self.terms_of_service_img = tk.PhotoImage(file="imgs/pay/terms of service.PNG")
        self.terms_of_service = ttk.Label(self.pay_scroll_frame, image=self.terms_of_service_img, border=0,
                                          background="white")
        self.terms_of_service.place(x=15, y=790)
        self.all_check_bool = False
        self.check_bool = False
        self.pay_allcheck_img = tk.PhotoImage(file="imgs/pay/pay_allcheck_gray.PNG")
        self.pay_allcheck_redimg = tk.PhotoImage(file="imgs/pay/pay_allcheck_red.PNG")
        self.pay_allcheck = ttk.Label(self.terms_of_service, image=self.pay_allcheck_img, border=0,
                                      background="white")
        self.pay_allcheck.bind("<Button-1>", self.terms_of_service_allclick)
        self.pay_allcheck.place(x=6, y=4)
        self.pay_check_img = tk.PhotoImage(file="imgs/pay/pay_check_gray.PNG")
        self.pay_check_redimg = tk.PhotoImage(file="imgs/pay/pay_check_red.PNG")
        i = 0
        self.check_x = 6
        self.check_y = 42
        self.terms_of_service_list = []
        while i < 4:
            self.pay_check = ttk.Label(self.terms_of_service, image=self.pay_check_img, border=0,
                                       background="white")
            self.pay_check.bind("<Button-1>", self.terms_of_service_click)
            self.pay_check.place(x=self.check_x, y=self.check_y + 31 * i)
            self.terms_of_service_list.append(self.pay_check)
            i += 1
        # 결제 버튼
        self.pay_btn_img = tk.PhotoImage(file="imgs/pay/pay_btn.PNG")
        self.pay_btn = ttk.Label(self.pay_scroll_frame, image=self.pay_btn_img, border=0, background="white")


        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        self.pay_btn.bind("<Button-1>", lambda event, dict=s_dict: self.pay_btn_click(event, dict))
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        self.pay_btn.place(x=25, y=1000)
        self.pay_scroll.pack(side="top", fill="both", expand=True)

    # 상품상세페이지의 번개톡
    def info_talk_click(self, e):
        print(111111111111111111111111111111111)
        #print(sales_dic[self.click_label])
        self.talk_info_frame = tk.Frame(self.window, width=500, height=750, bd=0, bg="white")
        self.talk_info_frame.place(x=0, y=0)
        # 상단
        self.talk_info_top = tk.Frame(self.talk_info_frame, width=500, height=125, bd=0, bg="white")
        self.talk_info_top.place(x=0, y=0)
        # 뒤로가기
        self.talk_info_back_img = tk.PhotoImage(file="imgs/back.png")
        self.talk_info_back = ttk.Label(self.talk_info_top, image=self.talk_info_back_img, border=0,
                                        background="white")
        self.talk_info_back.bind("<Button-1>", lambda event: self.lower(event, self.talk_info_frame))
        self.talk_info_back.place(x=10, y=15)
        # 대화하는 상대
        self.talk_info_user = ttk.Label(self.talk_info_top, text=sales_dic[self.click_label][0], border=0,
                                        background="white")
        self.talk_info_user.config(font=("맑은 고딕", 15, 'bold'))
        self.talk_info_user.place(x=45, y=0)
        # 상대 접속 상태
        self.talk_info_user_state = ttk.Label(self.talk_info_top, text="유저 상태", border=0, background="white")
        self.talk_info_user_state.config(font=("맑은 고딕", 10), foreground="gray")
        self.talk_info_user_state.place(x=45, y=32)
        # 점점점
        self.talk_info_dot_img = tk.PhotoImage(file="imgs/talk/dot.PNG")
        self.talk_info_dot = ttk.Label(self.talk_info_top, image=self.talk_info_dot_img, border=0,
                                       background="white")
        self.talk_info_dot.place(x=450, y=12)
        # 상품 이미지
        talk_sale_img = Image.open(io.BytesIO(sales_dic[self.click_label][11]))
        talk_sale_img = talk_sale_img.resize((35, 35))
        info_tk_img = ImageTk.PhotoImage(talk_sale_img)
        self.talk_info_sale = ttk.Label(self.talk_info_top, border=0, background="white")
        self.talk_info_sale.config(image=info_tk_img)
        self.talk_info_sale.img = info_tk_img
        self.talk_info_sale.place(x=10, y=65)
        # 상품 가격
        self.talk_info_sale_price = ttk.Label(self.talk_info_top, border=0, background="white")
        self.talk_info_sale_price.config(text=f"{sales_dic[self.click_label][5]}원", font=("맑은 고딕", 12, "bold"))
        self.talk_info_sale_price.place(x=60, y=62)
        # 상품명
        self.talk_info_sale_name = ttk.Label(self.talk_info_top, border=0, background="white")
        self.talk_info_sale_name.config(text=sales_dic[self.click_label][1], font=("맑은 고딕", 10), foreground="gray")
        self.talk_info_sale_name.place(x=60, y=85)
        # 배송비
        self.talk_info_sale_delivery = ttk.Label(self.talk_info_top, border=0, background="white",
                                                 font=("맑은 고딕", 9), foreground="gray")
        if sales_dic[self.click_label][6] != "0":
            self.talk_info_sale_delivery.config(text=f"{sales_dic[self.click_label][6]}원")
        else:
            self.talk_info_sale_delivery.config(text="무료배송")
        self.talk_info_sale_delivery.place(x=60, y=105)
        # 안전결제
        self.talk_info_pay_img = tk.PhotoImage(file="imgs/talk/pay.PNG")
        self.talk_info_pay = ttk.Label(self.talk_info_top, image=self.talk_info_pay_img, border=0,
                                       background="white")
        self.talk_info_pay.bind("<Button-1>", self.talk_pay_btn)
        self.talk_info_pay.place(x=400, y=62)
        # 중단
        self.talk_info_mid = tk.Frame(self.talk_info_frame, width=500, height=700, bd=0, bg="white")
        self.talk_info_mid.place(x=0, y=125)
        self.talk_info_scroll = ScrollFrame(self, self.talk_info_mid)
        self.talk_info_scroll_view = tk.Frame(self.talk_info_scroll.viewPort, width=500, height=700, bd=0,
                                              bg="white")
        self.talk_info_scroll_view.pack()
        # 상대 프로필
        self.talk_info_user_profile_img = tk.PhotoImage(file="imgs/talk/profile.PNG").zoom(7).subsample(4, 4)
        self.talk_info_user_profile = ttk.Label(self.talk_info_scroll_view, image=self.talk_info_user_profile_img,
                                                border=0, background="white")
        self.talk_info_user_profile.pack(pady=15)
        # 아이디
        self.talk_info_user_id = ttk.Label(self.talk_info_scroll_view, text=self.talk_info_user.cget("text"),
                                           border=0, background="white")
        self.talk_info_user_id.config(font=("맑은 고딕", 17, "bold"))
        self.talk_info_user_id.pack()
        # 날짜
        self.talk_info_day = tk.Label(self.talk_info_scroll_view, bd=0, bg="white", width=70, height=2)
        self.talk_info_day.config(
            text=f"------------------------------------   {datetime.datetime.now().strftime("%Y년 %m월 %d일")}  -----------------------------------")
        self.talk_info_day.config(font=("맑은 고딕", 10), foreground="gray")
        self.talk_info_day.pack(pady=15)
        # 하단
        self.talk_info_bot = tk.Frame(self.talk_info_frame, width=500, height=40, bd=0, bg="white")
        self.talk_info_bot.place(x=0, y=710)
        # 상품 선택
        self.talk_sale_choice_img = tk.PhotoImage(file="imgs/talk/sale_choice.PNG")
        self.talk_sale_choice = ttk.Label(self.talk_info_bot, image=self.talk_sale_choice_img, border=0,
                                          background="white")
        self.talk_sale_choice.place(x=10, y=2)
        # 텍스트 입력
        self.talk_en_label = tk.Label(self.talk_info_bot, width=50, height=2, bd=0, background="white")
        self.talk_en_label.place(x=55, y=2)
        self.talk_en = tk.Entry(self.talk_en_label, width=30, bd=0, background="white")
        self.talk_en.insert(0, "메시지를 입력하세요.")
        self.talk_en.bind("<Button-1>", self.talk_en_click)
        self.talk_en.bind("<Return>", self.talk_en_enter)
        self.talk_en.config(font=("맑은 고딕", 13), fg="gray")
        self.talk_en.place(x=6, y=2)
        # 이모티콘
        self.talk_emoticon_img = tk.PhotoImage(file="imgs/talk/emoticon.PNG")
        self.talk_emoticon = ttk.Label(self.talk_info_bot, image=self.talk_emoticon_img, border=0,
                                       background="white")
        self.talk_emoticon.place(x=420, y=3)
        # 사진
        self.talk_picture_img = tk.PhotoImage(file="imgs/talk/picture.PNG")
        self.talk_picture = ttk.Label(self.talk_info_bot, image=self.talk_picture_img, border=0, background="white")
        self.talk_picture.place(x=460, y=2)
        self.talk_info_scroll.pack(side="top", fill="both", expand=True)
        openFrame(self.talk_info_frame)

    # 메인의 최근 본 상품
    def main_recent_click(self, e):
        openFrame(self.main_recent_win)
        openFrame(self.main_recent_bot)
        for widget in self.recent_in_scroll.winfo_children():
            widget.forget()
        self.like_btn.configure(font=("맑은 고딕", 16, "bold"))
        self.recent_btn.configure(font=("맑은 고딕", 16, "bold", "underline"))
        # 제품명이 길어 뒤에 ...이 있을경우
        for i in range(len(self.recent_sale)):
            s_price = self.recent_sale[i].winfo_children()[1].cget('text').replace(",", "").strip("원")
            s_name = self.recent_sale[i].winfo_children()[3].cget('text')
            if self.recent_sale[i].winfo_children()[3].cget('text')[-3:] == "...":
                s_name = self.recent_sale[i].winfo_children()[3].cget('text')[:-3]

            try:
                sendMsg = ["main_recent_click", s_name, s_price]
                sock.send(pickle.dumps(sendMsg))
                data_len = pickle.loads(sock.recv(2048))
                data = b''
                if data_len[0] == "main_recent_click":
                    while len(data) < data_len[1]:
                        packet = sock.recv(10240)
                        if not packet:
                            break
                        data += packet

                s_list = pickle.loads(data)  # 물품 정보 리스트$$$$$$$$$$
                print("~~~~~~~~~~~~~~~~~~~~~~~~`")
                print(s_list, "s_list")
            except Exception as ex:
                print(ex)

            self.x = 15 + 250 * (i % 2)
            self.y = 20 + 330 * (i // 2)
            self.recent_in_scroll_mini = tk.Frame(self.recent_in_scroll, width=220, height=300, bd=0, bg="white")

            self.recent_sale[i].winfo_children()[2].configure(text=s_list[0][1])
            # image = Image.open(io.BytesIO(s_list[0][11]))
            # image = image.resize((220, 210))
            # tk_img = ImageTk.PhotoImage(image)

            if s_list[i][-1] == "판매완료":
                tk_img = tkinter.PhotoImage(file=complete_img_filepath)
            else:
                image = Image.open(io.BytesIO(s_list[i][11]))
                image = image.resize((200, 200))
                tk_img = ImageTk.PhotoImage(image)

            self.mini_image = tk.Label(self.recent_in_scroll_mini, width=220, height=210, bd=0, bg="white",
                                       text="상품 이미지")
            self.mini_image.config(image=tk_img)
            self.mini_image.image = tk_img
            self.mini_image.place(x=0, y=0)
            # 상품 가격
            self.mini_price = ttk.Label(self.recent_in_scroll_mini,
                                        text=s_list[0][5])
            self.mini_price.configure(font=("맑은 고딕", 14, "bold"), background="white")
            self.mini_price.place(x=0, y=240)
            # 상품명
            self.recent_name = truncate_text_recent(s_list[0][1])
            self.mini_name = ttk.Label(self.recent_in_scroll_mini, text=self.recent_name)
            self.mini_name.configure(font=("맑은 고딕", 12), background="white")
            self.mini_name.place(x=0, y=215)

            self.recent_in_scroll_mini.bind("<Button-1>",
                                            lambda event, sinfo_list=s_list: self.sale_click(event, sinfo_list))
            self.recent_in_scroll_mini.place(x=self.x, y=self.y)
            self.recent_in_scroll.configure(height=self.y + 300)
            print(self.recent_in_scroll_mini.winfo_children()[1].cget("text"))
            print(self.recent_in_scroll_mini.winfo_children()[2].cget("text"))
        self.recent_in_scroll.pack()

    # 메인의 찜
    def main_like_click(self, e):
        for widget in self.like_in_scroll.winfo_children():
            # widget.destroy()        #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
            widget.place_forget()    # destroy 하면 제품을 다시는 열 수 없음
        openFrame(self.main_recent_win)
        openFrame(self.main_like_bot)

        self.like_btn.configure(font=("맑은 고딕", 16, "bold", "underline"))
        self.recent_btn.configure(font=("맑은 고딕", 16, "bold"))
        try:
            recvMsg_like = ()
            # 로그인 계정, 상품명
            sendMsg_name = ["main_like_click"]
            sock.send(pickle.dumps(sendMsg_name))
            data_len_name = pickle.loads(sock.recv(1024))
            # print(data_len_name[1])
            if data_len_name[0] == "main_like_click":
                data_name = b''
                while len(data_name) < data_len_name[1]:
                    packet_name = sock.recv(2048)
                    if not packet_name:
                        break
                    data_name += packet_name
                recvMsg_like = pickle.loads(data_name)
        except Exception as ex:
            print("--------------------- error", "main_like_click")
            print(ex)
        try:
            for i in range(len(recvMsg_like)):
                self.x = 15 + 250 * (i % 2)
                self.y = 20 + 330 * (i // 2)
                self.like_in_scroll_mini = tk.Frame(self.like_in_scroll, width=220, height=300, bd=0, bg="white")
                # image = Image.open(io.BytesIO(recvMsg_like[i][11]))
                # image = image.resize((220, 210))
                # tk_img = ImageTk.PhotoImage(image)

                if recvMsg_like[i][-1] == "판매완료":
                    tk_img = tkinter.PhotoImage(file=complete_img_filepath)
                else:
                    image = Image.open(io.BytesIO(recvMsg_like[i][11]))
                    image = image.resize((220, 210))
                    tk_img = ImageTk.PhotoImage(image)

                self.like_mini_image = tk.Label(self.like_in_scroll_mini, width=220, height=210, bd=0, bg="white",
                                                text="상품 이미지")
                self.like_mini_image.config(image=tk_img)
                self.like_mini_image.image = tk_img
                self.like_mini_image.place(x=0, y=0)
                # 상품 가격
                self.like_mini_price = ttk.Label(self.like_in_scroll_mini, text=f"{recvMsg_like[i][5]}원")
                self.like_mini_price.configure(font=("맑은 고딕", 14, "bold"), background="white")
                self.like_mini_price.place(x=0, y=240)
                # 찜
                self.like_mini_like_img = tk.PhotoImage(file="imgs/sale_info/like2.png")
                self.like_mini_like = tk.Label(self.like_in_scroll_mini, image=self.like_mini_like_img, bd=0,
                                               bg="white")
                self.like_mini_like.image = self.like_mini_like_img
                self.like_mini_like.config(width=25, height=29)
                self.like_mini_like.bind("<Button-1>", self.main_like_delete)
                self.like_mini_like.place(x=180, y=240)
                # 상품명
                self.like_name = truncate_text_recent(recvMsg_like[i][1])
                self.like_mini_name = ttk.Label(self.like_in_scroll_mini, text=self.like_name)
                self.like_mini_name.configure(font=("맑은 고딕", 12), background="white")
                self.like_mini_name.place(x=0, y=215)
                # self.like_in_scroll_mini.bind("<Button-1>", self.sale_click)
                self.like_in_scroll_mini.bind("<Button-1>", lambda event, sinfo_list=recvMsg_like[i]: self.sale_click(event, sinfo_list))
                self.like_in_scroll_mini.place(x=self.x, y=self.y)
                self.like_in_scroll.configure(height=self.y + 300)
            self.like_in_scroll.pack()
        except Exception as ex:
            print(ex)




    # 찜 페이지에서 하트누르면 삭제
    def main_like_delete(self, e):
        try:
            if e.widget.master.winfo_children()[3].cget("text")[-3:] == "...":
                sendMsg = ["main_like_delete", e.widget.master.winfo_children()[3].cget("text")[:-3]]
            else:
                sendMsg = ["main_like_delete", e.widget.master.winfo_children()[3].cget("text")]
            sock.send(pickle.dumps(sendMsg))
        except Exception as ex:
            print(ex)
        self.main_like_click(e)
######################################
    # 상품 상세페이지 이미지 왼쪽 화살표
    def info_image_change_left(self, e):
        self.info_image_list_index -= 1
        if self.info_image_list_index < 0:
            self.info_image_list_index = len(self.info_image_list) - 1
        info_image_list_index = Image.open(io.BytesIO(self.info_image_list[self.info_image_list_index]))
        info_image_list_index = info_image_list_index.resize((370, 300))
        info_tk_img = ImageTk.PhotoImage(info_image_list_index)
        self.info_image.config(image=info_tk_img)
        self.info_image.image = info_tk_img

    # 상품 상세페이지 이미지 오른쪽 화살표
    def info_image_change_right(self, e):
        self.info_image_list_index += 1
        if self.info_image_list_index >= len(self.info_image_list):
            self.info_image_list_index = 0
        info_image_list_index = Image.open(io.BytesIO(self.info_image_list[self.info_image_list_index]))
        info_image_list_index = info_image_list_index.resize((370, 300))
        info_tk_img = ImageTk.PhotoImage(info_image_list_index)
        self.info_image.config(image=info_tk_img)
        self.info_image.image = info_tk_img

    # 상품 상세정보 카테고리 클릭
    def info_category_click(self, e):
        openFrame(self.sale_frame)

        for widget in self.sale_frame.winfo_children():
            widget.place_forget()
        try:
            sendMsg = ["click_category", e.widget.cget("text")]
            sock.send(pickle.dumps(sendMsg))

            data_len = pickle.loads(sock.recv(1024))
            if data_len[0] == "click_category":

                data = b""
                while len(data) < data_len[1]:
                    packet = sock.recv(4096)
                    if not packet:
                        break
                    data += packet

                c_click = pickle.loads(data)        # c_click : 물품 정보 리스트$$$$$$$$$$

        except Exception as ex:
            print("--------------------- error")
            print(ex)



        c_click = list(c_click)

        for i in range(len(c_click)):
            self.x = 14 + 250 * (i % 2)
            self.y = 20 + 300 * (i // 2)
            self.sale = tk.Frame(self.sale_frame, width=200, height=290, bg="white")
            # s_list[i][11] - 이미지 바이너리 데이터
            # image = Image.open(io.BytesIO(c_click[i][11]))
            # image = image.resize((200, 177))
            # tk_img = ImageTk.PhotoImage(image)

            if c_click[i][-1] == "판매완료":
                tk_img = tkinter.PhotoImage(file=complete_img_filepath)
            else:
                image = Image.open(io.BytesIO(c_click[i][11]))
                image = image.resize((200, 177))
                tk_img = ImageTk.PhotoImage(image)

            self.sale_img = tk.Label(self.sale, width=202, height=180, bd=0)
            self.sale_img.config(image=tk_img)
            self.sale_img.image = tk_img
            self.sale_price = tk.Label(self.sale, height=1, bg="white", text=f"{c_click[i][5]}원",
                                       font=("맑은 고딕", 14, "bold"), anchor="w")
            self.sale_name = ttk.Label(self.sale, width=22, text=f"{c_click[i][1]}", font=("맑은 고딕", 12))
            self.sale_name.configure(background="white")
            self.sale_name.configure(wraplength=200, anchor="w")
            self.sale_addr = tk.Label(self.sale, height=1, text=f"{c_click[i][9]}", font=("맑은 고딕", 10), fg="gray",
                                      bg="white")
            self.sale_addr.place(x=-2, y=265)
            self.sale_name.place(x=-2, y=211)
            self.sale_price.place(x=-2, y=180)
            self.sale_img.place(x=-2, y=-2)
            self.sale.place(x=self.x, y=self.y)
            # 상품 클릭시
            self.sale.bind("<Button-1>", lambda event, sinfo_list=c_click[i]: self.sale_click(event, sinfo_list))
            sales_dic[str(self.sale).split(".!")[-1]] = c_click[i]
            self.sale_frame.configure(height=self.y + 300)
        openFrame(self.search_window)
        openFrame(self.search_frame3)

    # 판매자용 상품 상세페이지 상태변경
    def seller_state_change(self, e):
        self.seller_state_change_win = tk.Toplevel()
        self.seller_state_change_win.geometry("500x300+700+550")
        self.seller_state_change_win.configure(background="white")
        # 판매중
        self.seller_state_selling = tk.Label(self.seller_state_change_win, width=10, height=3, text="판매중", bg="white")
        self.seller_state_selling.configure(font=("맑은 고딕", 14, "bold"), fg="red")
        self.seller_state_selling.pack(pady=5)
        # 예약중
        self.seller_state_reservation = tk.Label(self.seller_state_change_win, width=10, height=3, text="예약중",
                                                 bg="white")
        self.seller_state_reservation.configure(font=("맑은 고딕", 14, "bold"))
        self.seller_state_reservation.pack(pady=5)
        # 판매완료
        self.seller_state_done = tk.Label(self.seller_state_change_win, width=10, height=3, text="판매완료", bg="white")
        self.seller_state_done.configure(font=("맑은 고딕", 14, "bold"))
        self.seller_state_done.pack(pady=5)

    # 메인 화면의 카테고리
    def main_category(self, e):
        self.main_category_win = tk.Frame(self.window, width=500, height=750)
        self.main_category_win.configure(bg="white")
        self.main_category_win.place(x=0, y=0)
        openFrame(self.main_category_win)
        # self.main_category_win.geometry("500x750+700+100")

        # 상단
        self.category_top = tk.Frame(self.main_category_win, width=500, height=160, bd=0, bg="white")
        self.category_top.pack()
        self.category_del_img = tk.PhotoImage(file="imgs/del.png")
        self.category_del = ttk.Label(self.category_top, border=0, background="white", image=self.category_del_img)
        self.category_del.bind("<Button-1>", lambda event: openFrame(self.homeFrame))
        self.category_del.place(x=455, y=10)
        # 전체메뉴 라벨
        self.menu_label_img = tk.PhotoImage(file="imgs/home_category/menu.png")
        self.menu_label = ttk.Label(self.category_top, image=self.menu_label_img, border=0, background="white")
        self.menu_label.place(x=20, y=60)
        # 탭
        self.tab_label_img = tk.PhotoImage(file="imgs/home_category/tab.png")
        self.tab_label = ttk.Label(self.category_top, image=self.tab_label_img, border=0, background="white")
        self.tab_label.place(x=0, y=110)
        # 하단
        self.category_bot = tk.Frame(self.main_category_win, width=500, height=590, bg="white", bd=0)
        self.category_bot.pack()
        # 카테고리 종류
        category_name_list = ["의류", "신발", "액세서리", "전자기기", "가전제품", "여가생활", "가구", "생활용품", "식품", "유아", "공구", "반려동물",
                              "도서/티켓/문구"]
        path = "imgs/home_category/detail"
        contents = os.listdir(path)
        for i in range(len(contents)):
            self.image_path = (path + '/' + contents[i])
            self.x = 20 + 120 * (i % 4)
            self.y = 25 + 130 * (i // 4)
            self.category = tk.Label(self.category_bot, border=0, background="white", width=25, height=29)

            self.category_img_img = tk.PhotoImage(file=f"{self.image_path}")
            self.category_img = ttk.Label(self.category, border=0, background="white", image=self.category_img_img)
            self.category_img.bind("<Button-1>", self.category_click)
            self.category_img.image = self.category_img_img
            self.category_img.pack()

            self.category_name = ttk.Label(self.category, border=0, background="white", text=f"{category_name_list[i]}")
            self.category_name.configure(font=("맑은 고딕", 11, "bold"))
            self.category_name.pack()

            self.category.place(x=self.x, y=self.y)

    # 카테고리 클릭
    def category_click(self, e):
        openFrame(self.sale_frame)
        for widget in self.sale_frame.winfo_children():
            widget.place_forget()
        c_name = e.widget.master.winfo_children()[1].cget("text")
        c_click = []

        try:
            sendMsg = ["click_category", c_name]
            sock.send(pickle.dumps(sendMsg))

            data_len = pickle.loads(sock.recv(1024))
            if data_len[0] == "click_category":

                data = b""
                while len(data) < data_len[1]:
                    packet = sock.recv(4096)
                    if not packet:
                        break
                    data += packet

                c_click = pickle.loads(data)        # 물품 정보 리스트$$$$$$$$$$

        except Exception as ex:
            print("--------------------- error")
            print(ex)


        for i in range(len(c_click)):
            self.x = 14 + 250 * (i % 2)
            self.y = 20 + 300 * (i // 2)
            self.sale = tk.Frame(self.sale_frame, width=200, height=290, bg="white")
            # s_list[i][11] - 이미지 바이너리 데이터
            # image = Image.open(io.BytesIO(c_click[i][11]))
            # image = image.resize((200, 177))
            # tk_img = ImageTk.PhotoImage(image)

            if c_click[i][-1] == "판매완료":
                tk_img = tkinter.PhotoImage(file=complete_img_filepath)
            else:
                image = Image.open(io.BytesIO(c_click[i][11]))
                image = image.resize((200, 177))
                tk_img = ImageTk.PhotoImage(image)

            self.sale_img = tk.Label(self.sale, width=202, height=180, bd=0)
            self.sale_img.config(image=tk_img)
            self.sale_img.image = tk_img
            self.sale_price = tk.Label(self.sale, height=1, bg="white", text=f"{c_click[i][5]}원",
                                       font=("맑은 고딕", 14, "bold"), anchor="w")
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            self.sale_like_img = tk.PhotoImage(file="imgs/sale_info/like.PNG")
            self.sale_like = tk.Label(self.sale, image=self.sale_like_img, border=0, background="white", width=25,
                                      height=29)
            self.sale_like.bind("<Button-1>", self.like_click)
            self.sale_like.image = self.sale_like_img
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            self.sale_name = ttk.Label(self.sale, width=22, text=f"{truncate_text(c_click[i][1])}", font=("맑은 고딕", 12))
            self.sale_name.configure(background="white")
            self.sale_name.configure(wraplength=200, anchor="w")
            self.sale_addr = tk.Label(self.sale, height=1, text=f"{c_click[i][9]}", font=("맑은 고딕", 10), fg="gray",
                                      bg="white")
            self.sale_addr.place(x=-2, y=265)
            self.sale_name.place(x=-2, y=211)
            self.sale_price.place(x=-2, y=180)
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            self.sale_like.place(x=167, y=180)
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            self.sale_img.place(x=-2, y=-2)
            self.sale.place(x=self.x, y=self.y)
            # 상품 클릭시
            self.sale.bind("<Button-1>", lambda event, sinfo_list=c_click[i]: self.sale_click(event, sinfo_list))
            sales_dic[str(self.sale).split(".!")[-1]] = c_click[i]
            self.sale_frame.configure(height=self.y + 300)
        openFrame(self.search_window)
        openFrame(self.search_frame3)

    def back_func(self, e, frame):
        frame.forget()

    def back2_func(self, e, frame):
        frame.forget(frame)

    def close_win(self, e):
        self.window.destroy()

    # 프레임 오픈
    def openMainFrames(self, e, frame, button=""):
        frame.lift()
        # 최근 본 상품 갱신
        try:
            if button.master.master == self.mainFrame_bottom:  # 메인 프레임 하단 버튼일 때만
                for i in range(len(self.mainButton_list)):
                    if self.mainButton_list[i] == button:
                        filepath = f"./imgs/home_bottom/{self.mainButtonImg_list[i]}_ac.png"
                    else:
                        filepath = f"./imgs/home_bottom/{self.mainButtonImg_list[i]}_deac.png"
                    img = tkinter.PhotoImage(file=filepath)
                    self.mainButtonImg_list2[i] = img

                for j in range(len(self.mainButton_list)):
                    self.mainButton_list[j].configure(image=self.mainButtonImg_list2[j])

                    if button.master == self.mainButtonLabel_list[j].master:
                        self.mainButtonLabel_list[j].configure(fg="#000000")
                    else:
                        self.mainButtonLabel_list[j].configure(fg="#b5b5b5")
            self.myTotalSalesValue = self.loadMySale()
            self.myTotalSalesLabel_money.configure(text=f"{self.myTotalSalesValue}원")

        except Exception as ex:
            print(ex)

    def openAddProduct(self, e):
        self.AddProduct = AddProduct(self.window)
        openFrame(self.AddProduct.addProductFrame)

    def label_click(self, e):
        text = e.widget.cget("text")
        self.search_en.delete(0, "end")
        self.search_en.insert(0, text)
        self.search_en_x_btn.forget()
        self.recent_search(e)

    # 연관 검색어 보이기
    def relation_search(self, e):
        # self.x_btn_img = tk.PhotoImage(file="imgs/searchx.png")
        # self.search_en_x_btn = tk.Button(self.search_top, width=20, height=20, image=self.x_btn_img, bg="gainsboro",
        #                                  bd=0, highlightthickness=0, command=self.del_en)
        self.search_en_x_btn.place(x=390, y=28)
        if self.search_en.get() == "":
            openFrame(self.search_bot)
            self.search_en_x_btn.forget()
        else:
            try:
                category = ()
                sendMsg = ["relation_search"]
                sock.send(pickle.dumps(sendMsg))
                data_len = pickle.loads(sock.recv(1024))
                if data_len[0] == "relation_search":
                    recvMsg = b''
                    while data_len[1] > len(recvMsg):
                        temp_data = sock.recv(1024)
                        recvMsg += temp_data

                    category = pickle.loads(recvMsg)
            except Exception as ex:
                print(ex)

            category = list(category)
            for widget in self.category_frame.winfo_children():
                widget.forget()
            for i in range(len(category)):
                category[i] = list(category[i])
                if self.search_en.get() in category[i][0]:
                    """
                    for j in range(len(category[i][0])):
                        if self.search_en.get() == category[i][0][j]:
                            category[i][0] = category[i][0].replace(category[i][0][j],self.BOLD + category[i][0][j] + self.RESET)
                            print(category[i][0])
                    """
                    self.border = tk.Frame(self.category_frame, background="gainsboro")
                    self.category_label = tk.Label(self.border, text=f"{category[i][0]}", font=("맑은 고딕", 14),
                                                   bg="white", padx=3, pady=3)
                    self.category_label.pack(padx=1, pady=1)
                    self.border.pack(padx=20, pady=10, anchor="w")
                    self.category_label.bind("<Button-1>", self.label_click)

            openFrame(self.relation_frame)

    # 검색창 비우기
    def del_en(self):
        self.search_en.delete("0", "end")
        self.search_en_x_btn.forget()
        self.openFrame_search_win(self.search_window)

    # 검색창 클릭
    def search_en_click(self, event):
        if self.search_en.get() == "검색어를 입력해주세요":
            self.search_en.delete("0", "end")
        elif self.search_en.get() != "":
            openFrame(self.relation_frame)
            # self.search_en_x_btn = tk.Button(self.search_top, width=20, height=20, image=self.x_btn_img, bg="gainsboro",
            #                                  bd=0, highlightthickness=0, command=self.del_en)
            self.search_en_x_btn.place(x=390, y=28)

    # 관련 상품 창
    def recent_search(self, e):
        if self.search_en.get() != "":
            self.text = self.search_en.get()

            sendMsg = ["search_storage", self.text]
            sock.send(pickle.dumps(sendMsg))
            # self.text = truncate_text_search(self.text)

        self.search_en_x_btn.forget()
        openFrame(self.search_frame3)

        # 관련 상품창
        for widget in self.sale_frame.winfo_children():
            # widget.destroy()   # 검색해서 상품 클릭을 하고 홈버튼을 누르고 다시 검색해서 상품 클릭을 하면 에러남, 메인에 있는 상품은 들어가지지만 최근 본상품이 에러남
            widget.place_forget()  # 관련 상품창의 위젯들이 안사라짐
        # self.back_btn.destroy()
        # self.sale_back_btn_img = tk.PhotoImage(file="imgs/back.png")
        # self.sale_back_btn = ttk.Label(self.search_top, background="white",
        #                          cursor="hand2", border=0, image=self.back_img)
        # self.sale_back_btn.bind("<Button-1>",openFrame(self.search_bot))
        # self.sale_back_btn.place(x=20, y=23)
        openFrame(self.search_frame3)

        s_list = ()
        search_word = self.search_en.get()
        try:
            sendMsg = ["relative_product", search_word]
            sock.send(pickle.dumps(sendMsg))

            data_len = pickle.loads(sock.recv(1024))
            if data_len[0] == "relative_product":

                data = b""
                while len(data) < data_len[1]:
                    packet = sock.recv(4096)
                    if not packet:
                        break
                    data += packet

                s_list = tuple(pickle.loads(data))      # 물품 정보 리스트$$$$$$$$$$
        except Exception as ex:
            print("----------검색어 관련 상품")
            print(ex)

        for i in range(len(s_list)):
            # s_list[i] - 각 self.sale의 정보를 담고 있음
            self.x = 14 + 250 * (i % 2)
            self.y = 20 + 300 * (i // 2)
            self.sale = tk.Frame(self.sale_frame, width=200, height=290, bg="white")

            #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            if s_list[i][-1] == "판매완료":
                tk_img = tkinter.PhotoImage(file=complete_img_filepath)
            else:
                image = Image.open(io.BytesIO(s_list[i][11]))
                image = image.resize((200, 177))
                tk_img = ImageTk.PhotoImage(image)
            #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

            self.sale_img = tk.Label(self.sale, width=202, height=180, bd=0)
            self.sale_img.config(image=tk_img)
            self.sale_img.image = tk_img

            self.sale_price = tk.Label(self.sale, height=1, bg="white", text=f"{s_list[i][5]}원",
                                       font=("맑은 고딕", 14, "bold"), anchor="w")
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            self.sale_like_img = tk.PhotoImage(file="imgs/sale_info/like.PNG")
            self.sale_like = tk.Label(self.sale, image=self.sale_like_img, border=0, background="white", width=25,
                                      height=29)
            self.sale_like.bind("<Button-1>", self.like_click)
            self.sale_like.image = self.sale_like_img
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            self.sale_name = ttk.Label(self.sale, width=22, text=f"{truncate_text(s_list[i][1])}", font=("맑은 고딕", 12))
            self.sale_name.configure(background="white")
            self.sale_name.configure(wraplength=200, anchor="w")
            self.sale_addr = tk.Label(self.sale, height=1, text=f"{s_list[i][9]}", font=("맑은 고딕", 10), fg="gray",
                                      bg="white")
            self.sale_addr.place(x=-2, y=265)
            self.sale_name.place(x=-2, y=211)
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            self.sale_like.place(x=167, y=180)
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            self.sale_price.place(x=-2, y=180)
            self.sale_img.place(x=-2, y=-2)
            self.sale.place(x=self.x, y=self.y)
            # 상품 클릭시
            # self.sale.bind("<Button-1>", lambda event, sinfo_list=s_list[i]: self.sale_click(event, sinfo_list))
            self.sale.bind("<Button-1>", lambda event, sinfo_list=s_list[i]: self.sale_click(event, sinfo_list))
            sales_dic[str(self.sale).split(".!")[-1]] = s_list[i]
            self.sale_frame.configure(height=self.y + 300)
            self.sale_scroll.canvas.configure(height=self.y + 300)
            if self.y + 300 < 616:
                self.sale_frame.configure(height=616)
                self.sale_scroll.canvas.configure(height=616)

        self.sale_scroll.pack(side="top", fill="both", expand=True)

    # 상품 상세페이지

    def sale_click(self, e, sinfo_list):

        s_id = sinfo_list[0]
        # s_id = "id"
        # 상품명이 너무길어 생략되어 있다면 생략되기 전까지 상품명이 같은 것을 찾고 복구
        if e.widget.winfo_children()[2].cget("text")[-3:] == "...":
            for i in range(len(self.recent_sale)):
                if e.widget.winfo_children()[2].cget("text")[:-3] in self.recent_sale[i].winfo_children()[2].cget(
                        "text"):
                    e.widget.winfo_children()[2].configure(text=self.recent_sale[i].winfo_children()[2].cget("text"))
        self.recent_count = 0
        if len(self.recent_sale) == 0:
            self.recent_sale.insert(0, e.widget)
        else:
            for i in range(len(self.recent_sale)):
                if e.widget.winfo_children()[2].cget("text") == self.recent_sale[i].winfo_children()[2].cget("text"):
                    del self.recent_sale[i]
                    self.recent_sale.insert(0, e.widget)
                    self.recent_count += 1
            if self.recent_count == 0:
                self.recent_sale.insert(0, e.widget)
        self.click_label = str(e.widget).split(".!")[-1]
        if self.click_label in sales_dic.keys():
            # 상품 상세 페이지
            self.sale_info = tk.Frame(self.window, width=500, height=750, bd=0, bg="white")
            self.sale_info.place(x=0, y=0)
            # 상품 상세 페이지 상단
            self.sale_info_top = tk.Label(self.sale_info, width=500, height=3, bd=0, bg="white")
            self.sale_info_top.place(x=0, y=0)
            # 이전 버튼
            self.info_back_img = tk.PhotoImage(file="imgs/back.png")
            self.info_back = tk.Label(self.sale_info_top, width=25, height=29, image=self.info_back_img, bg="white",
                                      cursor="hand2")
            self.info_back.bind("<Button-1>", lambda event: self.lower(event, self.sale_info))
            # 홈 버튼
            self.info_home_img = tk.PhotoImage(file="imgs/home.png")
            self.info_home = tk.Label(self.sale_info_top, width=25, height=29, image=self.info_home_img, bg="white",
                                      cursor="hand2")
            self.info_home.bind("<Button-1>", lambda event: self.openFrame(self.homeFrame))
            self.info_search_img = tk.PhotoImage(file="imgs/home_top/searchButton.png").subsample(1, 1)
            self.info_search = tk.Label(self.sale_info_top, width=25, height=29, image=self.info_search_img, bg="white",
                                        cursor="hand2")
            self.info_search.bind("<Button-1>", lambda event: self.openFrame(self.search_window))
            self.info_search.place(x=450, y=8)
            self.info_home.place(x=400, y=8)
            self.info_back.place(x=18, y=8)

            # 상품 중앙 페이지
            self.sale_info_mid = tk.Frame(self.sale_info, bd=0)
            self.sale_info_mid.place(x=0, y=45)
            self.sale_info_scroll = ScrollFrame(self, self.sale_info_mid)
            self.sale_info_frame = tk.Frame(self.sale_info_scroll.viewPort, height=1500, bd=0, bg="white")
            self.sale_info_frame.pack()

            self.info_image_list = []
            self.info_image_list_index = 0
            self.j = 11
            while self.j < 15:
                if sales_dic[self.click_label][self.j] != None:
                    self.info_image_list.append(sales_dic[self.click_label][self.j])
                self.j += 1

            info_image = Image.open(io.BytesIO(sales_dic[self.click_label][11]))
            info_image = info_image.resize((370, 300))
            info_tk_img = ImageTk.PhotoImage(info_image)
            # 상품 이미지
            self.info_image = tk.Label(self.sale_info_frame, bd=0, bg="gainsboro")
            self.info_image.config(image=info_tk_img)
            self.info_image.image = info_tk_img
            self.info_image.pack()
            # self.info_image.place(x=0,y=0)



            # 상품명
            self.info_name = ttk.Label(self.sale_info_frame, border=0, text=f"{sales_dic[self.click_label][1]}",
                                       background="white")
            self.info_name.configure(font=("맑은 고딕", 14), wraplength=500, anchor="w")
            self.info_name.pack(anchor="w", padx=15, pady=10)
            # self.info_name.place(x=20,y=310)
            # 가격
            self.info_price = ttk.Label(self.sale_info_frame, border=0, text=f"{sales_dic[self.click_label][5]}원",
                                        anchor="w", background="white")
            self.info_price.configure(font=("맑은 고딕", 17, "bold"))
            self.info_price.pack(anchor="w", padx=15)
            # self.info_price.place(x=20,y=340)
            # 가격 제안
            self.info_price_offer_img = tk.PhotoImage(file="imgs/sale_info/price offer.png")
            self.info_price_offer = ttk.Label(self.sale_info_frame, border=0, image=self.info_price_offer_img,
                                              background="white")
            self.info_price_offer.pack(anchor="w", padx=12, pady=3)
            # 주소, 등록시간
            self.info_addr = ttk.Label(self.sale_info_frame, border=0, text=f"{sales_dic[self.click_label][9]}",
                                       anchor="w", background="white")
            self.info_addr.configure(font=("맑은 고딕", 11), foreground="gray")
            self.info_addr.pack(anchor="w", padx=12, pady=3)
            # self.info_addr.place(x=20,y=380)
            # 번개케어, 결제혜택
            self.info_fill_img = tk.PhotoImage(file="imgs/sale_info/care.PNG")
            self.info_fill = ttk.Label(self.sale_info_frame, border=0, image=self.info_fill_img, background="white")
            self.info_fill.pack(anchor="w", padx=15, pady=3)

            # 상세정보 라벨
            self.info_detail_label = ttk.Label(self.sale_info_frame, border=0, text="상세 정보", anchor="w",
                                               background="white")
            self.info_detail_label.configure(font=("맑은 고딕", 14, "bold"))
            self.info_detail_label.pack(anchor="w", padx=15, pady=10)

            # 카테고리 라벨
            self.info_detail_category_label = tk.Label(self.sale_info_frame, border=0, background="white", text="카테고리")
            self.info_detail_category_label.configure(font=("맑은 고딕", 13), width=20, height=1, anchor="w",
                                                      foreground="gray")
            self.info_detail_category_label.pack(anchor="w", padx=15, pady=3)
            # 카테고리 정보
            self.info_detail_category = tk.Label(self.info_detail_category_label, border=0, background="white",
                                                 text=f"{sales_dic[self.click_label][2]}")
            self.info_detail_category.configure(anchor="e", font=("맑은 고딕", 11))
            self.info_detail_category.bind("<Button-1>", self.info_category_click)
            self.info_detail_category.place(x=90, y=2)
            # 상품상태 라벨
            self.info_detail_state_label = tk.Label(self.sale_info_frame, bd=0, bg="white", text="상품상태")
            self.info_detail_state_label.configure(font=("맑은 고딕", 13), width=20, height=1, anchor="w",
                                                   foreground="gray")
            self.info_detail_state_label.pack(anchor="w", padx=15, pady=3)
            # 상품상태 정보
            self.info_detail_state = tk.Label(self.info_detail_state_label, border=0, background="white",
                                              text=f"{sales_dic[self.click_label][3]}")
            self.info_detail_state.configure(anchor="e", font=("맑은 고딕", 11))
            self.info_detail_state.place(x=90, y=2)
            # 수량 라벨
            self.info_detail_count_label = tk.Label(self.sale_info_frame, bd=0, bg="white", text="수량")
            self.info_detail_count_label.configure(font=("맑은 고딕", 13), width=20, height=1, anchor="w",
                                                   foreground="gray")
            self.info_detail_count_label.pack(anchor="w", padx=15, pady=3)
            # 수량 정보
            self.info_detail_count = tk.Label(self.info_detail_count_label, border=0, background="white",
                                              text=f"{sales_dic[self.click_label][7]}")
            self.info_detail_count.configure(anchor="e", font=("맑은 고딕", 11))
            self.info_detail_count.place(x=90, y=2)

            # self.info_detail_label.place(x=20,y=420)
            self.info_detail = ttk.Label(self.sale_info_frame, border=0, text=f"{sales_dic[self.click_label][10]}",
                                         anchor="w", background="white")
            self.info_detail.configure(font=("맑은 고딕", 14), wraplength=500)
            self.info_detail.pack(anchor="w", padx=15, pady=10)
            # self.info_detail.place(x=20,y=460)

            # 배송비 라벨
            self.info_delivery_label = ttk.Label(self.sale_info_frame, border=0, text="배송비", anchor="w",
                                                 background="white")
            self.info_delivery_label.configure(font=("맑은 고딕", 13, "bold"))
            self.info_delivery_label.pack(anchor='w', padx=15, pady=10)

            # 배송비
            self.info_delivery = ttk.Label(self.sale_info_frame, border=0, text=f"{sales_dic[self.click_label][6]}원",
                                           anchor="w", background="white")
            self.info_delivery.configure(font=("맑은 고딕", 13))
            self.info_delivery.pack(anchor='w', padx=15)

            # 스크롤에 height를 배송비 좌표를 구해 y를 한 50정도 +해서 배치하고
            # 해시태그의 시작지점을 배송비의 아래 오른쪽 적당한 곳에 설정
            # 해시태그
            self.tag_frame = ttk.Label(self.sale_info_frame, background="white", border=0, anchor="w", width=500)
            self.tag_frame.configure(font=("맑은 고딕", 12))
            for i in range(len(sales_dic[self.click_label][4].split(","))):
                self.hashtag = sales_dic[self.click_label][4].split(",")[i]
                self.tag_x = 0 + 80 * (i % 4)
                self.tag_y = 0 + 50 * (i // 4)
                self.info_tag = tk.Label(self.tag_frame, bd=1, text=f"{self.hashtag}", bg="whitesmoke")
                self.info_tag.configure(font=("맑은 고딕", 12), fg="gray", padx=2)
                self.info_tag.bind("<Button-1>", self.hashtag_click)
                self.info_tag.place(x=self.tag_x, y=self.tag_y)
            self.tag_frame.pack(anchor='w', padx=15, pady=20)
##############################################
            if len(self.info_image_list) >= 2:
                # 이미지 변경할 화살표
                # 왼쪽
                self.info_image_left_img = tk.PhotoImage(file="imgs/sale_info/image_left.png")
                self.info_image_left = ttk.Label(self.sale_info_frame, image=self.info_image_left_img, border=0,
                                                 background="white")
                self.info_image_left.bind("<Button-1>", self.info_image_change_left)
                self.info_image_left.place(x=15, y=125)
                # 오른쪽
                self.info_image_right_img = tk.PhotoImage(file="imgs/sale_info/image_right.png")
                self.info_image_right = ttk.Label(self.sale_info_frame, image=self.info_image_right_img,
                                                  border=0, background="white")
                self.info_image_right.bind("<Button-1>", self.info_image_change_right)
                self.info_image_right.place(x=450, y=125)
################################################
            if user_id != s_id:
                # 상품 하단 페이지
                self.sale_info_bot = tk.Frame(self.sale_info, width=500, height=70, bd=0, bg="white")
                self.sale_info_bot.place(x=0, y=680)
                # 번개톡
                self.info_talk_img = tk.PhotoImage(file="imgs/sale_info/talk.PNG")
                self.info_talk = tk.Label(self.sale_info_bot, width=125, height=45, image=self.info_talk_img)
                self.info_talk.place(x=110, y=8)
                # 결재
                self.info_pay_img = tk.PhotoImage(file="imgs/sale_info/pay.PNG")
                self.info_pay = tk.Label(self.sale_info_bot, width=190, height=45, image=self.info_pay_img)

            else:
                # 판매자용 상품 하단 페이지
                self.sale_info_bot2 = tk.Frame(self.sale_info, width=500, height=70, bd=0, bg="white")
                self.sale_info_bot2.place(x=0,y=680)
                # up하기
                self.info2_up_img = tk.PhotoImage(file="imgs/sale_info/seller/up.PNG")
                self.info2_up = ttk.Label(self.sale_info_bot2, border=0, background="white",image=self.info2_up_img)
                self.info2_up.place(x=10,y=14)
                # 광고하기
                self.info2_ad_img = tk.PhotoImage(file="imgs/sale_info/seller/ad.PNG")
                self.info2_ad = ttk.Label(self.sale_info_bot2, border=0, background="white", image=self.info2_ad_img)
                self.info2_ad.place(x=122, y=14)
                # 배송신청
                self.info2_delivery_img = tk.PhotoImage(file="imgs/sale_info/seller/delivery.PNG")
                self.info2_delivery = ttk.Label(self.sale_info_bot2, border=0, background="white", image=self.info2_delivery_img)
                self.info2_delivery.place(x=253, y=14)
                # 상태 변경
                self.info2_state_img = tk.PhotoImage(file="imgs/sale_info/seller/state.PNG")
                self.info2_state = ttk.Label(self.sale_info_bot2, border=0, background="white", image=self.info2_state_img)
                self.info2_state.bind("<Button-1>", self.seller_state_change)
                self.info2_state.place(x=370, y=10)

            # eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
            if sales_dic[self.click_label][-1] == "판매완료":
                self.info_pay.configure(state="disabled")
                self.info_talk.configure(state="disabled")
            else:
                self.info_pay.bind("<Button-1>", lambda event: self.pay_click(event, self.sale_info_frame))
                self.info_talk.bind("<Button-1>", self.info_talk_click)
            #eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

            self.info_pay.place(x=270, y=8)
            # 찜버튼
            self.info_like_img = tk.PhotoImage(file="imgs/sale_info/like.PNG")
            self.info_like = tk.Label(self.sale_info_bot, width=25, height=29, image=self.info_like_img, bg="white")
##################################################
            self.info_like.bind("<Button-1>", self.sale_info_like_click)
            self.info_like.place(x=26, y=16)

            # 유저의 최근 카테고리 업데이트
            self.update_userRecentCategory(self.info_detail_category.cget('text'))




        self.sale_info_scroll.pack(side="top", fill="both", expand=True)
        openFrame(self.sale_info)

    def update_userRecentCategory(self, category):
        sendMsg = ["update_userRecentCategory", category]
        sock.send(pickle.dumps(sendMsg))

    # 해시태그 클릭
    def hashtag_click(self, e):
        self.search_en.delete(0, "end")
        self.search_en.insert(0, e.widget.cget("text")[1:])
        self.recent_search(e)
        openFrame(self.search_window)

    # 결재 버튼
    def pay_click(self, e, frame):
        # idx = [1, 2, 4, 10] # 이름, 가격, 주소, 상세설명
        s_dict = {"s_name": frame.winfo_children()[1].cget('text'),
                  "s_price": frame.winfo_children()[2].cget('text').replace(",", "").strip("원"),
                  "s_address": frame.winfo_children()[4].cget('text'),
                  "s_info": frame.winfo_children()[10].cget('text')}
        print("s_dict------\t",s_dict)


        self.pay_toplevel = tk.Toplevel()
        self.pay_toplevel.geometry("500x750+700+100")
        # 상단
        self.pay_top2 = tk.Frame(self.pay_toplevel, width=500, height=50, bg="white")
        self.pay_top2.pack()
        self.pay_back_img = tk.PhotoImage(file="imgs/back.png")
        self.back2 = tk.Label(self.pay_top2, width=25, height=29, bg="white", bd=0, image=self.pay_back_img)
        self.back2.bind("<Button-1>", lambda event: self.back_click(event, self.pay_toplevel))
        self.back2.place(x=15, y=10)
        # 하단 스크롤
        self.pay_scroll = ScrollFrame(self, self.pay_toplevel)
        self.pay_scroll_frame = tk.Frame(self.pay_scroll.viewPort, width=500, height=1080, bg="white")
        self.pay_scroll_frame.pack()
        # 결제하기 라벨
        self.pay_label_img = tk.PhotoImage(file="imgs/pay/paylabel.PNG")
        self.pay_label = tk.Label(self.pay_scroll_frame, width=90, height=40, bg="white", image=self.pay_label_img)
        self.pay_label.place(x=15, y=10)
        # 상품 이미지
        pay_image = Image.open(io.BytesIO(sales_dic[self.click_label][11]))
        pay_image = pay_image.resize((50, 48))
        pay_tk_img = ImageTk.PhotoImage(pay_image)
        self.product_image = tk.Label(self.pay_scroll_frame)
        self.product_image.config(image=pay_tk_img)
        self.product_image.image = pay_tk_img
        self.product_image.place(x=15, y=61)
        self.product_price = ttk.Label(self.pay_scroll_frame, text=f"{frame.winfo_children()[2].cget('text')}")
        self.product_price.configure(font=("맑은 고딕", 14, "bold"), background="white")
        self.product_price.place(x=70, y=61)

        self.product_name = ttk.Label(self.pay_scroll_frame, text=f"{frame.winfo_children()[1].cget('text')}")
        self.product_name.configure(font=("맑은 고딕", 10), background="white", foreground="gray")
        self.product_name.place(x=70, y=91)

        self.Transaction_method_img = tk.PhotoImage(file="imgs/pay/Transaction method.PNG")
        self.Transaction_method = ttk.Label(self.pay_scroll_frame, image=self.Transaction_method_img,
                                            background="white")
        self.Transaction_method.place(x=15, y=150)

        self.pay_line = tk.Label(self.pay_scroll_frame, width=500, height=1, bg="whitesmoke")
        self.pay_line.place(x=0, y=190)

        self.delivery_place_label_img = tk.PhotoImage(file="imgs/pay/delivery_place.PNG")
        self.delivery_place_label = ttk.Label(self.pay_scroll_frame, background="white",
                                              image=self.delivery_place_label_img)
        self.delivery_place_label.place(x=15, y=240)

        # 배송지 등록
        self.delivery_place_border_img = tk.PhotoImage(file="imgs/pay/delivery_entry.PNG")
        self.delivery_place_border = ttk.Label(self.pay_scroll_frame, image=self.delivery_place_border_img, border=0,
                                               background="white")
        self.delivery_place_border.place(x=15, y=275)
        self.delivery_place_en = tk.Entry(self.delivery_place_border, bg="white", bd=0, width=35, font=("맑은 고딕", 15),
                                          fg="gray")
        self.delivery_place_en.insert(0, "배송지를 입력해주세요")
        self.delivery_place_en.bind("<Button-1>", self.delivery_place_en_click)
        self.delivery_place_en.bind("<Leave>", self.delivery_place_en_key)
        self.delivery_place_en.place(x=25, y=19)

        # 배송 요청사항
        self.delivery_request_img = tk.PhotoImage(file="imgs/pay/delivery_entry.PNG")
        self.delivery_request_border = ttk.Label(self.pay_scroll_frame, image=self.delivery_place_border_img, border=0,
                                                 background="white")
        self.delivery_request_border.place(x=15, y=342)
        self.delivery_request_en = tk.Entry(self.delivery_request_border, bg="white", bd=0, width=35,
                                            font=("맑은 고딕", 15), fg="gray")
        self.delivery_request_en.insert(0, "배송 요청사항")
        self.delivery_request_en.bind("<Button-1>", self.delivery_request_en_click)
        self.delivery_request_en.bind("<Leave>", self.delivery_request_en_key)
        self.delivery_request_en.place(x=25, y=19)

        # 결제금액
        self.payprice_label_img = tk.PhotoImage(file="imgs/pay/payprice_label.PNG")
        self.payprice_label = ttk.Label(self.pay_scroll_frame, image=self.payprice_label_img, border=0,
                                        background="white")
        self.payprice_label.place(x=16, y=440)

        self.payprice_img = tk.PhotoImage(file="imgs/pay/paypriceframe.PNG")
        self.payprice = ttk.Label(self.pay_scroll_frame, image=self.payprice_img, border=0, background="white")
        self.payprice.place(x=15, y=480)

        # 상품금액
        self.pay_product_price = tk.Label(self.payprice, text=f"{sales_dic[self.click_label][5]}원", bd=0, bg="white")
        self.pay_product_price.configure(font=("맑은 고딕", 14, "bold"), anchor="e")
        self.price_x = 385 - 10 * len(sales_dic[self.click_label][5])
        self.price_y = 32
        self.pay_product_price.place(x=self.price_x, y=self.price_y)

        # 배송비
        self.pay_product_delivery = ttk.Label(self.payprice, text=f"+{sales_dic[self.click_label][6]}원", border=0,
                                              background="white")
        self.pay_product_delivery.configure(font=("맑은 고딕", 13), anchor="e")
        if len(sales_dic[self.click_label][6]) == 4:
            self.pay_product_delivery.place(x=340, y=70)
        else:
            self.pay_product_delivery.place(x=368, y=70)
        # 수수료
        # 만원 이상부터
        if len(sales_dic[self.click_label][5]) > 4:
            self.fee = int(round(int(sales_dic[self.click_label][5]) * (3.7 / 100), -2))
            self.pay_product_fee = ttk.Label(self.payprice, text=f"+{self.fee}원", border=0, background="white")
            self.pay_product_fee.configure(font=("맑은 고딕", 13), anchor="e")
            self.fee_x = 351
            self.fee_y = 109
            if len(str(self.fee)) == 3:
                self.pay_product_fee.place(x=self.fee_x, y=self.fee_y)
            elif len(str(self.fee)) == 4:
                self.pay_product_fee.place(x=self.fee_x - 10, y=self.fee_y)
            elif len(str(self.fee)) == 5:
                self.pay_product_fee.place(x=self.fee_x - 20, y=self.fee_y)
        else:
            self.fee = 0

        # 총 결제금액
        self.total = round(int(sales_dic[self.click_label][5]) + int(sales_dic[self.click_label][6]) + int(self.fee),
                           -2)
        self.total_price = ttk.Label(self.payprice, text=f"{self.total}원", border=0, background="white")
        self.total_price.configure(font=("맑은 고딕", 14, "bold"), anchor="e")
        self.total_x = 385 - 10 * len(str(self.total))
        self.total_y = 177
        self.total_price.place(x=self.total_x, y=self.total_y)

        self.pay_line2 = tk.Label(self.pay_scroll_frame, width=500, height=1, bg="whitesmoke")
        self.pay_line2.place(x=0, y=740)

        # 이용약관
        self.terms_of_service_img = tk.PhotoImage(file="imgs/pay/terms of service.PNG")
        self.terms_of_service = ttk.Label(self.pay_scroll_frame, image=self.terms_of_service_img, border=0,
                                          background="white")
        self.terms_of_service.place(x=15, y=790)
        self.all_check_bool = False
        self.check_bool = False
        self.pay_allcheck_img = tk.PhotoImage(file="imgs/pay/pay_allcheck_gray.PNG")
        self.pay_allcheck_redimg = tk.PhotoImage(file="imgs/pay/pay_allcheck_red.PNG")
        self.pay_allcheck = ttk.Label(self.terms_of_service, image=self.pay_allcheck_img, border=0, background="white")
        self.pay_allcheck.bind("<Button-1>", self.terms_of_service_allclick)
        self.pay_allcheck.place(x=6, y=4)
        self.pay_check_img = tk.PhotoImage(file="imgs/pay/pay_check_gray.PNG")
        self.pay_check_redimg = tk.PhotoImage(file="imgs/pay/pay_check_red.PNG")
        i = 0
        self.check_x = 6
        self.check_y = 42
        self.terms_of_service_list = []
        while i < 4:
            self.pay_check = ttk.Label(self.terms_of_service, image=self.pay_check_img, border=0, background="white")
            self.pay_check.bind("<Button-1>", self.terms_of_service_click)
            self.pay_check.place(x=self.check_x, y=self.check_y + 31 * i)
            self.terms_of_service_list.append(self.pay_check)
            i += 1
        # 결제 버튼
        self.pay_btn_img = tk.PhotoImage(file="imgs/pay/pay_btn.PNG")
        self.pay_btn = ttk.Label(self.pay_scroll_frame, image=self.pay_btn_img, border=0, background="white")
        self.pay_btn.bind("<Button-1>", lambda event, dict=s_dict: self.pay_btn_click(event, dict))
        self.pay_btn.place(x=25, y=1000)

        self.pay_scroll.pack(side="top", fill="both", expand=True)

    # 결제버튼 클릭
    def pay_btn_click(self, e, s_dict):
        if self.delivery_place_en.get() == "배송지를 입력해주세요":
            win32api.MessageBox(0, "배송지를 입력해주세요.", "에러", 16)
        elif self.all_check_bool == False:
            win32api.MessageBox(0, "이용약관에 동의해주세요", "에러", 16)
        else:
            change_productSale("판매완료", s_dict)
            win32api.MessageBox(0, "결제완료 되었습니다.", "완료", 0)
            self.pay_toplevel.destroy()
            # 판매자용 상품 페이지의 상태변경에서 판매중의 색깔을 검은색, 판매완료 색깔을 빨간색
            # self.seller_state_selling.configure(fg="black")
            # self.seller_state_done.configure(fg="red")
            openFrame(self.homeFrame)

    # 이용약관 전체
    def terms_of_service_allclick(self, e):
        if self.all_check_bool:
            self.all_check_bool = False
            self.pay_allcheck.configure(image=self.pay_allcheck_img)
            for label in self.terms_of_service_list:
                label.configure(image=self.pay_check_img)
                label.image = self.pay_check_img
        else:
            self.all_check_bool = True
            self.pay_allcheck.configure(image=self.pay_allcheck_redimg)
            for label in self.terms_of_service_list:
                label.configure(image=self.pay_check_redimg)
                label.image = self.pay_check_redimg

    # 이용약관 각각
    def terms_of_service_click(self, e):
        self.terms_count = 0
        if self.check_bool:
            self.check_bool = False
            e.widget.configure(image=self.pay_check_img)
        else:
            self.check_bool = True
            e.widget.configure(image=self.pay_check_redimg)
        for i in range(len(self.terms_of_service_list) - 1):
            if self.terms_of_service_list[i].cget("image")[0][7:] != self.terms_of_service_list[i + 1].cget("image")[0][
                                                                     7:]:
                self.terms_count += 1
        if self.terms_count > 0:
            self.pay_allcheck.configure(image=self.pay_allcheck_img)
            self.all_check_bool = False

    # 배송 요청사항 엔트리
    def delivery_request_en_key(self, e):
        if self.delivery_request_en.get() == "":
            self.delivery_request_en.insert(0, "배송 요청사항")

    # 배송 요청사항 엔트리
    def delivery_request_en_click(self, e):
        if self.delivery_request_en.get() == "배송 요청사항":
            self.delivery_request_en.delete(0, "end")

    # 배송지 엔트리
    def delivery_place_en_key(self, e):
        if self.delivery_place_en.get() == "":
            self.delivery_place_en.insert(0, "배송지를 입력해주세요")

    # 배송지 엔트리
    def delivery_place_en_click(self, e):
        if self.delivery_place_en.get() == "배송지를 입력해주세요":
            self.delivery_place_en.delete(0, "end")

    # 관련 상품 찜 버튼
    def like_click(self, e):
        if self.like_bool:
            self.like2_img = tk.PhotoImage(file="imgs/sale_info/like2.PNG")
            e.widget.configure(image=self.like2_img)
            e.widget.image = self.like2_img
            try:
                # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                if e.widget.master.winfo_children()[3].cget("text")[-3:] == "...":
                    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    sendMsg = ["like_click", e.widget.master.winfo_children()[3].cget("text")[:-3], self.like_bool]
                else:
                    sendMsg = ["like_click", e.widget.master.winfo_children()[3].cget("text"), self.like_bool]
                sock.send(pickle.dumps(sendMsg))
            except Exception as ex:
                print(ex)
            self.like_bool = False
        else:
            self.like2_img = tk.PhotoImage(file="imgs/sale_info/like.PNG")
            e.widget.configure(image=self.like2_img)
            e.widget.image = self.like2_img
            try:
                # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                if e.widget.master.winfo_children()[3].cget("text")[-3:] == "...":
                    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    sendMsg = ["like_click", e.widget.master.winfo_children()[3].cget("text")[:-3], self.like_bool]
                else:
                    sendMsg = ["like_click", e.widget.master.winfo_children()[3].cget("text"), self.like_bool]
                sock.send(pickle.dumps(sendMsg))
            except Exception as ex:
                print(ex)
            self.like_bool = True
#########################################
    # 상세페이지 찜 버튼
    def sale_info_like_click(self, e):
        print("sale_info_like_click")
        self.sale_info_name = e.widget.master.master.winfo_children()[1].winfo_children()[0].winfo_children()[0].winfo_children()[0].winfo_children()[1].cget("text")
        if self.like_bool:
            self.like2_img = tk.PhotoImage(file="imgs/sale_info/like2.PNG")
            e.widget.configure(image=self.like2_img)
            e.widget.image = self.like2_img
            try:
                # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                if self.sale_info_name[-3:] == "...":
                    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    sendMsg = ["like_click", self.sale_info_name[:-3], self.like_bool]
                else:
                    sendMsg = ["like_click", self.sale_info_name, self.like_bool]
                sock.send(pickle.dumps(sendMsg))
            except Exception as ex:
                print(ex)
            self.like_bool = False
        else:
            self.like2_img = tk.PhotoImage(file="imgs/sale_info/like.PNG")
            e.widget.configure(image=self.like2_img)
            e.widget.image = self.like2_img
            try:
                # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                if self.sale_info_name[-3:] == "...":
                    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                    sendMsg = ["like_click", self.sale_info_name[:-3], self.like_bool]
                else:
                    sendMsg = ["like_click", self.sale_info_name, self.like_bool]
                sock.send(pickle.dumps(sendMsg))
            except Exception as ex:
                print(ex)
            self.like_bool = True
#############################################
    # 최근 검색어 삭제
    def del_recent(self, event, button):
        # master : 부모 위젯 추출
        key = button.master.cget("text")  # 클릭한 버튼의 부모 위젯(Label)의 텍스트 추출 -> recentSearchLables 딕셔너리의 key
        try:
            sendMsg = ["recent_search_del", key]
            sock.send(pickle.dumps(sendMsg))
        except Exception as ex:
            print(ex)
        button.master.destroy()  # 라벨 파괴
        del self.recent_label_dic[key]
        if len(self.recent_frame_mini.winfo_children()) == 0:
            self.all_del_btn.destroy()

    # 최근 검색어 전체 삭제
    def all_del(self):
        for widget in self.recent_frame_mini.winfo_children():
            widget.destroy()
        try:
            sendMsg = ["recent_search_all_del"]
            sock.send(pickle.dumps(sendMsg))
        except Exception as ex:
            print(ex)
        self.recent_label_dic.clear()
        self.all_del_btn.destroy()

    # 요즘 많이 찾는 검색어
    def search_count(self):
        try:
            sendMsg = ["search_count"]
            sock.send(pickle.dumps(sendMsg))

            data_len = pickle.loads(sock.recv(1024))
            if data_len[0] == "search_count":

                recvMsg = b''
                while data_len[1] > len(recvMsg):
                    temp = sock.recv(4096)
                    recvMsg += temp
                recvMsg = pickle.loads(recvMsg)

        except Exception as ex:
            print("--------------------- 요즘 많이 찾는 검색어")
            print(ex)
        self.count_dic.clear()
        for i in range(len(recvMsg)):
            if i in self.count_dic:
                self.count_dic[recvMsg[i][0]] += 1
            else:
                self.count_dic[recvMsg[i][0]] = 1
        return self.count_dic

    # 검색어 상위 4개
    def search_top_count(self):
        self.search_count()
        return sorted(self.count_dic.items(), reverse=True, key=lambda x: x[1])[:4]

    # frame 닫기
    def back_click(self, e, frame):
        frame.destroy()
        self.make_check = True

    def load_sList(self, dict):
        sendMsg = ["load", dict]
        sock.send(pickle.dumps(sendMsg))
        recvMsg = pickle.loads(sock.recv(2048))
        return recvMsg



class AddProduct(tkinter.Frame):
    def __init__(self, window):
        tkinter.Frame.__init__(self, window)
        self.window = window
        # self.window.geometry("500x750+1200+100")  # pc
        self.window.geometry("500x750+700+10")  # desktop

        # 상품 등록 프레임
        self.addProductFrame = tkinter.Frame(self.window, width=500, height=750, bg='white')
        self.addProductFrame.place(x=0, y=0)

        # 상품 등록 상단
        self.addProductFrame_top = tkinter.Frame(self.addProductFrame, width=500, height=50, bg='white')
        self.addProductFrame_top.place(x=0, y=0)

        self.addProductButton_back = tkinter.Button(self.addProductFrame_top, bg='white', border=0,
                                                    text="〈", font=("맑은 고딕", 17, 'bold'))
        self.addProductButton_back.place(x=10, y=0)
        self.addProductButton_back.bind("<Button-1>", lambda event, frame=self.addProductFrame: self.back(event, frame))

        self.addProductButtonImg = tkinter.PhotoImage(file="./imgs/addproduct/registration2.png")
        self.addProductButton_reg = tkinter.Label(self.addProductFrame_top, text="등록", image=self.addProductButtonImg,
                                                  border=0, bg='white', fg="white")
        self.addProductButton_reg.place(x=425, y=10)

        self.addProductButton_reg.bind("<Button-1>", self.clickRegistButton)

        # 상품 등록 중앙
        # 스크롤 프레임
        # self.addProductFrame_mid = tkinter.Frame(self.addProductFrame, width=500, height=700, bg='white')
        self.addProductFrame_mid = tkinter.Frame(self.addProductFrame, bg='white')
        self.addProductFrame_mid.place(x=0, y=50)

        self.addProductScrollFrame = ScrollFrame(self, self.addProductFrame_mid)  # add a new scrollable frame.
        self.addProductScrollFrame.configure(bg='white', width=50, height=10)
        self.addProductScrollFrame.canvas.configure(height=700)

        self.addProductInnerFrame = tkinter.Frame(self.addProductScrollFrame.viewPort, bg='white', width=500,
                                                  height=800)
        self.addProductInnerFrame.pack()

        # 사진 등록
        self.selectPictureLabel = tkinter.Frame(self.addProductInnerFrame, width=66, height=5, bg='white')
        self.selectPictureLabel.place(x=0, y=10)

        self.selectPictureBtn_img = tkinter.PhotoImage(file='./imgs/addproduct/selectImg.png')
        self.selectPictureButton = tkinter.Label(self.selectPictureLabel, bg='gray', border=0,
                                                 image=self.selectPictureBtn_img)
        self.selectPictureButton.pack(side='left', padx=16)
        # self.selectPictureButton.place(x=0, y=0)
        self.selectPictureButton.bind("<Button-1>", self.selectPicture)

        self.selectedPictureCount = 0
        self.selectedPictureLabel = tkinter.Label(self.addProductInnerFrame, bg="#f6f6f6",
                                                  text=f"{self.selectedPictureCount}/4",
                                                  font=("맑은 고딕", 11, "bold"), fg="#999999")
        self.selectedPictureLabel.place(x=34, y=48)
        self.selectedPictureLabel.bind("<Button-1>", self.selectPicture)

        self.selectedPicture1 = tkinter.Label(self.selectPictureLabel, border=0)
        self.selectedPicture2 = tkinter.Label(self.selectPictureLabel, border=0)
        self.selectedPicture3 = tkinter.Label(self.selectPictureLabel, border=0)
        self.selectedPicture4 = tkinter.Label(self.selectPictureLabel, border=0)

        self.deselectImg = tkinter.PhotoImage(file="./imgs/addproduct/deselectImg.png")
        self.deselectImgButton1 = tkinter.Label(self.selectedPicture1, image=self.deselectImg, border=0)
        self.deselectImgButton2 = tkinter.Label(self.selectedPicture2, image=self.deselectImg, border=0)
        self.deselectImgButton3 = tkinter.Label(self.selectedPicture3, image=self.deselectImg, border=0)
        self.deselectImgButton4 = tkinter.Label(self.selectedPicture4, image=self.deselectImg, border=0)

        self.selectedPicturesLabels = {1: self.selectedPicture1,
                                       2: self.selectedPicture2,
                                       3: self.selectedPicture3,
                                       4: self.selectedPicture4}

        self.deselectImgBtns = {1: self.deselectImgButton1,
                                2: self.deselectImgButton2,
                                3: self.deselectImgButton3,
                                4: self.deselectImgButton4}

        self.recentDelNum = 0
        self.posibleNums = [1, 2, 3, 4]
        self.selectedNums = {}

        for i in range(len(self.deselectImgBtns)):
            self.deselectImgBtns[i + 1].place(x=40, y=0)
            self.deselectImgBtns[i + 1].bind("<Button-1>", lambda event, labelNum=int(
                str(self.selectedPicturesLabels[i + 1])[-1]): self.deselectImg_func(event, labelNum))

        # 상품명
        self.addProductNameLabel = tkinter.Label(self.addProductInnerFrame, bg='white', width=65, height=3, border=0)
        self.addProductNameLabel.place(x=18, y=100)

        self.addProductEntry_name = tkinter.Entry(self.addProductNameLabel, bg='white', width=50, border=0,
                                                  font=("맑은 고딕", 15, "bold"), fg="#9c9c9c", justify='left')
        self.addProductEntry_name.bind("<FocusIn>", self.focusIn_apen)
        self.addProductEntry_name.bind("<FocusOut>", self.focusOut_apen)
        self.addProductEntry_name.insert(0, "상품명(두 글자 이상 적어주세요.)")
        self.addProductEntry_name.place(x=0, y=3)

        self.addProduct_underline = tkinter.Label(self.addProductNameLabel, bg='#e5e5e5', width=100, height=1, border=0)
        self.addProduct_underline.place(x=0, y=45)

        # 카테고리
        # self.category = ["패션", '전자기기', '가전제품', '여가생활', '가구', '생활용품', '식품', '반려동물용품', '유아', '공구', '도서/티켓/문구']
        self.addProductCategoryLabel = tkinter.Label(self.addProductInnerFrame, bg='white', width=65, height=3,
                                                     border=0)
        self.addProductCategoryLabel.place(x=18, y=160)

        self.addProductLabel_category = tkinter.Label(self.addProductCategoryLabel, bg='white', width=31,
                                                      font=("맑은 고딕", 15, "bold"), fg='#9c9c9c', text="카테고리", anchor='w')
        self.addProductLabel_category.place(x=0, y=0)

        self.addProduct_underline = tkinter.Label(self.addProductCategoryLabel, bg='#e5e5e5', width=100, height=1,
                                                  border=0)
        self.addProduct_underline.place(x=0, y=45)

        # 상품 상태
        self.addProductConditionLabel = tkinter.Label(self.addProductInnerFrame, bg='white', width=65, height=3,
                                                      border=0)
        self.addProductConditionLabel.place(x=18, y=220)

        self.addProductLabel_condition = tkinter.Label(self.addProductConditionLabel, bg='white', width=31,
                                                       font=("맑은 고딕", 15, "bold"), fg='#9c9c9c', text="상품상태",
                                                       anchor='w')
        self.addProductLabel_condition.place(x=0, y=0)

        self.addProduct_underline = tkinter.Label(self.addProductConditionLabel, bg='#e5e5e5', width=100, height=1,
                                                  border=0)
        self.addProduct_underline.place(x=0, y=45)

        # # 태그
        self.addProductTagLabel = tkinter.Label(self.addProductInnerFrame, bg='white', width=65, height=3, border=0)
        self.addProductTagLabel.place(x=18, y=280)

        self.addProductEntry_tag = tkinter.Entry(self.addProductTagLabel, bg='white', width=38, border=0,
                                                 font=("맑은 고딕", 15, "bold"), fg='#9c9c9c')
        self.addProductEntry_tag.insert(0, "# 태그")
        self.addProductEntry_tag.place(x=0, y=0)
        self.addProductEntry_tag.bind("<FocusIn>", self.focusIn_apet)
        self.addProductEntry_tag.bind("<FocusOut>", self.focusOut_apet)
        self.addProductEntry_tag.bind("<KeyRelease>", self.keyReleaseTag)

        self.addProduct_underline = tkinter.Label(self.addProductTagLabel, bg='#e5e5e5', width=100, height=1,
                                                  border=0)
        self.addProduct_underline.place(x=0, y=45)
        self.tagList = []

        # ￦ 가격
        self.addProductPriceLabel = tkinter.Label(self.addProductInnerFrame, bg='white', width=65, height=3, border=0)
        self.addProductPriceLabel.place(x=18, y=340)

        self.addProductLabel_won = tkinter.Label(self.addProductPriceLabel, bg='white', width=2, anchor='w',
                                                 font=("맑은 고딕", 15, ""), text="￦", fg='#9c9c9c')
        self.addProductLabel_won.place(x=0, y=0)
        self.addProductEntry_price = tkinter.Entry(self.addProductPriceLabel, bg='white', width=36, border=0,
                                                   font=("맑은 고딕", 15, "bold"), fg="#9c9c9c", justify='left')
        self.addProductEntry_price.insert(0, "가격")
        self.addProductEntry_price.place(x=27, y=3)

        self.addProductEntry_price.bind("<FocusIn>", self.focusIn_apep)
        self.addProductEntry_price.bind("<FocusOut>", self.focusOut_apep)

        self.addProduct_underline = tkinter.Label(self.addProductPriceLabel, bg='#e5e5e5', width=100, height=1,
                                                  border=0)
        self.addProduct_underline.place(x=0, y=45)

        # 가격제안 버튼(기능 x, 클릭은 가능)
        self.addProductDiscountLabel = tkinter.Label(self.addProductInnerFrame, bg='white', width=65, height=2,
                                                     border=0)
        self.addProductDiscountLabel.place(x=18, y=400)

        self.checkImg_ac = tkinter.PhotoImage(file="./imgs/addproduct/check_ac.png")
        self.checkImg_deac = tkinter.PhotoImage(file="./imgs/addproduct/check_deac.png")
        self.checked_DiscountLable = False
        self.addProductDiscountLabel_check = tkinter.Label(self.addProductDiscountLabel, bg='white')
        self.addProductDiscountLabel_check.configure(image=self.checkImg_deac)
        self.addProductDiscountLabel_check.pack(side='left')
        self.addProductDiscountLabel_check.bind("<Button-1>", self.clickCheckBox_apdl)

        self.addProductDiscountLabel_text = tkinter.Label(self.addProductDiscountLabel, bg='white', border=0,
                                                          text="가격제안 받기", font=("맑은 고딕", 12, "bold"))
        self.addProductDiscountLabel_text.pack(side='left', padx=5)
        self.addProductDiscountLabel_text.bind("<Button-1>", self.clickCheckBox_apdl)

        self.addProductDiscountLabel_detail = tkinter.Label(self.addProductDiscountLabel, bg='white', border=0,
                                                            text="가격을 제안받고 더 빠르게 판매해요", fg='#8b8b8b',
                                                            font=("맑은 고딕", 11, "bold"))
        self.addProductDiscountLabel_detail.pack(side='left')

        # 배송비 radio 버튼
        self.addProductDelFeeLabel = tkinter.Label(self.addProductInnerFrame, bg="white", width=65, height=2, border=0,
                                                   anchor='w')
        self.addProductDelFeeLabel.place(x=18, y=437)

        self.delivery_fee = tkinter.IntVar()

        self.radio_active = tkinter.PhotoImage(file="./imgs/addproduct/radio_ac.PNG")
        self.radio_deactive = tkinter.PhotoImage(file="./imgs/addproduct/radio_deac.PNG")

        self.addProductDelFeeRadio_contain = tkinter.Radiobutton(self.addProductDelFeeLabel, variable=self.delivery_fee,
                                                                 value=0)
        self.addProductDelFeeRadio_contain.configure(image=self.radio_deactive, selectimage=self.radio_active,
                                                     indicatoron=False,
                                                     border=0, bg='white', highlightthickness=0)
        self.addProductDelFeeLabel_contain = tkinter.Label(self.addProductDelFeeLabel, bg='white',
                                                           text="배송비포함", font=("맑은 고딕", 12, "bold"))
        self.addProductDelFeeRadio_contain.place(x=0, y=3)
        self.addProductDelFeeLabel_contain.place(x=25, y=2)
        self.addProductDelFeeLabel_contain.bind("<Button-1>", self.clickRadioDelFeeContain)
        self.addProductDelFeeRadio_contain.bind("<Button-1>", self.clickRadioDelFeeContain)

        self.addProductDelFeeRadio_separate = tkinter.Radiobutton(self.addProductDelFeeLabel,
                                                                  variable=self.delivery_fee, value=1)
        self.addProductDelFeeRadio_separate.configure(image=self.radio_deactive, selectimage=self.radio_active,
                                                      indicatoron=False,
                                                      border=0, bg='white', highlightthickness=0)
        self.addProductDelFeeLabel_separate = tkinter.Label(self.addProductDelFeeLabel, bg='white',
                                                            text="배송비별도", font=("맑은 고딕", 12, "bold"))

        self.addProductDelFeeLabel_input = tkinter.Label(self.addProductDelFeeLabel, bg='white', border=0,
                                                         text="입력", font=("맑은 고딕", 11, "bold", "underline"),
                                                         fg="#666666")
        self.addProductDelFeeRadio_separate.place(x=130, y=3)
        self.addProductDelFeeLabel_separate.place(x=155, y=2)
        self.addProductDelFeeLabel_input.place(x=245, y=4)
        self.addProductDelFeeLabel_separate.bind("<Button-1>", self.clickRadioDelFeeSeparate)
        self.addProductDelFeeLabel_input.bind("<Button-1>", self.clickRadioDelFeeSeparate)
        self.addProductDelFeeRadio_separate.bind("<Button-1>", self.clickRadioDelFeeSeparate)

        self.addProductDelFeeLabel_img = tkinter.PhotoImage(file="./imgs/addproduct/deliveryFee.png")
        self.addProductDelFeeLabel_inputLabel = tkinter.Label(self.addProductDelFeeLabel, bg="white", borderwidth=1,
                                                              image=self.addProductDelFeeLabel_img)
        self.addProductDelFeeLabel_inputWon = tkinter.Label(self.addProductDelFeeLabel_inputLabel, height=1, bg="white",
                                                            text="원", fg="gray", anchor='e', border=0,
                                                            font=("맑은 고딕", 11))
        self.addProductDelFeeLabel_inputEntry = tkinter.Entry(self.addProductDelFeeLabel_inputLabel, bg='white',
                                                              border=0, width=13,
                                                              font=("맑은 고딕", 11, "bold"))
        self.addProductDelFeeLabel_inputEntry.insert(0, 0)
        self.addProductDelFeeLabel_inputEntry.configure(state="disabled", disabledbackground="white")
        self.addProductDelFeeLabel_inputEntry.place(x=10, y=4)
        self.addProductDelFeeLabel_inputWon.place(x=130, y=4)
        self.addProductDelFeeLabel_inputLabel.place(x=300, y=0)

        # 옵션 선택
        self.addProductSelOpLabel = tkinter.Label(self.addProductInnerFrame, bg="white", border=0, width=65, height=3)
        self.addProductSelOpLabel.place(x=18, y=480)

        self.selectOptionImg = tkinter.PhotoImage(file='./imgs/addproduct/selectOption.png')
        self.addProductSelOpButton = tkinter.Label(self.addProductSelOpLabel, bg='white', image=self.selectOptionImg,
                                                   text="옵션선택", font=("맑은 고딕", 12, "bold"))
        self.addProductSelOpButton.place(x=0, y=-1)

        self.temp_defaltAmount = 1
        self.temp_defaltExchange = "불가"
        self.temp_defaltAddress = "서구 둔산2동"  # 임시 기본 주소 -> db에서 받아오는 걸로 수정해야함 ---------------------------------------

        self.option_text = f"{self.temp_defaltAmount}개 • 교환{self.temp_defaltExchange} • {self.temp_defaltAddress}"
        self.addProductSelOpText = tkinter.Label(self.addProductSelOpLabel, bg='white', border=0, pady=6,
                                                 text=self.option_text, font=("맑은 고딕", 11, "bold"), fg="#979797")
        self.option_list = [f"{self.temp_defaltAmount}", f"{self.temp_defaltExchange}", f"{self.temp_defaltAddress}"]
        self.addProductSelOpText.place(x=100, y=8)

        # 상세정보
        self.addProduct_underline = tkinter.Label(self.addProductInnerFrame, bg='#e5e5e5', width=65, height=0,
                                                  border=0)
        self.addProduct_underline.place(x=18, y=761)

        self.addProductDetailText = tkinter.Text(self.addProductInnerFrame, bg='white', width=51, border=0, height=10,
                                                 font=("맑은 고딕", 13, ""), fg="#b4b4b4")
        self.detail_defaltText = ("브랜드, 모델명, 구매 시기, 하자 유무 등 상품 설명을 최대한 자세히 적어주세요.\n" +
                                  "전화번호, SNS 계정 등 개인정보 입력은 제한될 수 있어요.\n"
                                  + "\n안전하고 건전한 거래 환경을 위해 과학기술정보통신부, 한국인터넷진흥원과 번개장터(주)가 함께합니다.")
        self.addProductDetailText.insert('end', self.detail_defaltText)
        self.addProductDetailText.place(x=18, y=544)

        self.addProductDetailText.bind("<FocusIn>", self.focusIn_apdt)
        self.addProductDetailText.bind("<FocusOut>", self.focusOut_apdt)

        self.addProductScrollFrame.pack(side="top", fill="both", expand=True)

        # 기능 bind
        self.addProductLabel_category.bind("<Button-1>", self.openSelectCategoryFrame)
        self.addProductLabel_condition.bind("<Button-1>", self.openSelectConditionFrame)
        self.addProductSelOpButton.bind("<Button-1>", self.openSelectOptionFrame)

    # 기능
    def back(self, e, frame):  # 프레임 닫기
        frame.destroy()

    def openSelectCategoryFrame(self, e):
        self.selectCategory = SelectCategory(self.window, self.back, self.addProductLabel_category)
        openFrame(self.selectCategory.setCategoryFrame)

    def openSelectConditionFrame(self, e):
        self.selectCondition = SelectCondition(self.window, self.back, self.addProductLabel_condition)
        openFrame(self.selectCondition.setConditionFrame)

    def openSelectTagFrame(self, e):
        pass

    def openSelectOptionFrame(self, e):
        self.selectOption = SelectOption(self.window, self.back, self.option_list, self.addProductSelOpText)
        openFrame(self.selectOption.selectOptionFrame)

    # 사진 불러오기 / 삭제하기
    def selectPicture(self, e):
        filepath = ""
        if self.selectedPictureCount < 4:
            filepath = filedialog.askopenfilename(
                filetypes=(("image file", "*.png"), ("image file", "*.jpg"), ("image file", "*.jpeg")))
        try:
            if filepath:
                # 이미지 변환 사이즈 : 65 * 65
                with open(filepath, 'rb') as f:
                    data = f.read()
                encoded_img = np.frombuffer(data, dtype=np.uint8)
                src = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)

                if filepath.split(".")[-1] in ["jpg", "jpeg"]:
                    cvt_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
                elif filepath.split(".")[-1] == "png":
                    cvt_src = cv2.cvtColor(src, cv2.COLOR_BGRA2RGB)

                dst = cv2.resize(cvt_src, dsize=(65, 65), interpolation=cv2.INTER_LINEAR)
                image = Image.fromarray(dst)

                self.selectedPictureCount += 1
                self.selectedPictureLabel.configure(text=f"{self.selectedPictureCount}/4")

                new_img = ImageTk.PhotoImage(image)
                self.selectedPicturesLabels[self.posibleNums[0]].configure(image=new_img)
                self.selectedPicturesLabels[self.posibleNums[0]].image = new_img
                self.selectedPicturesLabels[self.posibleNums[0]].pack(side='left', padx=16)

                self.selectedNums[self.posibleNums[0]] = data
                self.posibleNums.remove(self.posibleNums[0])
                #print(self.selectedNums.keys())

        except Exception as ex:
            print(ex)

    def deselectImg_func(self, event, labelNum):
        try:
            self.selectedPicturesLabels[labelNum - 1].forget()

            self.recentDelNum = labelNum - 1
            self.posibleNums.append(self.recentDelNum)
            del self.selectedNums[self.recentDelNum]
            print(self.selectedNums.keys())

            self.selectedPictureCount -= 1
            self.selectedPictureLabel.configure(text=f"{self.selectedPictureCount}/4")

        except Exception as ex:
            print(ex)

    # 상품명
    def focusIn_apen(self, e):
        if self.addProductEntry_name.get() == "상품명(두 글자 이상 적어주세요.)":
            self.addProductEntry_name.delete(0, len(self.addProductEntry_name.get()))
            self.addProductEntry_name.configure(fg="black")

    def focusOut_apen(self, e):
        if not self.addProductEntry_name.get():
            self.addProductEntry_name.insert(0, f"상품명(두 글자 이상 적어주세요.)")
            self.addProductEntry_name.configure(fg="#9c9c9c")

    # 태그
    def focusIn_apet(self, e):
        if self.addProductEntry_tag.get() == "# 태그":
            self.addProductEntry_tag.delete(1, len(self.addProductEntry_tag.get()))
            self.addProductEntry_tag.configure(fg='black')

    def focusOut_apet(self, e):
        if self.addProductEntry_tag.get() == "# 태그" or self.addProductEntry_tag.get().lstrip("# ") == "":
            self.addProductEntry_tag.delete(0, 'end')
            self.addProductEntry_tag.insert('end', "# 태그")
            self.addProductEntry_tag.configure(fg='#9c9c9c')

        else:
            print(self.addProductEntry_tag.get().split("# "))

    def keyReleaseTag(self, e):
        cursor_index = self.addProductEntry_tag.index(tkinter.INSERT)
        if e.keysym == 'space':
            self.addProductEntry_tag.insert(cursor_index, '#')

    # 가격
    def focusIn_apep(self, e):
        if self.addProductEntry_price.get() == "가격":
            self.addProductEntry_price.delete(0, len(self.addProductEntry_price.get()))
            self.addProductEntry_price.configure(fg='black')
            self.addProductLabel_won.configure(fg='black')

    def focusOut_apep(self, e):
        if not self.addProductEntry_price.get():
            self.addProductEntry_price.insert(0, f"가격")
            self.addProductEntry_price.configure(fg='#9c9c9c')
            self.addProductLabel_won.configure(fg='#9c9c9c')

    # 가격제안 클릭
    def clickCheckBox_apdl(self, e):
        if self.checked_DiscountLable:  # 클릭 시점 체크 상태일 경우 -> 비활성화
            self.checked_DiscountLable = False
            self.addProductDiscountLabel_check.configure(image=self.checkImg_deac)
        else:  # -> 활성화
            self.checked_DiscountLable = True
            self.addProductDiscountLabel_check.configure(image=self.checkImg_ac)

    # 배송비 라디오 버튼 레이블 클릭
    def clickRadioDelFeeContain(self, e):
        self.addProductDelFeeRadio_contain.select()
        self.addProductDelFeeRadio_separate.deselect()
        self.addProductDelFeeLabel_inputEntry.delete(0, 'end')
        self.addProductDelFeeLabel_inputEntry.insert(0, 0)
        self.addProductDelFeeLabel_inputEntry.config(state="disabled")

    def clickRadioDelFeeSeparate(self, e):
        self.addProductDelFeeRadio_separate.select()
        self.addProductDelFeeRadio_contain.deselect()
        self.addProductDelFeeLabel_inputEntry.config(state="normal")
        self.addProductDelFeeLabel_inputEntry.delete(0, 'end')

    # 상세 설명
    def focusIn_apdt(self, e):
        if self.addProductDetailText.get(1.0, "end-1c") == self.detail_defaltText:
            self.addProductDetailText.delete(1.0, "end-1c")
            self.addProductDetailText.configure(fg='black')

    def focusOut_apdt(self, e):
        if not self.addProductDetailText.get(1.0, "end-1c"):
            self.addProductDetailText.insert(1.0, self.detail_defaltText)
            self.addProductDetailText.configure(fg='#9c9c9c')

    def clickRegistButton(self, e):
        try:
            productName = self.addProductEntry_name.get()
            productCategory = self.addProductLabel_category.cget("text")
            productCondition = self.addProductLabel_condition.cget("text")
            tag_list = self.addProductEntry_tag.get().split()
            productPrice = self.addProductEntry_price.get()
            deliveryFee = self.addProductDelFeeLabel_inputEntry.get()
            option_list = self.addProductSelOpText.cget("text").split(" • ")
            productDetail = self.addProductDetailText.get(1.0, "end")
            selectedImgsBinary = []
            for key, value in self.selectedNums.items():
                selectedImgsBinary.append(value)

            for i in range(4 - len(selectedImgsBinary)):
                selectedImgsBinary.append(None)

            if not selectedImgsBinary:
                tkinter.messagebox.showerror("경고", "상품 사진을 선택해주세요")

            # elif not self.addProductEntry_name.get().strip() or self.addProductEntry_name.get() == "상품명":
            elif not productName.strip() or productName == "상품명(두 글자 이상 적어주세요)":
                tkinter.messagebox.showerror("경고", "상품명을 입력해주세요")

            elif len(productName) < 2:
                tkinter.messagebox.showerror("경고", "상품명은 두 글자 이상 적어주세요")

            # elif self.addProductLabel_category.cget("text") == "카테고리":
            elif productCategory == "카테고리":
                tkinter.messagebox.showerror("경고", "카테고리를 선택해주세요")

            # elif self.addProductLabel_condition.cget("text") == "상품상태":
            elif productCondition == "상품상태":
                tkinter.messagebox.showerror("경고", "상품상태를 선택해주세요")

            elif self.addProductEntry_tag.get() in ["# 태그", ""]:
                tkinter.messagebox.showerror("경고", "태그를 선택해주세요")
            elif "#" in tag_list:
                tkinter.messagebox.showerror("경고", "유효하지 않은 태그가 포함되어있습니다")

            elif productPrice in ["가격", ""]:
                tkinter.messagebox.showerror("경고", "상품 가격을 입력해주세요")
            elif not productPrice.isdecimal():
                tkinter.messagebox.showerror("경고", "상품 가격이 유효하지 않습니다")

            elif not deliveryFee:
                tkinter.messagebox.showerror("경고", "배송비를 입력해주세요")
            elif not deliveryFee.isdecimal():
                tkinter.messagebox.showerror("경고", "배송비가 유효하지 않습니다")

            elif self.addProductDetailText.cget("fg") == "#b4b4b4" or not productDetail.strip():
                tkinter.messagebox.showerror("경고", "상세정보를 입력해주세요")

            else:
                productTags = ','.join(tag_list)
                sendMsg = ["registProduct", productName, productCategory, productCondition, productTags, productPrice,
                           deliveryFee]
                sendMsg += option_list
                sendMsg.append(productDetail.rstrip("\n"))
                sendMsg += selectedImgsBinary  # 10, 11, 12, 13
                sendMsg.append("판매 중")

            sendMsg_len = ["registProduct", len(pickle.dumps(sendMsg))]
            sock.send(pickle.dumps(sendMsg_len))
            sock.send(pickle.dumps(sendMsg))
            recvMsg = pickle.loads(sock.recv(1024))

            if recvMsg[0] == "registProduct":
                if recvMsg[1]:
                    tkinter.messagebox.showinfo("알림", "상품 등록이 완료되었습니다")
                    self.addProductFrame.destroy()
                else:
                    tkinter.messagebox.showinfo("오류", "다시 시도해주세요")

            ##################################### 서버 메시지핸들러 등록 / 페이지 이동 추가

        except Exception as ex:
            print(ex)
        # # message send
        pass


class SelectCategory(tkinter.Frame):  # 카테고리 선택 프레임
    def __init__(self, window, back, frame):
        tkinter.Frame.__init__(self, window)
        self.window = window
        self.back = back
        self.addProductLabel_category = frame

        # 카테고리 선택 프레임
        self.setCategoryFrame = tkinter.Frame(self.window, width=500, height=750, bg='white')
        self.setCategoryFrame.place(x=0, y=0)

        # 카테고리 상단 프레임
        self.setCategoryFrame_top = tkinter.Frame(self.setCategoryFrame, width=500, height=50, bg='white')
        self.setCategoryFrame_top.place(x=0, y=0)

        self.setCategoryButton_back = tkinter.Button(self.setCategoryFrame_top, bg='white', border=0,
                                                     text="〈", font=("맑은 고딕", 17, 'bold'))
        self.setCategoryButton_back.place(x=10, y=0)
        self.setCategoryButton_back.bind("<Button-1>",
                                         lambda event, frame=self.setCategoryFrame: self.back(event, frame))

        self.setCategoryLabel_text = tkinter.Label(self.setCategoryFrame_top, bg='white', border=0,
                                                   text="카테고리", font=("맑은 고딕", 15, 'bold'))
        self.setCategoryLabel_text.place(x=40, y=10)

        # 카테고리 중앙 프레임
        self.setCategoryFrame_center = tkinter.Frame(self.setCategoryFrame, width=500, height=700, bg='white')
        self.setCategoryFrame_center.place(x=0, y=50)

        self.setCategoryScrollFrame = ScrollFrame(self, self.setCategoryFrame_center)
        self.setCategoryScrollFrame.canvas.configure(height=700)
        self.setCategoryScrollFrame.configure(height=750)

        self.setCategoryFrame_inner = tkinter.Frame(self.setCategoryScrollFrame.viewPort, width=500, height=750,
                                                    bg="white")
        self.setCategoryFrame_inner.pack()

        self.addProduct_underline = tkinter.Label(self.setCategoryFrame_inner, bg='#e5e5e5', width=66, height=1,
                                                  border=0)
        self.addProduct_underline.place(x=18, y=43)

        self.setCategoryLabel = tkinter.Label(self.setCategoryFrame_inner, width=46, height=2, bg="white",
                                              text="전체", font=("맑은 고딕", 12, "bold"), fg='gray', anchor='w')
        self.setCategoryLabel.place(x=18, y=10)

        self.categorys = ["의류", "신발", "액세서리", '전자기기', '가전제품', '여가생활', '가구', '생활용품', '식품', '반려동물용품', '유아', '공구',
                          '도서/티켓/문구']
        self.categoryButtons = []
        for i in range(len(self.categorys)):
            setCategoryButton = tkinter.Button(self.setCategoryFrame_inner, text=f"{self.categorys[i]}")
            setCategoryButton.configure(font=("맑은 고딕", 15, "bold"), border=0, bg='white', width=50, anchor='w')
            setCategoryButton.bind("<Button-1>",
                                   lambda event, Button=setCategoryButton: self.clickCategory(event, Button))
            setCategoryButton.place(x=18, y=90 + i * 50)
            if self.addProductLabel_category.cget("text") == self.categorys[i]:
                setCategoryButton.configure(fg='#dc0c1c')
            self.categoryButtons.append(setCategoryButton)

    def clickCategory(self, e, Button):
        # print(self.categorys[self.categoryButtons.index(Button)])
        self.addProductLabel_category.configure(fg="black",
                                                text=f"{self.categorys[self.categoryButtons.index(Button)]}")
        self.back(e, frame=self.setCategoryFrame)


class SelectCondition(tkinter.Frame):  # 상태 선택 프레임
    def __init__(self, window, back, frame):
        tkinter.Frame.__init__(self, window)
        self.window = window
        self.back = back
        self.addProductLabel_condition = frame

        # 상품 상태 전체 프레임
        self.setConditionFrame = tkinter.Frame(self.window, width=500, height=750, bg="#000000")
        self.setConditionFrame.place(x=0, y=0)

        # 상태 상단 프레임
        self.setConditionFrame_top = tkinter.Frame(self.setConditionFrame, width=500, height=50, bg='white')
        self.setConditionFrame_top.place(x=0, y=0)

        self.setConditionButton_back = tkinter.Button(self.setConditionFrame_top, bg='white', border=0,
                                                      text="〈", font=("맑은 고딕", 17, 'bold'))
        self.setConditionButton_back.place(x=10, y=0)
        self.setConditionButton_back.bind("<Button-1>",
                                          lambda event, frame=self.setConditionFrame: self.back(event, frame))

        self.setConditionLabel_text = tkinter.Label(self.setConditionFrame_top, bg='white', border=0,
                                                    text="상품상태", font=("맑은 고딕", 15, 'bold'))
        self.setConditionLabel_text.place(x=40, y=10)

        # 상태 선택 중앙 프레임
        self.setConditionFrame_center = tkinter.Frame(self.setConditionFrame, width=500, height=700, bg='white')
        self.setConditionFrame_center.place(x=0, y=50)

        self.setConditionLabel = tkinter.Label(self.setConditionFrame_center, width=46, height=1, bg="white",
                                               text="상품상태는 어떤가요?", font=("맑은 고딕", 22, "bold"), fg='black', anchor='w')
        self.setConditionLabel.place(x=18, y=10)

        self.Conditions = {'새 상품 (미사용)': '사용하지 않은 새 상품',
                           '사용감 없음': '사용은 했지만 눈에 띄는 흔적이나 얼룩이 없음',
                           '사용감 적음': '눈에 띄는 흔적이나 얼룩이 약간 있음',
                           '사용감 많음': '눈에 띄는 흔적이나 얼룩이 많이 있음',
                           '고장/파손 상품': '기능 이상이나 외관 손상 등을 수리/수선이 필요'}
        self.ConditionButtons = []
        for i in range(len(self.Conditions)):
            setConditionLabel = tkinter.Label(self.setConditionFrame_center, bg="white", border=0, width=60, height=6)
            setConditionLabel.place(x=25, y=90 + i * 100)

            setConditionButton = tkinter.Label(setConditionLabel, text=f"{list(self.Conditions.keys())[i]}")
            setConditionButton.place(x=0, y=0)
            setConditionButton.config(font=("맑은 고딕", 17, "bold"), border=0, bg='white', width=50, anchor='w')

            setConditionDetail = tkinter.Label(setConditionLabel, text=f"{list(self.Conditions.values())[i]}")
            setConditionDetail.place(x=0, y=38)
            setConditionDetail.config(font=("맑은 고딕", 13, "bold"), border=0, bg='white', width=50, anchor='w',
                                      fg='#8d8d8d')

            setConditionLabel.bind("<Button-1>",
                                   lambda event, Button=setConditionButton: self.clickCondition(event, Button))
            setConditionButton.bind("<Button-1>",
                                    lambda event, Button=setConditionButton: self.clickCondition(event, Button))
            setConditionDetail.bind("<Button-1>",
                                    lambda event, Button=setConditionButton: self.clickCondition(event, Button))

            if self.addProductLabel_condition.cget("text") == list(self.Conditions.keys())[i]:
                setConditionButton.configure(fg='#dc0c1c')
                setConditionDetail.configure(fg='#dc0c1c')

            self.ConditionButtons.append(setConditionButton)

    def clickCondition(self, e, Button):
        self.addProductLabel_condition.configure(fg="black",
                                                 text=f"{Button.cget('text')}")
        self.back(e, frame=self.setConditionFrame)


class SelectOption(tkinter.Frame):  # 옵션 선택 프레임
    def __init__(self, window, back, option_list, addProductSelOpText):
        tkinter.Frame.__init__(self, window)
        self.window = window
        self.back = back
        self.option_list = option_list
        self.addProductSelOpText = addProductSelOpText
        # print(option_list)

        # 옵션 선택 프레임
        self.selectOptionFrame = tkinter.Frame(self.window, width=500, height=750, bg='white')
        self.selectOptionFrame.place(x=0, y=0)

        # 옵션선택 상단 프레임
        self.selectOptionFrame_top = tkinter.Frame(self.selectOptionFrame, width=500, height=50, bg='white')
        self.selectOptionFrame_top.place(x=0, y=0)

        self.selectOptionButton_back = tkinter.Button(self.selectOptionFrame_top, bg='white', border=0,
                                                      text="〈", font=("맑은 고딕", 17, 'bold'))
        self.selectOptionButton_back.place(x=10, y=0)
        self.selectOptionButton_back.bind("<Button-1>",
                                          lambda event, frame=self.selectOptionFrame: self.back(event, frame))

        self.selectOptionLabel_text = tkinter.Label(self.selectOptionFrame_top, bg='white', border=0,
                                                    text="옵션선택", font=("맑은 고딕", 15, 'bold'))
        self.selectOptionLabel_text.place(x=40, y=10)

        # 옵션선택 중앙 프레임
        self.selectOptionFrame_center = tkinter.Frame(self.selectOptionFrame, width=500, height=700, bg='white')
        self.selectOptionFrame_center.place(x=0, y=50)

        self.selectOptionLabel = tkinter.Label(self.selectOptionFrame_center, width=46, height=1, bg="white",
                                               text="옵션을 선택해주세요", font=("맑은 고딕", 20, "bold"), fg='black', anchor='w')
        self.selectOptionLabel.place(x=18, y=10)

        self.selectOptionAmountLabel = tkinter.Label(self.selectOptionFrame_center, bg='white',
                                                     fg='gray', text="수량", font=("맑은 고딕", 14, "bold"))
        self.selectOptionAmountLabel.place(x=30, y=90)

        self.selectOptionAmountImg = tkinter.PhotoImage(file="./imgs/addproduct/optionAmount.PNG")
        self.selectOptionAmountLabel_entry = tkinter.Label(self.selectOptionFrame_center, bg="white", border=0,
                                                           image=self.selectOptionAmountImg)
        self.selectOptionAmountLabel_entry.place(x=100, y=80)

        self.selectOptionEntry = tkinter.Entry(self.selectOptionAmountLabel_entry, bg="white", width=25, border=0,
                                               fg='black', font=("맑은 고딕", 14, "bold"))
        self.selectOptionEntry.place(x=25, y=10)
        self.selectOptionEntry.insert(0, self.option_list[0])

        self.selectOptionAmountLabel_text = tkinter.Label(self.selectOptionAmountLabel_entry, bg="white", border=0,
                                                          fg='gray', font=("맑은 고딕", 14), text="개")
        self.selectOptionAmountLabel_text.place(x=325, y=10)

        self.selectOptionExcangeLabel = tkinter.Label(self.selectOptionFrame_center, bg='white',
                                                      fg='gray', text="교환", font=("맑은 고딕", 14, "bold"))
        self.selectOptionExcangeLabel.place(x=30, y=170)

        self.exchange = tkinter.IntVar()
        self.selectedRadioText = "불가"
        # self.selectOptionRaio_exchange1 = tkinter.Radiobutton(self.selectOptionFrame_center, bg='white', variable=self.exchange, value=0,
        #                                              fg='gray', text="가능", font=("맑은 고딕", 14, "bold"))
        # self.selectOptionRaio_exchange2 = tkinter.Radiobutton(self.selectOptionFrame_center, bg='white', variable=self.exchange, value=1,
        #                                              fg='gray', text="불가", font=("맑은 고딕", 14, "bold"))
        self.exchangeN_sel = tkinter.PhotoImage(file="./imgs/addproduct/exchangNego_sel.png")
        self.exchangeN_desel = tkinter.PhotoImage(file="./imgs/addproduct/exchangNego_desel.png")
        self.selectOptionRaio_exchange1 = tkinter.Radiobutton(self.selectOptionFrame_center, bg='white',
                                                              image=self.exchangeN_desel,
                                                              selectimage=self.exchangeN_sel,
                                                              indicatoron=False, variable=self.exchange, value=0, bd=0,
                                                              text="불가")
        self.exchangeP_sel = tkinter.PhotoImage(file="./imgs/addproduct/exchangPosi_sel.png")
        self.exchangeP_desel = tkinter.PhotoImage(file="./imgs/addproduct/exchangPosi_desel.png")
        self.selectOptionRaio_exchange2 = tkinter.Radiobutton(self.selectOptionFrame_center, bg='white',
                                                              indicatoron=False, selectimage=self.exchangeP_sel,
                                                              variable=self.exchange, value=1,
                                                              image=self.exchangeP_desel, bd=0, text="가능")

        self.selectOptionRaio_exchange1.place(x=97, y=160)
        self.selectOptionRaio_exchange2.place(x=287, y=160)

        self.selectOptionRaio_exchange1.bind("<Button-1>",
                                             lambda e, radio=self.selectOptionRaio_exchange1: self.selectRadioButton(e,
                                                                                                                     radio))
        self.selectOptionRaio_exchange2.bind("<Button-1>",
                                             lambda e, radio=self.selectOptionRaio_exchange2: self.selectRadioButton(e,
                                                                                                                     radio))

        if self.option_list[1] == "가능":
            self.selectOptionRaio_exchange2.select()
        else:
            self.selectOptionRaio_exchange1.select()

        self.selectOptionAddressLabel = tkinter.Label(self.selectOptionFrame_center, bg='white',
                                                      fg='gray', text="지역", font=("맑은 고딕", 14, "bold"))
        self.selectOptionAddressLabel.place(x=30, y=260)

        self.selectOptionAddressImg = tkinter.PhotoImage(file="./imgs/addproduct/optionAmount.PNG")
        self.selectOptionAddressLabel_entry = tkinter.Label(self.selectOptionFrame_center, bg="white", border=0,
                                                            image=self.selectOptionAmountImg)
        self.selectOptionAddressLabel_entry.place(x=100, y=250)

        self.selectOptionEntry_adress = tkinter.Entry(self.selectOptionAddressLabel_entry, bg="white", width=30,
                                                      border=0,
                                                      fg='black', font=("맑은 고딕", 14, "bold"))
        self.selectOptionEntry_adress.place(x=20, y=11)
        self.selectOptionEntry_adress.insert(0, self.option_list[2])

        self.completeImg = tkinter.PhotoImage(file="./imgs/addproduct/optionComplete.PNG")
        self.selectOptionButton_complete = tkinter.Label(self.selectOptionFrame_center, image=self.completeImg,
                                                         border=0)
        self.selectOptionButton_complete.place(x=30, y=340)
        self.selectOptionButton_complete.bind(
            "<Button-1>",
            lambda e, frame=self.selectOptionFrame, option_list=self.option_list: self.clickComplete(e, frame,
                                                                                                     option_list=option_list)
        )

        self.alertLabel = tkinter.Label(self.selectOptionFrame_center, bg='white', fg='red', font=("맑은 고딕", 12, ""),
                                        border=0)
        self.alertLabel.place(x=30, y=350)

    def selectRadioButton(self, e, radio):
        self.selectedRadioText = radio.cget("text")

    def clickComplete(self, e, frame, option_list):
        self.option_list = option_list
        if not self.selectOptionEntry.get():
            self.selectOptionEntry.insert(0, 1)

        elif not self.selectOptionEntry.get().isdecimal():
            win32api.MessageBox(0, "수량이 유효하지 않습니다.", "에러", 16)
            return

        self.option_list = [int(self.selectOptionEntry.get()),
                            self.selectOptionExcangeLabel.cget("text") + self.selectedRadioText,
                            self.selectOptionEntry_adress.get()]

        self.addProductSelOpText.configure(
            text=f"{self.option_list[0]}개 • {self.option_list[1]} • {self.option_list[2]}")
        self.back(e, frame)


class EditInform(tkinter.Frame):
    def __init__(self, window):
        tkinter.Frame.__init__(self, window)
        self.window = window
        # self.window.geometry("500x750+1200+100")  # pc
        self.window.geometry("500x750+700+10")  # desktop

        self.login_font = tkinter.font.Font(family="맑은 고딕", size=20, weight="bold")
        self.basic_font = tkinter.font.Font(family="맑은 고딕", size=14)
        self.overlab_font = tkinter.font.Font(family="맑은 고딕", size=10)
        self.combo_font = tkinter.font.Font(family="맑은 고딕", size=11)
        self.logo_img = tk.PhotoImage(file="imgs/home_top/logoBtn.png")
        self.back_img = tk.PhotoImage(file="imgs/back.png")

        self.editMainFrame = tkinter.Frame(self.window, width=500, height=750, bg="white", bd=0)
        self.editMainFrame.place(x=0, y=0)

        # 로고
        self.make_win_logo_label = tk.Label(self.editMainFrame, width=170, height=40, image=self.logo_img, bg="white")
        self.make_win_logo_label.place(x=330, y=10)

        # self.make_win.geometry("500x750+700+100")
        # self.editMainFrame.geometry("500x750+700+10")
        # self.editMainFrame.title("회원가입")
        self.make_back_btn = tk.Button(self.editMainFrame, bg="white", font=self.basic_font, bd=0, image=self.back_img,
                                       cursor="hand2",
                                       highlightthickness=0, command=lambda: [self.back(self.editMainFrame)])
        self.make_back_btn.place(x=30, y=20)
        self.make_name_label = tk.Label(self.editMainFrame, text="이름", bg="white", font=self.basic_font)
        self.make_name_label.place(x=30, y=80)
        self.make_name_entry = tk.Entry(self.editMainFrame, font=self.basic_font, bg="gainsboro", width=43, bd=0,
                                        highlightthickness=0)
        self.make_name_entry.place(x=30, y=120)
        self.make_birth_label = tk.Label(self.editMainFrame, text="생년월일", bg="white", font=self.basic_font)
        self.make_birth_label.place(x=30, y=160)
        self.make_birthy_entry = tk.Entry(self.editMainFrame, font=self.basic_font, bg="gainsboro", width=11, bd=0,
                                          highlightthickness=0)
        self.make_birthy_entry.place(x=30, y=200)
        self.make_birthm_entry = tk.Entry(self.editMainFrame, font=self.basic_font, bg="gainsboro", width=11, bd=0,
                                          highlightthickness=0)
        self.make_birthm_entry.place(x=170, y=200)
        self.make_birthd_entry = tk.Entry(self.editMainFrame, font=self.basic_font, bg="gainsboro", width=11, bd=0,
                                          highlightthickness=0)
        self.make_birthd_entry.place(x=310, y=200)

        self.make_id_label = tk.Label(self.editMainFrame, text="ID", bg="white", font=self.basic_font)
        self.make_id_label.place(x=30, y=240)
        self.make_id_entry = tk.Label(self.editMainFrame, font=self.basic_font, bg="gainsboro", width=39, bd=0,
                                      highlightthickness=0, anchor='w')
        self.make_id_entry.place(x=30, y=280)
        self.make_id_entry.bind("<Button-1>", self.idClick)

        self.make_pw_label = tk.Label(self.editMainFrame, text="Password", bg="white", font=self.basic_font)
        self.make_pw_label.place(x=30, y=320)
        self.make_pw_entry = tk.Entry(self.editMainFrame, show="*", font=self.basic_font, bg="gainsboro", width=43,
                                      bd=0,
                                      highlightthickness=0)
        self.make_pw_entry.place(x=30, y=360)

        self.make_email_label = tk.Label(self.editMainFrame, text="Email", bg="white", font=self.basic_font)
        self.make_email_label.place(x=30, y=400)
        self.make_email_entry = tk.Entry(self.editMainFrame, font=self.basic_font, bg="gainsboro", width=22, bd=0,
                                         highlightthickness=0)
        self.make_email_entry.place(x=30, y=440)
        self.make_email_combo = ttk.Combobox(self.editMainFrame, values=email, font=self.combo_font)
        self.make_email_combo.set("선택")
        self.make_email_combo.place(x=280, y=440)
        self.make_phone_label = tk.Label(self.editMainFrame, text="연락처", bg="white", font=self.basic_font)
        self.make_phone_label.place(x=30, y=480)
        self.make_phone_combo = ttk.Combobox(self.editMainFrame, values=phone, font=self.combo_font, width=10)
        self.make_phone_combo.set("선택")
        self.make_phone_combo.place(x=30, y=520)
        self.make_phone_entry = tk.Entry(self.editMainFrame, font=self.basic_font, bg="gainsboro", width=31, bd=0,
                                         highlightthickness=0)
        self.make_phone_entry.place(x=150, y=520)
        self.make_addr_label = tk.Label(self.editMainFrame, text="주소", bg="white", font=self.basic_font)
        self.make_addr_label.place(x=30, y=560)
        self.make_addr_entry = tk.Entry(self.editMainFrame, font=self.basic_font, bg="gainsboro", width=43, bd=0,
                                        highlightthickness=0)
        self.make_addr_entry.place(x=30, y=600)

        self.usermake_btn = tk.Button(self.editMainFrame, text="정보수정", width=39, font=self.basic_font, fg="white",
                                      bg="#d80c18",
                                      cursor="hand2", bd=0, activebackground="#a60a14",
                                      activeforeground="white")
        self.usermake_btn.place(x=30, y=680)
        self.usermake_btn.bind("<Button-1>", self.editInform)

        # 정보 불러와서 넣기
        self.recvData = self.loadData()
        print(list(self.recvData[1][0]))
        if self.recvData[0] == "load_Inform":
            print("정보 기입 시작")
            inform_list = list(self.recvData[1][0])
            self.make_id_entry.configure(text=inform_list[0])
            self.make_pw_entry.insert(0, inform_list[1])
            self.make_name_entry.insert(0, inform_list[2])
            self.make_birthy_entry.insert(0, inform_list[3][:4])
            self.make_birthm_entry.insert(0, inform_list[3][4:6])
            self.make_birthd_entry.insert(0, inform_list[3][6:])
            self.make_email_entry.insert(0, inform_list[4][:inform_list[4].index("@")])

            for e in email:
                if e == inform_list[4][inform_list[4].index("@"):]:
                    self.make_email_combo.current(email.index(e))
            for p in phone:
                if p == inform_list[5]:
                    self.make_phone_combo.current(phone.index(p))
            self.make_phone_entry.insert(0, inform_list[6])
            self.make_addr_entry.insert(0, inform_list[7])

    def loadData(self):
        sendMsg = ["load_Inform"]
        sock.send(pickle.dumps(sendMsg))
        recvMsg = pickle.loads(sock.recv(4096))
        return recvMsg

    def idClick(self, e):
        tkinter.messagebox.showwarning("경고", "ID는 수정이 불가능합니다.")

    def editInform(self, e):
        id = self.make_id_entry.cget("text")
        pw = self.make_pw_entry.get()
        name = self.make_name_entry.get()
        birth = self.make_birthy_entry.get() + self.make_birthm_entry.get() + self.make_birthd_entry.get()
        email = self.make_email_entry.get() + self.make_email_combo.get()
        agency = self.make_phone_combo.get()
        phone = self.make_phone_entry.get()
        addr = self.make_addr_entry.get()

        # sendMsg = ["editInform" ,f"'{id}','{pw}','{name}','{birth}','{email}','{agency}','{phone}','{addr}'"]
        # sock.send(pickle.dumps(sendMsg))
        # recvMsg = pickle.loads(sock.recv(1024))
        # if recvMsg[0] == "editInform":
        #     if recvMsg[1]:
        #         tkinter.MessageBox()
        print(id, pw, name, birth, email, agency, phone, addr, "정보 1111")
        self.mysql_add(id, pw, name, birth, email, agency, phone, addr)

    def mysql_add(self, id, pw, name, birth, email, agency, phone, addr):
        print(id, pw, name, birth, email, agency, phone, addr, "정보 222222")
        count_name = 0
        count_email = 0
        count_agency = 0
        p = re.compile('[ㄱ-힣]')
        for i in range(len(name)):
            r = p.search(name[i])
            print(r)
            if r != None:  # 한글이 있으면
                count_name += 1
        if "선택" in email:  # 도메인을 선택 안한 경우
            count_email += 1
        if "선택" == agency:
            count_agency += 1
        if count_name == len(name) and birth.isdigit() and len(
                birth) == 8 and count_email == 0 and count_agency == 0 and phone.isdigit() and pw != "" and addr != "":
            # if id_check == 2:
            # sendMsg = ["editInform", f"'{id}','{pw}','{name}','{birth}','{email}','{agency}','{phone}','{addr}'"]
            sendMsg = ["editInform", [id, pw, name, birth, email, agency, phone, addr]]
            encoded_Msg = pickle.dumps(sendMsg)
            sock.send(encoded_Msg)
            recvMsg = sock.recv(1024)
            decode_Msg = pickle.loads(recvMsg)
            if decode_Msg[0] == "editInform":
                if decode_Msg[1]:
                    win32api.MessageBox(0, "정보가 수정되었습니다.", "알림", 0)
                    self.editMainFrame.destroy()
                else:
                    win32api.MessageBox(0, "정보 수정에 실패하였습니다.\n다시 시도해주세요.", "에러", 0)
            # else:
            #     win32api.MessageBox(0, "중복체크 하십시오.", "알림", 0)
        elif count_name != len(name):
            win32api.MessageBox(0, "잘못된 이름입니다.", "에러", 16)
        elif not birth.isdigit() or len(birth) != 8:
            win32api.MessageBox(0, "잘못된 생년월일입니다.", "에러", 16)
        elif pw == "":
            win32api.MessageBox(0, "비밀번호를 입력해주세요.", "에러", 16)
        elif count_email != 0:
            win32api.MessageBox(0, "도메인을 선택하세요.", "에러", 16)
        elif count_agency != 0:
            win32api.MessageBox(0, "통신사를 선택하세요.", "에러", 16)
        elif not phone.isdigit():
            win32api.MessageBox(0, "잘못된 전화번호입니다.", "에러", 16)
        elif addr == "":
            win32api.MessageBox(0, "주소를 입력해주세요.", "에러", 16)

    def back(self, e):
        self.editMainFrame.destroy()

logined_id = ""
complete = 1
while complete:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', PORT))
    window = login(tkinter.Tk())
    window.window.mainloop()

atexit.register(handle_exit, "프로그램이 종료되었습니다.")
sock.send(pickle.dumps(["!disconnect"]))