import socketserver
import threading
import pymysql
import pickle


# HOST = '172.30.1.79'
HOST = 'localhost'
# HOST = '192.168.31.23'
PORT = 9950

lock = threading.Lock()
# admin = ["admin"]
user_list = []

con = pymysql.connect(host='192.168.31.23', user='team5', password="1234", port=3306, db="team5",charset='utf8')
#con = pymysql.connect(host='localhost', user='root', password="0000", port=3306, db="team5",charset='utf8')
cur = con.cursor()

cur.execute("SELECT id FROM user;")
for i in cur:
    user_list.append(i[0])

# print(user_list)


class UserManager:

    def __init__(self):
        self.users = {} #client side를 통해 접속한 유저 객체를 담는 변수
        self.per = True

    def sendUserList(self):
        pass

    def addUser(self, user_id, conn, addr):
        if user_id in self.users:
            # conn.send('already exist.\n'.encode())
            return None
        lock.acquire() #thread의 lock객체는 공유데이터를 다룰 때 스레드를 독립성을 보장
        self.users[user_id] = (conn, addr)  # 이사이에는 동기화 되어야 하는 작업이 들어가야한다.
        lock.release() #독립성 보장해야하는 작업이 끝나면 release로 풀어줌

        # for key in self.users.keys():
        #     #실시간 self.users 딕셔너리에서 사용자 이름만 뜯어서 문자열로 만드는과정
        #     self.user_list_str += " "+key
        # self.sendMessageToAll(self.user_list_str)
        #모든 접속 중인 클라이언트 객체들에게 위에서 만든 명부 문자열을 송출하는 함수 호출
        return user_id

    def sendMessageToAll(self, msg):
        pass

    def removeUser(self, username):
        if username not in self.users:
            return
        lock.acquire()
        del self.users[username]
        lock.release()
        self.sendMessageToAll('[%s] 퇴장.' % username)
        self.user_list_str = "^^"
        for key in self.users.keys():
            self.user_list_str += " " + key
        self.sendMessageToAll(self.user_list_str)
    def forced_exit(self, username):
        if username not in self.users:
            return
        self.users[username][0].close()
        user_list.remove(username)
        lock.acquire()
        del self.users[username]
        lock.release()
        self.sendMessageToAll('[%s] 강제퇴장 당하셨습니다.' % username)
        self.user_list_str = "^^"
        for key in self.users.keys():
            self.user_list_str += " " + key
        self.sendMessageToAll(self.user_list_str)


    def upload_sales(self, msg):
        print("상품 등록 시작")

        # sql = f"INSERT INTO bungaejangter.sales VALUES({sqlString});"
        sql = f"INSERT INTO team5.sales VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        msg[7] = msg[7][:-1]
        values = tuple(msg)
        cur.execute(sql, values)
        con.commit()

        #tags = values[4].replace("#", "").split(",")
        tags = values[1].split(" ")
        for tag in tags:
            sql_check = f"SELECT * FROM team5.category WHERE c_name='{tag}';"
            if not cur.execute(sql_check):
                print("태그 추가 시작")
                sql_addTag = "INSERT INTO team5.category VALUES (%s);"
                data = (tag)
                cur.execute(sql_addTag, data)
                con.commit()
            print("태그 추가 성공")
        return "success"

    def click_category(self, c_name):
        print("카테고리 클릭")
        sql = f"SELECT * FROM team5.sales WHERE s_category = '{c_name}'"
        try:
            cur.execute(sql)
            c_click = list(cur.fetchall())

            serialized_data = pickle.dumps(c_click)

            # 데이터 길이 전송
            data_length = len(serialized_data)
        except:
            data_length = 0
            c_click = []

        return data_length, c_click

    def recent_product(self, s_name):
        print("최근 본 상품")
        try:
            sql = f"SELECT s_img FROM team5.sales WHERE s_name = '{s_name}'"
            cur.execute(sql)
            cur_img = [cur.fetchall()[0][0]]

            serialized_data = pickle.dumps(cur_img)

            # 데이터 길이 전송
            data_length = len(serialized_data)
        except:
            data_length = 0
            cur_img = []

        return data_length, cur_img

    def relative_product(self, search_word):
        print("검색어 관련 상품")
        try:
            sql = f"SELECT * FROM team5.sales WHERE s_name LIKE '%{search_word}%';"
            cur.execute(sql)
            s_list = cur.fetchall()

            serialized_data = pickle.dumps(s_list)

            # 데이터 길이 전송
            data_length = len(serialized_data)
        except:
            data_length = 0
            s_list = ()

        return data_length, s_list

    def search_storage(self,user_id, text):
        print("채팅 저장")
        sql = f"INSERT INTO team5.search_record VALUES('{user_id}','{text}')"
        cur.execute(sql)
        con.commit()

    def recent_search(self,user_id):
        print("최근 검색어")
        try:
            sql = f"SELECT sr_text FROM team5.search_record WHERE sr_id = '{user_id}'"
            cur.execute(sql)
            rs_list = cur.fetchall()

            serialized_data = pickle.dumps(rs_list)

            data_length = len(serialized_data)
        except:
            data_length = 0
            rs_list = ()

        return data_length, rs_list

    def recent_search_del(self,user_id, text):
        print("최근 검색어 삭제")
        sql = f"DELETE FROM team5.search_record WHERE sr_id = '{user_id}' and sr_text = '{text}'"
        cur.execute(sql)
        con.commit()
    def recent_search_all_del(self,user_id):
        print("최근 검색어 전체 삭제")
        sql = f"DELETE FROM team5.search_record WHERE sr_id = '{user_id}';"
        cur.execute(sql)
        con.commit()

    def search_count(self):
        print("제일 많은 검색어")
        try:
            sql = "SELECT sr_text FROM team5.search_record"
            cur.execute(sql)
            sc_list = cur.fetchall()

            serialized_data = pickle.dumps(sc_list)

            # 데이터 길이 전송
            data_length = len(serialized_data)
        except:
            data_length = 0
            sc_list = ()

        return data_length, sc_list

    def main_sales_click(self, s_id, s_name):
        print("메인 화면 상품 클릭")
        try:
            sql = f"SELECT * FROM team5.sales WHERE s_id='{s_id}' AND s_name='{s_name}';"
            cur.execute(sql)
            ms_list = cur.fetchall()

            serialized_data = pickle.dumps(ms_list)

            # 데이터 길이 전송
            data_length = len(serialized_data)
        except:
            data_length = 0
            ms_list = ()

        return data_length, ms_list

    def main_recent_click(self, s_name, s_price):
        print("최근 본 상품 클릭")
        # try:
        sql = f"SELECT * FROM team5.sales WHERE s_name LIKE %s AND s_price=%s"
        data = (s_name, s_price)
        cur.execute(sql, data)

        s_list = cur.fetchall()
        data = pickle.dumps(s_list)
        data_length = len(data)
        # except Exception as ex:
        #     print(ex)
        return data_length, s_list

    #def main_recent_click(self,user_id):
    #    print("최근 본 상품 클릭")
    #    # try:
    #    sql = f"SELECT * FROM team5.recent_sale WHERE rs_id = '{user_id}'"
    #    cur.execute(sql)
    #
    #    s_list = cur.fetchall()
    #    data = pickle.dumps(s_list)
    #    data_length = len(data)
    #    # except Exception as ex:
    #    #     print(ex)
    #    return data_length, s_list




    # 찜한 상품 보이기
    def main_like_click(self, user_id):
        print("찜한 상품 보이기")
        like_list = []
        try:
            sql = f"SELECT like_sale FROM team5.like_list WHERE like_id = '{user_id}';"
            cur.execute(sql)
            if cur.execute(sql) > 0:
                like_sale_name = cur.fetchall()
                for i in range(len(like_sale_name)):
                    sql2 = f"SELECT * FROM team5.sales WHERE s_name = '{like_sale_name[i][0]}';"
                    cur.execute(sql2)

                    ml_list = cur.fetchall()[0]

                    like_list.append(ml_list)
        except:
            ml_list = ()
            like_list = []
        # 완료된 리스트 길이
        data_length = len(pickle.dumps(like_list))
        return data_length, like_list
    # 찜하기
    def like_click(self, user_id, sale_name, like):
        print("상품 찜하기")
        print(like)
        sql = f"SELECT s_name FROM team5.sales WHERE s_name LIKE '%{sale_name}%'"
        cur.execute(sql)
        sale_name = cur.fetchall()[0][0]
        if like == True:
            sql = f"SELECT * FROM team5.like_list WHERE like_id = '{user_id}' and like_sale = '{sale_name}';"
            if cur.execute(sql) == 0:
                sql = f"INSERT INTO team5.like_list VALUES('{user_id}','{sale_name}');"
                cur.execute(sql)
                con.commit()
        else:
            sql = f"DELETE FROM team5.like_list WHERE like_id = '{user_id}' and like_sale = '{sale_name}';"
            cur.execute(sql)
            con.commit()

    # 메인 찜한 상품 지우기
    def main_like_delete(self, user_id, like_sale):
        print("찜한 상품 지우기")
        sql = f"DELETE FROM team5.like_list WHERE like_id = '{user_id}' and like_sale LIKE '%{like_sale}%'"
        cur.execute(sql)
        con.commit()

    def relation_search(self, click_widget):
        print("메인 화면 상품 클릭")
        try:
            sql = "SELECT c_name FROM team5.category"
            cur.execute(sql)
            category_list = cur.fetchall()

            serialized_data = pickle.dumps(category_list)

            # 데이터 길이 전송
            data_length = len(serialized_data)
        except:
            data_length = 0
            category_list = ()
        return data_length, category_list

    def chat_list(self,user_id):
        print("채팅 목록 확인 함수")
        chat_list = []
        try:
            sql = f"SELECT * FROM team5.chat_record;"
            cur.execute(sql)
            chat_in = cur.fetchall()
            # 내가 채팅 보낸 상품
            for i in range(len(chat_in)):
                print()
                if chat_in[i][0] == user_id:
                    sql2 = f"SELECT * FROM team5.sales WHERE s_id = '{chat_in[i][1]}' and s_name = '{chat_in[i][2]}'"
                    if cur.execute(sql2) > 0:
                        chat_send_sale = cur.fetchall()
                        for i in range(len(chat_send_sale)):
                            if chat_send_sale[i][0] == chat_send_sale[i-1][0] and chat_send_sale[i][1] == chat_send_sale[i-1][1]:
                                del list(chat_send_sale)[i]
                        chat_list.append(chat_send_sale)

            # 내가 채팅 받은 상품
            for j in range(len(chat_in)):
                sql3 = f"SELECT * FROM team5.sales WHERE s_id = '{user_id}' and s_name = '{chat_in[j][2]}';"
                if cur.execute(sql3) > 0:
                    chat_rec_sale = cur.fetchall()
                    chat_list.append(chat_rec_sale)
        except Exception as ex:
            print(ex)
            data_length = 0
            chat_list = []
        data_length = len(pickle.dumps(chat_list))
        return data_length, chat_list

    def chat_window_frame(self, user_id, sale_name):
        print("채팅창 로드 함수")
        chat_list = []
        try:
            sql = f"SELECT * FROM team5.sales WHERE s_name = '{sale_name}';"
            cur.execute(sql)
            chat_info = cur.fetchall()[0]

            chat_list.append(chat_info)
            sql2 = f"SELECT my_id,receive_id,chat_record FROM team5.chat_record WHERE chat_sale_name = '{sale_name}';"
            if cur.execute(sql2) > 0:
                chat_record = cur.fetchall()[0]

                chat_list.append(chat_record)
        except:
            data_length = 0
            chat_info = ()

        data_length = len(pickle.dumps(chat_list))

        return data_length, chat_list
    def chat_storage(self,user_id, other_id,sale_name, chat):
        print("채팅 저장 함수")
        chat = pickle.dumps(chat)
        sql = f"INSERT INTO team5.chat_record VALUES(%s,%s,%s,%s);"
        values = (user_id, other_id, sale_name, chat)
        cur.execute(sql, values)
        con.commit()

    # 최근 본 상품 저장
    def recent_sale(self, user_id, sale_name):
        print("최근 본 상품 저장")
        recent_sale_list = []
        sql = f"SELECT * FROM team5.sales WHERE s_id != '{user_id}' and s_name LIKE '%{sale_name}%';"
        cur.execute(sql)
        recent_sale2 = cur.fetchall()[0]
        sql = f"SELECT * FROM team5.recent_sale WHERE rs_id = '{user_id}';"
        cur.execute(sql)
        count = 0
        if len(cur.fetchall()) == 0:
            #recent_sale_list.insert(0, cur.fetchall()[0])
            sql = f"INSERT INTO team5.recent_sale VALUES('{user_id}','{recent_sale2[0]}','{recent_sale2[1]}', '{count + 1}')"
            cur.execute(sql)
            con.commit()
        else:
            for i in range(len(cur.fetchall())):
                if len(cur.fetchall()) == 5:
                    recent_sale_list.pop()
                recent_sale_list.insert(0,cur.fetchall()[i][0])
                sql = f"delete from team5.recent_sale where rs_id = '{user_id}'"
                cur.execute(sql)
                con.commit()
                sql = f"INSERT INTO team5.recent_sale VALUES('{user_id}','{recent_sale2[0]}','{recent_sale2[1]}', '{count + 1}')"
                cur.execute(sql)
                con.commit()


    def talk_pay(self, msg):
        print("채팅 결제")
        try:
            sql=f"SELECT * FROM team5.sales WHERE s_name = '{msg[1]}';"
            cur.execute(sql)

            talk_pay = cur.fetchall()

            serialized_data = pickle.dumps(talk_pay)

            # 데이터 길이 전송
            data_length = len(serialized_data)
        except:
            data_length = 0
            talk_pay = ()

        return data_length, talk_pay
    def load_Inform(self, user_id ,msg):
        print("정보 불러오기 시작")
        sql = f"SELECT * FROM team5.user WHERE id = '{user_id}';"
        cur.execute(sql)

        inform_list = cur.fetchall()
        return inform_list
    def update_inform(self, user_id, msg):
        print("개인정보수정 시작")
        il = msg[1]
        try:
            sql = "UPDATE team5.user SET password=%s, name=%s, birth=%s, email=%s, mc=%s, pn=%s, address=%s WHERE id=%s"
            data = (il[1], il[2], il[3], il[4], il[5], il[6], il[7], il[0])
            cur.execute(sql, data)
            con.commit()
            return "success"
        except Exception as ex:
            print(ex, "정보 수정 에러")
            return ""
    def loadSale(self, user_id):
        print("올해 수익 불러오기")
        total_sales = 0
        msg = ""
        try:
            sql = "SELECT s_price FROM team5.sales WHERE s_id=%s AND s_sale=%s;"
            data=(user_id, '판매완료')
            cur.execute(sql, data)
            for i in cur.fetchall():
                total_sales += int(i[0])
            msg = "success"
        except Exception as ex:
            print(ex, "수익 불러오기 실패")
            msg = "fail"

        return total_sales, msg
    def update_userRecentCategory(self, user_id, category):
        print("유저 최근 카테고리 업데이트")
        try:
            sql = "UPDATE team5.user SET recentcategory=%s WHERE id=%s;"
            data = (category, user_id)
            cur.execute(sql, data)
            con.commit()
        except Exception as ex:
            print(ex)
    def loadRecentCategory(self, user_id):
        print("최근 카테고리 불러오기")
        recentCategory = "의류"
        try:
            sql = "SELECT recentcategory FROM team5.user WHERE id=%s;"
            cur.execute(sql, user_id)
            recentCategory = cur.fetchall()[0][0]
        except Exception as ex:
            print(ex)

        try:
            ret = ""
            sql = "SELECT * FROM team5.sales WHERE s_category=%s AND s_id!=%s AND s_sale=%s;"
            data=(recentCategory, user_id, '판매 중')
            cur.execute(sql, data)
            print("__________________ 카테고리 리스트 상위 3개")
            ret = cur.fetchall()[:3]
        except Exception as ex:
            print(ex, "-----ex")

        data_len = len(pickle.dumps(ret))
        print(data_len, "_____________카테고리 길이")

        return data_len, ret

    def change_productSale(self, state, dict):
        sql = "UPDATE team5.sales SET s_sale=%s WHERE "
        data = [state] + list(dict.values())
        dict_keys = list(dict.keys())
        for key in dict_keys:
            sql += f"{key}=%s"
            if key == dict_keys[-1]:
                sql += ";"
                break
            sql += " AND "
        print("-------------------------------")
        print(sql)
        print(data)

        cur.execute(sql, data)
        con.commit()
        print("success")

    def refreshMyFeed(self, id):
        sql = f"SELECT * FROM team5.sales WHERE s_id='{id}';"
        data_len, s_list = 0, ()
        try:
            cur.execute(sql)
            s_list = cur.fetchall()
            data_len = len(pickle.dumps(s_list))
            print(s_list)
        except:
            print(Exception, "피드 불러오기 실패")
        return data_len, s_list

    def refreshMySellList(self, id):
        sql = f"SELECT * FROM team5.sales WHERE s_id='{id}' AND s_sale='판매완료';"
        data_len, s_list = 0, ()
        try:
            cur.execute(sql)
            s_list = cur.fetchall()
            data_len = len(pickle.dumps(s_list))
            print(s_list)
        except:
            print(Exception, "피드 불러오기 실패")
        return data_len, s_list

    def messageHandler(self, user_id, msg): #강퇴하기나 이런 명령 여기서 하기
        try:
            print(msg)
            if msg[0] == "!disconnect":
                return -1

            if msg[0] == "registProduct":
                sendMsg = [msg[0]]
                try:
                    msg[0] = user_id
                    ret = self.upload_sales(msg)
                    sendMsg.append(ret)
                except Exception as ex:
                    print(ex, "1111111111111")
                    sendMsg.append("")
                self.sendPersonalMsg(user_id, sendMsg)
                return

            elif msg[0] == "click_category":
                data_length, c_click = self.click_category(msg[1])
                sendMsglen = [msg[0], data_length]
                self.sendPersonalMsg(user_id, sendMsglen)

                sendMsg = c_click
                self.sendPersonalMsg(user_id, sendMsg)
                return

            elif msg[0] == "recent_product":
                data_length, cur_img = self.recent_product(msg[1])
                sendMsg_dataLen = [msg[0], data_length]
                self.sendPersonalMsg(user_id, sendMsg_dataLen)

                sendMsg = cur_img
                self.sendPersonalMsg(user_id, sendMsg)
                return

            elif msg[0] == "relative_product":
                #data_length, s_list = self.relative_product(user_id,msg[1])
                data_length, s_list = self.relative_product(msg[1])
                sendMsg_dataLen = [msg[0], data_length]
                self.sendPersonalMsg(user_id, sendMsg_dataLen)

                sendMsg = list(s_list)
                self.sendPersonalMsg(user_id, sendMsg)
                return

            elif msg[0] == "main_sales_click":
                data_length, ms_list = self.main_sales_click(msg[1], msg[2])
                sendMsg_dataLen = [msg[0], data_length]
                self.sendPersonalMsg(user_id, sendMsg_dataLen)

                sendMsg = ms_list
                self.sendPersonalMsg(user_id, sendMsg)
                return

            elif msg[0] == "main_recent_click":
                print("test")
                data_length, s_list = self.main_recent_click(msg[1], msg[2])
                sendMsg_dataLen = [msg[0], data_length]
                self.sendPersonalMsg(user_id, sendMsg_dataLen)

                sendMsg = s_list
                self.sendPersonalMsg(user_id, sendMsg)
                return

            # elif "main_recent_click" in msg[0]:
            #     print(msg, "최근 본 상품")
            #     data_length, mr_list = self.main_recent_click(msg[0], msg[1])
            #     sendMsg_dataLen = [msg[0], data_length]
            #     self.sendPersonalMsg(user_id, sendMsg_dataLen)
            #
            #     sendMsg = mr_list
            #     self.sendPersonalMsg(user_id, sendMsg)
            #     return

            # 찜 하기
            elif msg[0] == "like_click":
                print(msg, "찜하기")
                self.like_click(user_id, msg[1], msg[2])
                return

            # 찜한 상품 보이기
            elif msg[0] == "main_like_click":
                print(msg, "찜한 상품 보이기")
                data_length, ml_list = self.main_like_click(user_id)
                sendMsg_dataLen = [msg[0], data_length]
                self.sendPersonalMsg(user_id, sendMsg_dataLen)

                sendMsg = ml_list
                self.sendPersonalMsg(user_id, sendMsg)
                return

            elif msg[0] == "main_like_delete":
                print(msg,"찜한 상품 지우기")
                self.main_like_delete(user_id,msg[1])

            elif msg[0] == "relation_search":
                print(msg, "연관 검색어")
                data_length, category_list = self.relation_search(msg[0])
                sendMsg_dataLen = [msg[0], data_length]
                self.sendPersonalMsg(user_id, sendMsg_dataLen)

                sendMsg = category_list
                self.sendPersonalMsg(user_id, sendMsg)
                return

            elif msg[0] == "search_storage":
                print(msg, "검색어 저장")
                self.search_storage(user_id, msg[1])

            elif msg[0] == "recent_search":
                print(msg, "최근 검색어")
                data_length, rs_list = self.recent_search(user_id)
                sendMsg_dataLen = [msg[0], data_length]
                self.sendPersonalMsg(user_id, sendMsg_dataLen)

                sendMsg = rs_list
                self.sendPersonalMsg(user_id, sendMsg)
                return

            elif msg[0] == "recent_search_del":
                print(msg,"최근 검색어 삭제")
                self.recent_search_del(user_id,msg[1])
                return

            elif msg[0] == "recent_search_all_del":
                print(msg,"최근 검색어 전체 삭제")
                self.recent_search_all_del(user_id)
                return

            elif msg[0] == "search_count":
                print("제일 많은 검색어")
                data_length, sc_list = self.search_count()
                sendMsg_dataLen = [msg[0], data_length]
                self.sendPersonalMsg(user_id, sendMsg_dataLen)

                sendMsg = sc_list
                self.sendPersonalMsg(user_id, sendMsg)
                return

            # 채팅 목록
            elif msg[0] == "chat_list":
                print(msg, "채팅 목록 확인")
                data_length, talk_fetchall = self.chat_list(user_id)
                sendMsg_dataLen = [msg[0], data_length]
                self.sendPersonalMsg(user_id, sendMsg_dataLen)

                sendMsg = talk_fetchall
                self.sendPersonalMsg(user_id, sendMsg)
                return
            # 채팅창 로드
            elif msg[0] == "chat_window_frame":
                print(msg, "채팅창 로드")
                data_length, chat_info = self.chat_window_frame(user_id,msg[1])
                sendMsg_dataLen = [msg[0], data_length]
                self.sendPersonalMsg(user_id, sendMsg_dataLen)

                sendMsg = chat_info
                self.sendPersonalMsg(user_id, sendMsg)
                return
            # 채팅 저장
            elif msg[0] == "chat_storage":
                print(msg, "채팅 저장")
                self.chat_storage(user_id, msg[1], msg[2], msg[3])
                return
            # 최근 본 상품 저장
            elif msg[0] == "recent_sale":
                print(msg, "최근 본 상품 저장")
                self.recent_sale(user_id, msg[1])


            elif msg[0] == 'talk_pay':
                data_length, talk_pay_fetchall = self.talk_pay(msg)
                sendMsg_dataLen = [msg[0], data_length]
                self.sendPersonalMsg(user_id, sendMsg_dataLen)

                sendMsg = talk_pay_fetchall
                self.sendPersonalMsg(user_id, sendMsg)
                return

            elif msg[0] == "load_Inform":
                inform_list = self.load_Inform(user_id, msg)
                sendMsg = ["load_Inform", inform_list]
                self.sendPersonalMsg(user_id, sendMsg)
                return

            elif msg[0] == "editInform":
                res = self.update_inform(user_id, msg)
                sendMsg = [msg[0], res]
                self.sendPersonalMsg(user_id, sendMsg)

            elif msg[0] == "loadSale":
                res, msg = self.loadSale(user_id)
                print(res, msg)
                sendMsg = ["loadSale", msg, res]
                self.sendPersonalMsg(user_id, sendMsg)

            elif msg[0] == "loadStoreName":
                self.sendPersonalMsg(user_id, [msg[0], user_id])

            elif msg[0] == "update_userRecentCategory":
                self.update_userRecentCategory(user_id, msg[1])

            elif msg[0] == "loadRecentCategory":
                print(msg, "최근 카테고리")
                data_length, category_list = self.loadRecentCategory(user_id)
                sendMsg_dataLen = [msg[0], data_length]
                self.sendPersonalMsg(user_id, sendMsg_dataLen)

                sendMsg = category_list
                self.sendPersonalMsg(user_id, sendMsg)

            elif msg[0] == "change_productSale":
                self.change_productSale(msg[1], msg[2])

            elif msg[0] == "refreshMyFeed":
                print("피드 불러오기 시작")
                data_len, s_list = self.refreshMyFeed(msg[1])
                sendMsg_dataLen = [msg[0], data_len]
                self.sendPersonalMsg(user_id, sendMsg_dataLen)

                self.sendPersonalMsg(user_id, s_list)

            elif msg[0] == "refreshMySellList":
                print("판매내역 불러오기 시작")
                data_len, s_list = self.refreshMySellList(msg[1])
                sendMsg_dataLen = [msg[0], data_len]
                self.sendPersonalMsg(user_id, sendMsg_dataLen)

                self.sendPersonalMsg(user_id, s_list)


            else:
                return -1

        except Exception as e:
            print(e)

    def sendPersonalMsg(self, user_id, msg):
        self.users[user_id][0].send(pickle.dumps(msg))


class MyTcpHandler(socketserver.BaseRequestHandler):
    userman = UserManager()
    print("서버 오픈")
    def handle(self):
        user_id = ""
        print(self,"self memory")
        print('client [%s] 연결' % self.client_address[0])
        while True:
            try:
                msg = pickle.loads(self.request.recv(1024))
                print(msg, "---------------------- 메시지")

                if msg[0] == "logIn":
                    user_id = self.loginUser(self, msg)
                    # pass

                elif msg[0] == "signUp":
                    print("회원가입 들어감")
                    ret = self.registUser(self, msg)
                    sendMsg = [msg[0], f"{ret}"]
                    self.request.send(pickle.dumps(sendMsg))

                elif msg[0] == "id_check":
                    print("중복체크 시작")
                    ret = self.overlab_check(self, msg)
                    sendMsg = [msg[0], f"{ret}"]
                    self.request.send(pickle.dumps(sendMsg))

                elif msg[0] == "id_find":
                    print("아이디 찾기 시작")
                    sendMsg = self.findId(self, msg)
                    self.request.send(pickle.dumps(sendMsg))

                elif msg[0] == "pw_find":
                    print("비밀번호 찾기 시작")
                    sendMsg = self.findPw(self, msg)
                    self.request.send(pickle.dumps(sendMsg))

                elif msg[0] == "pw_reset":
                    print("비밀번호 재설정")
                    sendMsg = self.resetPw(self, msg)
                    self.request.send(pickle.dumps(sendMsg))

                    recvMsg = pickle.loads(self.request.recv(1024))
                    sendMsg2 = self.updatePw(self, recvMsg)
                    self.request.send(pickle.dumps(sendMsg2))

                if user_id:
                    print(user_id, ":user_id")
                    print(self.request)
                    print(self.client_address)
                    print(self.server)
                    self.chat_latest = 0

                    self.userman.addUser(user_id, self.request, self.client_address)
                    print(user_id, "로그인 완료")
                    while 1:
                        print("여기 반복")
                        try:
                            msg = pickle.loads(self.request.recv(300000))
                            if msg[0] == "registProduct":
                                data_len = msg[1]
                                msg = b''
                                while data_len > len(msg):
                                    msg += self.request.recv(8192)
                                msg = pickle.loads(msg)

                            sendMsg = self.userman.messageHandler(user_id, msg)

                            if sendMsg == -1:
                                self.request.close()
                                break
                        except Exception as ex:
                            print(ex)
                            break

            except Exception as e:
                print(e)
                break
        print('[%s]종료' % self.client_address[0])
        self.userman.removeUser(user_id)


    def loginUser(self, dummy, list):
        user_list = []
        cur.execute("SELECT id FROM user;")
        for i in cur:
            user_list.append(i[0])
        try:
            user_id = list[1]
            input_pw = list[2]
            sql = f"SELECT password FROM user WHERE id='{user_id}';"
            cur.execute(sql)
            user_pw = cur.fetchone()[0]
        except Exception as ex:
            send_msg = ["logIn", ""]
            encoded_msg = pickle.dumps(send_msg)
            self.request.send(encoded_msg)
            return ""

        if input_pw == user_pw:
            send_msg = ["logIn", "1"]
            encoded_msg = pickle.dumps(send_msg)
            self.request.send(encoded_msg)
            return user_id
        else:
            send_msg = ["logIn", ""]
            encoded_msg = pickle.dumps(send_msg)
            self.request.send(encoded_msg)
            return ""

    def registUser(self, dummy, list):
        try:
            sql = f"INSERT INTO user VALUES({list[1]});"
            cur.execute(sql)
            con.commit()
            print("회원가입 성공")
            return 1
        except:
            print("회원가입 실패")
            return ""

    def overlab_check(self, dummy, msg):
        try:
            sql = f"SELECT id FROM user WHERE id LIKE '{msg[1]}';"
            if cur.execute(sql):
                print("이미 있는 아이디")
                ret = 1
            else:
                print("생성 가능")
                ret = ""
        except:
            ret = 1
        return ret

    def findId(self, dummy, msg):
        sendMsg = ["id_find"]
        try:
            sql = f"SELECT id FROM user WHERE name='{msg[1]}' AND birth='{msg[2]}';"
            cur.execute(sql)
            sendMsg.append(cur.fetchall()[0][0])
        except Exception as ex:
            print(ex)
            sendMsg.append("")
        return sendMsg

    def findPw(self, dummy, msg):
        sendMsg = ["pw_find"]
        try:
            sql = f"SELECT password FROM user WHERE id = '{msg[1]}' AND name = '{msg[2]}' AND birth = '{msg[3]}';"
            cur.execute(sql)
            sendMsg.append(cur.fetchall()[0][0])
        except Exception as ex:
            print(ex)
            sendMsg.append("")
        print(sendMsg)
        return sendMsg

    def resetPw(self, dummy, msg):
        sendMsg = ["pw_reset"]
        try:
            sql = f"SELECT password FROM user WHERE id = '{msg[1]}' AND name = '{msg[2]}';"
            cur.execute(sql)
            sendMsg.append(cur.fetchall()[0][0])
        except Exception as ex:
            sendMsg.append("")
            print(ex)
        print(sendMsg)
        return sendMsg

    def updatePw(self, dummy, msg):
        sendMsg = ["update_pw"]
        if msg[0] == "update_pw":
            try:
                sql = f"UPDATE user SET password = '{msg[1]}' WHERE id = '{msg[2]}';"
                cur.execute(sql)
                con.commit()
                sendMsg.append("success")
            except Exception as ex:
                print(ex)
                sendMsg.append("")

        print(sendMsg)
        return sendMsg




class ChatingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
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

