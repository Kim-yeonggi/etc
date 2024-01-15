# # 240115
# # 예외처리
# # 구문오류
#
# # index
# # value
# # type
# # syntax
#
# # => 프로세스 강제 중지
# while 1:
#     try:    # 실행하고자 하는 코드
#         x = input("1~9 숫자를 입력하세요")
#         stra = "123456789"
#         print(stra.index(x))
#         print(stra.index(x))
#         print(stra.index(x))
#         print(stra.index(x))
#         print(stra.index(x))
#         print(stra.index(x))
#         print(stra.index(x))
#         print(stra.index(x))
#         print(stra.index(x))
#         print(stra.index(x))
#     except: # 예외일 때 실행할 코드
#         print("error")
# # find : 찾는 문자가 없으면 -1 리턴
# # index : 찾는 문자가 없으면 오류 발생
#
# # if : 특정 상황에 대해서만 예외 처리 -> 모든 에러를 예측해야함
# # try : 모든 상황 예외처리 가능
import os
# # p.368
# list_input_a = ['52', '273', '32', 'spy', '103']
# list_number = []
# for item in list_input_a:
#     try:
#         float(item)
#         list_number.append(item)
#     except:
#         pass
# print("{} 내부에 있는 숫자는".format(list_input_a))
# print("{}입니다.".format(list_number))


# # try except else
# # try : 시도 실행
# # except : 예외 발생 코드
# # esle : 예외없이 실행 되었을 때 == try 의 모든 코드가 정상 실행 됐을 때
#
# try:
#     x = int(input('숫자 입력'))
#     x = int(input('숫자 입력'))
#     x = int(input('숫자 입력'))
#     x = int(input('숫자 입력'))
# except:
#     print("오류 발생o")
# else:
#     print('오류 발생 x')


# # finally
# # finall : 예외처리 구문에서 가장 마지막에 사용하는 구문
# # 예외 발생이 있든 없든 무조건 실행
#
# try:
#     x = int(input("num input"))
# except:
#     print("예외 발생")
# else:
#     print("정상실행")
# finally:
#     print("항상 실행하는 코드")

# # p.371
# try:
#     number_input_a = int(input("정수 입력 : "))
#     print("원의 반지름: ", number_input_a)
#     print("원의 둘레: ", number_input_a * 2 * 3.14)
#     print("원의 넓이: ", 3.14 * number_input_a**2)
# except:
#     print("정수를 입력하지 않았습니다.")
# else:
#     print("예외가 발생하지 않았습니다.")
# finally:
#     print("일단 프로그램이 어떻게든 끝났습니다.")



# # 1. try + excecpt
# # 2. try + fianlly
# # 3. try + except + finally
# # 4. try + except + else + finally
# # 5. try + except + else
#
#
# # p.373
# try:
#     file = open("info24fdasfa.txt", 'r')
#     # 오류 발생
# except Exception as e:
#     print("오류 발생")
#     print(e)
# else:
#     file.close()
#
#     print("# 파일이 제대로 닫혔는지 확인하기")
#     print('file.closed:', file.closed)


# # p.376
# def test():
#     print('test() 함수의 첫 줄입니다.')
#     try:    # 일단 실행
#         file = open("info240115.txt", 'w')
#         print('try 구문이 실행되었습니다.')
#         return
#         print('try 구문의 return 키워드 뒤입니다.')
#     except: # try 에서 오류 발생시 실행
#         print('except 구문이 실행되었습니다.')
#     else:   # try 에서 오류 발생 안하면 실행
#         print('else 구문이 실행되었습니다.')
#     finally:    # 마지막에 무조건 실행
#         print('finally 구문이 실행되었습니다.')       # retrun 을 만나도 finally 구문까지 실행 후 return 실행
#         file.close()
#     print('test() 함수의 마지막 줄입니다.')
# test()
#
# # 함수 내부에 try finally 있으면 try 도중 return 해도 finally 실행 후 탈출한다.'
# # 반복문의 break 경우에도 마찬가지로 finally 구문 실행 후 반복문 탈출한다

# # p.378
# while True:
#     try:
#         print("try")
#         break
#         print('try 2')
#     except:
#         print('except')
#     finally:
#         print('fianlly')
#
#     print('while 마지막')
# print('프로그램 종료/ 반복문 탈출')


# # p.379-381
# # 2.
# numbers = [52, 273, 32, 103, 90, 10, 275]
# print('# (1) 요소 내부에 있는 값 찾기')
# print('- {}는 {} 위치에 있습니다.'.format(52, numbers.index(52)))
# print()
#
# print('# (2) 요소 내부에 없는 값 찾기')
# number = 10000
# try:
#     print('- {}는 {} 위치에 있습니다.'.format(number, numbers.index(number)))
# except:
#     print('- 리스트 내부에 없는 값입니다.')
# print()
# print('--- 정상적으로 종료되었습니다. ---')



# # 예외 객체 exception object
# # 예외개체는 예외 정보를 담고 있다.
# # 모든 종류의 예외정보를 담고 있는 Exception 예외 객체를 보통 사용
# # Exception은 클래스
#
# list_number = [52, 273, 32, 72, 100]
# try:
#     number_input = int(input('숫자입력'))
#     print('{}번째 요소 : {}'.format(number_input, list_number[number_input]))
# # except Exception as e:        # 모든 에러 포함
# #     print("type(exception) :", type(e))
# #     print('exception :', e)
# except IndexError as e:
#     print('인덱스 범위 오류 :', e)
# except ValueError as e:
#     print('Value 오류 :', e)
# except Exception as e:
#     print(e)


# # raise 구문
# number = input("정수 입력")
# number = int(number)
# if number > 0:
#     raise NotImplementedError
# else:
#     raise NotImplementedError
#
# # raise : 강제 에러 발생
# # 작성법 : raise 예외 객체



# # 표준 모듈 : 내장        ex) datetime, random
# # 외부 모듈 : 다운로드 설치
#
# # package(      module(     class       (   function()  )       )        )
# # 표준 모듈 1. math
# import math, datetime
#
# print(math.floor(2.5))  # 내림
# print(math.ceil(2.5))   # 올림
#
# print(round(3.3))   # 내장함수 round

# # from 방식으로 모듈 호출 -> 모듈명. 생략 가능 (math.)
# from math import sin,cos,tan,floor,ceil
# print(floor(1.75))
#
# # from math import *    # math 모듈에 내장된 모든것 불러오기
#
# import math as m
# print(m.floor(1.75))


# # p.407
# import random
# print("# random 모듈")
#
# print('- random:', random.random())
# print("- uniform(10, 20):", random.uniform(10, 20))
#
# print('- randrange(10):', random.randrange(10))
# print('- randrange(10,20):', random.randrange(10,20))
#
# print('- choice([1, 2, 3, 4, 5]):',random.choice([1, 2, 3, 4, 5]))
# print('- shuffle([1, 2, 3, 4, 5]):',random.shuffle([1, 2, 3, 4, 5]))
# print('- sample([1, 2, 3, 4, 5], k=2):',random.sample([1, 2, 3, 4, 5], k=2))
#
# # random
# # random() : 0.0 <= ~ < 사이 float
# # uniform(n, m) : n~m 사이 균등 분포 값   float
# # randrange(n) : 0 ~ n 사이 값 리턴      int
# # randrange(n, m) : n ~ m 사이 값 리턴   int
# # choice([list]) : 리스트에서 랜덤 1개 선택
# # shuffle([list]) : 리스트 순서 섞기
# # sample([list], k = n) : list에서 랜덤으로 n개 요소 뽑기

# import random
# sum1 = 0
# sum2 = 0
# n = int(input("몇 번 반복 : "))
# for i in range(n):
#     uni = random.uniform(0,10)
#     ran = random.random()
#     sum1 += uni
#     sum2 += ran
# print(sum1/n)
# print(sum2/n)


# # p.408-9 : system 모듈
# import sys
# print(sys.argv)
# print('---')
#
# print('getwindowsversion:()', sys.getwindowsversion())
# print('---')
# print('copyright:', sys.copyright)
# print('---')
# print('version:', sys.version)
#
# sys.exit()      # process 강제 종료
# print(sys.argv)


# # p.410 : os 모듈
# from os import *
# print('현재 운영체제:', name)
# print('현재 폴더:', getcwd())
# print('현재 폴더 내부의 요소:', listdir())
#
# # mkdir("hello")
# # rmdir('hello')
# #
# # with open("original.txt", "w") as file:
# #     file.write('hello')
# # # rename('original.txt', 'new.txt')
# #
# # # remove('new.txt')
# #
# # system('dir')
#
# baseDir = os.getcwd()
# for idx, i in enumerate(os.listdir()):
#     print(i)
#     if "2023.txt" == i:
#         print("find", idx)
#         break


# # p.412
# import datetime
# print("# 현재 시각 출력하기")
# now = datetime.datetime.now()
# print(now.year, "년")
# print(now.month, "월")
# print(now.day, "일")
# print(now.hour, "시")
# print(now.minute, "분")
# print(now.second, "초")
# print()
#
# print("# 시간을 포맷에 맞춰 출력하기")
# output_a = now.strftime("%Y.%m.%d.%H.%M.%S")
# output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, \
#                                             now.month,\
#                                             now.day,\
#                                             now.hour,\
#                                             now.minute,\
#                                             now.second)
# output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}".format(*"년월일시분초"))
# # format(*"012345") 요소 하나하나가 매개변수로 지정
# print(output_a)
# print(output_b)
# print(output_c)



# import time
# print("3초 카운트 시작지점")
# time.sleep(3)
# print("3초 후 출력")


# from urllib import request
# # target = request.urlopen("https://naver.com")
# target = request.urlopen("https://ssl.pstatic.net/melona/libs/1482/1482220/c50a5041dd4e4f438fd4_20240105150550034.png")
# output = target.read()
# print(output)
#
# file = open('output.png', 'wb')
# file.write(output)
# file.close()

# b' 데이터~~~~~~~~~~~
# 바이너리 데이터
# 텍스트 데이터 100
# 텍스트 100이라는 숫자는 1,0,0으로 구성
# 텍스트 데이터 100은 49 48 48










