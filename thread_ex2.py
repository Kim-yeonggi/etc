import schedule
import time

job1 = 0
job2 = 0
count = 0

def message1():
    print("스케쥴 실행 중")

def message2(text):
    print(text)

def top():
    schedule.cancel_job(job1)

def start():
    global job1
    global job2
    global count
    job1=schedule.every(1).seconds.do(message1)         # 1초주기로 message1 실행
    job2=schedule.every(3).seconds.do(message2, "3초 추가")
    while 1:
        schedule.run_pending()
        time.sleep(1)
        count = count+1
start()

