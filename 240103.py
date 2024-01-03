# # syntax error : 문법 오류
# # type error : 데이터 형태 맞지 않음 ex)문자 + 숫자
# # index error : index of out of range ex) "0123"[5]
# # value error : 변환 불가능한 값을 변환 시도했을 경우
# #               ex) 숫자/문자가 아닌 값을 숫자/문자로 변환
# #                   소수점이 있는 숫자/문자열을 int로 변환
#
# print(int(input("입력:")))
#
# x=input()
# print(x.isdigit())     # .isdigit() : 숫자인지 판별
#
# # p.125 ex inch -> cm
# raw_input = input("inch 단위의 숫자를 입력해주세요: ")
#
# # 입력받은 데이터를 숫자 자료형을 변경하고, cm 단위로 변경
# inch = int(raw_input)
# cm = inch * 2.54
#
# #출력
# print(inch, "inch는 cm 단위로", cm, "입니다.")
#
# # p.133 스왑
# a = input("a")
# b = input("b")
#
# print(a, b)
# # (a, b) = (b, a)       # 튜플
# a += b
# b = a[0:5]
# a = a[5:]
# print(a, b)


# # ch 2-4 : 숫자와 문자열의 다양한 기능
# print("hello".isupper())    # 문자열이 소문자인지 판별
#
# # format : 문자열의 {}내부에 format 함수의 매개변수를 대입
# x=1
# y=2
# print("{}".format(x))
# print("x={}, y={}, x+y={}, x*y={}".format(x,y,x+y,x*y))
#
# # p.136
# # format() 함수로 숫자 -> 문자열 변환
# format_a = "{}만 원".format(5000)
# format_b = "파이썬열공하여 첫 연봉 {}만 원 만들기".format(5000)
# format_c = "{} {} {}".format(3000, 4000, 5000)
# format_d = "{} {} {}".format(1, "문자열", True)
#
# # 출력
# print(format_a)
# print(format_b)
# print(format_c)
# print(format_d)
#
#
#
# # :.nf -> 소수점 n번째 자리까지만 출력
# print("{:.2f}".format(15.1234))
#
# a = "AAAA bbbb CCcc DdDD"
# print(a.lower())    # 소문자로 변환하여 출력 / 원본 변환 x
# print(a)
# b = a.lower()
# print(b)
# print(b.upper())    # 대문자로 변환
# # => 원본 변환하지 않는 함수 : 비파괴 함수

# # 문자열 관련 함수
# # 1. lower()    # 소문자로 변환
# # 2. upper()    # 대문자로 변환
# # 3. strip()    # 공백 제거         // """ """ 엔 적용 X
# # 4. lstrip()   # 좌측 공백 제거
# # 5. rstrip()   # 우측 공백 제거
#
# print("   111   ".strip())

# # isalnum()     # 알파벳과 문자인지
# # isalpha()     # 알파벳인지
# # isdigit()     # 슷자인지
# # isspace()     # 공백(space) 인지    ex) " ".isspace() -> True

# # find() : 문자열 내부의 특정 문자(매개변수)의 위치 인덱스
# print("안녕하세요".find("하세"))

# # 문자열과 in 연산자
# print("hell" in "hello")
# # in 키워드로 문자열 내부에 특정 문자열 존재 여부 확인

# # split() 문자열 분리
# a="1 2 3 4 5 6 7".split(" ")    # .split("구분할 문자") -> list 형태로 출력
# print(a)

# # f문자열
# x=10
# print(f"{x}")  # == "{}".format(x)

# # p.152 도전문제
# # 1. 구의 부피와 겉넓이
# r = int(input("구의 반지름을 입력해주세요: "))
# pi = 3.141592
# a1 = 4 / 3 * pi * r**3
# a2 = 4 * pi * r**2
# print(f"= 구의 부피는 {a1}입니다.")
# print(f"= 구의 겉넓이는 {a2}입니다.")

# # 2. 피타고라스의 정리
# a = float(input("밑변의 길이를 입력해주세요: "))
# b = float(input("높이의 길이를 입력해주세요: "))
# c = (a**2 + b**2)**0.5
# print(f"빗변의 길이는 {c}입니다.")

# a = "hello"
# # count()
# print(a.count('l'))     # 특정 문자 'l'의 개수 반환
#
# # index()
# print(a.index('l'))   # 특정 문자(매개변수)의 위치 찾기 / 여러 개일 경우 첫번째 문자 인덱스만 반환
# # 문자열에서 위치 찾는 함수 : find(), index()
# # 찾고자 하는 문자열 없을시 : find() -> -1 반환 / index() -> error
#
# # replace(a, b) : 문자열에서 a를 b로 변경(대체)
# print(a.replace('l', '1'))  # 여러 개일 경우 모두 변경


# # Ch03 : 조건문
#
# # bool type
# # bool 자료형 : True 혹은 False 를 나타내는 자료형 / 참 거짓 식별
# # 보통 조건식, 함수의 결과값(return)으로 나옴
# print(1==1)
# " ", "111"  # True
# [1, 2, 3]   # True
# 1           # True
#
# ""      # False
# []      # False
# 0       # False
#
# # 비교 연산자
# # ==    같다
# # >     우측이 크다
# # >=    우측이 크거나 같다
# # <     우측이 작다
# # <=    우측이 작거나 같다
# # !=    다르다

# # 리스트(list) 데이터
# # [1, 2, 3, 'a', 'b']
# # 여러 요소의 데이터를 하나로 묶어 하나의 데이터로 처리하는 데이터 형태
# # 대활호 [] 로 생성, 각 요소는 쉼표로 구분
# a = []                      # 빈리스트
# b = [1]                     # 숫자 요소 1개 리스트
# c = [1, 2, 3]               # 숫자 여러 개 리스트
# d = [1, 'a']                # 숫자, 문자 혼합 리스트
# e = [1, []]                 # 2중첩 리스트
# f = [1, 2, [3, [4, ['a']]]] # 4중첩 리스트

# # 빈 리스트 생성 방법
# a = []      # 1. 대활호로 생성
# a = list()    # 2. list 함수로 생성
#
# # 리스트 인덱싱
# a = [1, 2, 3]
# print(a[0])
# a[0] = 100
# print(a)

# s = "abcde"
# print(s[0])
# # s[0] = 'm'  # TypeError
# s = s.replace('a', 'm')
# print(s)

# a = [1,2,3,[4,[5,6,7],8,9]]     # 2중 리스트
# print(a[3][1][-1])          # 7

# # 리스트 슬라이싱
# a=[0,1,2,3,4,5,6]
# print(a[3:6])

# # 리스트 연산
# a = [0,1,2]
# b = [3,4,5,]
# print(a+b)      # [0, 1, 2, 3, 4, 5]
# print(a*3)      # [0, 1, 2, 0, 1, 2]

# a=[0,1,2,3,4,5]
# print(len(a))       # 6

# # del 키워드 : 리스트 요소 삭제
# a = [0,1,2,3]
# del a[2]
# print(a)

# b = [0,1,2,3,4,5,6]
# del b[1:4]
# print(b)

# # 리스트 관련 함수
# # append() : 리스트의 마지막 위치에 요소 추가
# a = [0,1,2,3]
# a.append(['a', 'b', 'c'])
# print(a)

# # sort() 리스트 정렬 함수
# a = [10,5,2,4]
# a.sort()
# print(a)

# # reverse() : 리스트 뒤집는 함수
# a = ['a', 'ab', 'c', 'b']
# a.sort()
# a.reverse()
# print(a)

# # index() : 리스트 요소 찾기 함수
# a = [0,1,2]
# print(a.index(1))
# print(a.index(100))   # 리스트에 없는 값 -> Value Error

# # append()는 마지막 요소에 추가하는 방식
# # insert()는 지정 위치에 추가(삽입)하는 방식
# # insert(위치, 넣을 값)
# a = [0,1,3,4]
# a.insert(2, 2)
# print(a)

# # remove() 함수 : 리스트 요소 제거
# a = [0,1,2,3,3,3,3,3,3,3,4,5]
# a.remove(3)
# print(a)        # 처음 값만 제거

# # pop() 마지막 요소 꺼내기
# a = [0,1,2]
# print(a.pop())
# print(a)
#
# # count() : 특정 요소 개수 카운트
# a = [1,2,3,3,3,4,5]
# print(a.count(3))

# # extend() : 리스트 더하기
# a = [1,2,3]
# a.extend([4,5])         # ==  a += [4,5]
# print(a)

# # 문자열이 join 함수 : 구분자 텍스트.join('문자열')
# res = 'aaa'.join('bbb')
# print(res)
# res = ' '.join(res)
# print(res)


# # 딕셔너리 데이터 형태   * json 파일과 1대1 매칭 O
# # { }로 선언
# # 딕셔너리는 key:value의 쌍을 구성된 데이터
# # {key:value, key2:value2, key3:value3} -> 3개의 key:value 쌍

# d = {'name':'a', 'age':20, 'loc':[0, 1, 2, 3, 4]}
# print(d, type(d))

# # 딕셔너리는 []에 key 사용 (not index)
# # 딕셔너리 쌍 추가 삭제
# # 쌍 추가          a[추가 key] = 추가 value
# a = {1:'a'}
# a[2] = 'b'
# print(a)
# print(a[1])
#
# a[1] = 100
# print(a)
#
# # 쌍 제거
# del a[1]
# print(a)
#
# # 딕셔너리 생성시 주의사항
# # 딕셔너리의 key는 고유한 값 -> 중복 시 하나를 제외한 나머지 동일한 key의 value 모두 무시
# # => 동일한 key 여러 개 존재하지 않도록 생성

# # 불변값 : immutable : int / float / tuple
# # 가변값 : mutable : list / set / dictionary
# # dictionary의 key는 고유해야하고, 변하지 않는 값(immutable)을 쓴다.
# # => dictionary의 key에 list는 불가능 / value는 어떤 값이든 가능
#
# # 딕셔너리 관련 함수
# # key()
# d = {'name':'a', 'age':1, 'loc':[12, 1432, 0.1246]}
#
# # dictionary에 .key() 함수를 호출하면 dict_keys 객체를 리턴(반환)한다.
# print(type(d.keys()))           # <class 'dict_keys'>
#
# # dict_keys 는 list() 함수를 사용하여 list로 변환 가능하다.
# # print(d.keys()[0])            # 에러
# keyList = list(d.keys())        # dict_keys 객체 -> list 로 변환
# print(keyList)                  # name      ->  list로 변환 후 list index 사용 가능
# print(d[keyList[0]])     # a
#
# # values() 함수 : keys 함수는 key 객체, values() 함수는 values 객체 리턴
# print(d.values())
# valueList = list(d.values())    # dict_values 객체 -> list 로 변환
# print(valueList[0])
#
# # items() 함수 : key, value 를 쌍으로 얻음
# print(d.items())        # item()함수는 dict_items 객체를 리턴
# itemsList = list(d.items())
# print(itemsList[0])     # itemList의 0번째 인덱스는 튜플 형태의 (key, value) 데이터
#
# # clear() 함수 : dictionary 초기화(모든 내용 삭제)
# d.clear()
# print(d)


# x = {'a':1, 'b':'100', 'c':'abc'}
# print(x.get('a'))
# print(x.['a'])
# # get(x) 함수는 x라는 key에 대응하는 value를 얻을 수 있다.
# # x['a']에서 a키가 없을 때 오류 발생
# # get('a')에서 a가 딕셔너리 내에 없으면 None 리턴
#
# print('안녕' in '안녕하세요')
# print(3 in [1,2,3])
# print('a' in x)

# # tuple 자료형
# # 튜플은 리스트와 비슷하지만 차이점 존재
# # 튜플은 (,) 형태로 선언
# # 리스트는 요소 값 견경 가능 / 튜플은 변경 불가능(조회(호출)만 가능)  -> 값 추가, 삭제 불가능 ex) append, del
# t = ()          # 빈 튜플
# t = (1,)        # 요소 하나일 때 쉼표 삽입
# t = (1,2,3)
# t = (1,2,(3,4))
# tt = 1,2,3,4,5,"aaa"  # 여러 요소 쉼표로 구분 -> 자동을 튜플 처리
# print(type(tt))
# print(tt)
#
# print(tt[0])
# print(tt[:])
# print(len(tt))


# # set 집합 자료형
# s = set([1,2,3])
# print(s)
#
# s = set('hello')
# print(s)        # 출력 순서 랜덤
# # 중복 허용 X
# # unordered : 순서 없음 -> 랜덤 순서 출력 ex) l o h e / 인덱스 사용 불가
# print(list(s)[1])   # 리스트로 형변환 후 인덱스 사용 가능 but 순서 X

# # 교집합 / 합집합 / 차집합
# s1 = set([1,2,3,4,5,6])
# s2 = set([7,8,9,10,5,6])
#
# print(s1 & s2)                  # 교집합
# print(s1.intersection(s2))      # 교집합 함수
#
# print(s1 | s2)          # 합집합
# print(s1.union(s2))     # 합집합 함수
#
# print(s2-s1)              # 차집합
# print(s2.difference(s1))    # 차집합 함수
#
# # 집합에 값 추가 : add 함수
# s1.add(100)
# print(s1)

# # 집합에 값 제거 : remove 함수
# s1.remove(100)
# print(s1)


# # and 연산자 : 모두 참일 때 참
# # or 연산자 : 하나만 참이어도 참
# # not 연산자 : 참이면 거짓, 거짓이면 참 -> 결과 반대

# print('가방' < '하마')      # True
# x = 50
# print(10<x<100)

# print(not True)     # False
# x=10
# under20 = x<20
# print(under20)      # True
#
# print(x<20 and x<100)   # True
# print(x<20 or x<5)      # True
# print(x<20 and x<5)     # False

# # if 조건문 : 상황을 나누어 실행 여부 결정

# # if 조건식:
# #     수행문
# #     수행문
# #     수행문

# x=100
# if x>50:
#     print(x)
#     # 들여쓰기

# # p.164 조건문 기본 사용 / 양수 음수
# number = int(input("정수 입력>"))
#
# if number > 0:
#     print("양수입니다.")
#
# if number < 0:
#     print("음수입니다.")
#
# if number == 0:
#     print("0입니다.")

# # if문 구조
'''
if 조건식:
    조건식이 참일 때 실행할 문장 - 1
    조건식이 참일 때 실행할 문장 - 2
    조건식이 참일 때 실행할 문장 - 3
else:
    조건식이 거짓일 때 실행할 문장 - 1
    조건식이 거짓일 때 실행할 문장 - 2
    조건식이 거짓일 때 실행할 문장 - 3
'''

# # # p.165, 166 날짜/ 시간
# import datetime as dt
# now = dt.datetime.now()
# # print(now)
# # print(type(now))
# #
# # print(now.year, "년")
# # print(now.month, "월")
# # print(now.day, "일")
# # print(now.hour, "시")
# # print(now.minute, "분")
# # print(now.second, "초")
#
# print("{}년 {}월 {}일 {}시 {}분 {}초".format(
#     now.year,
#     now.month,
#     now.day,
#     now.hour,
#     now.minute,
#     now.second)
# )

# # p.167 오전 오후 구분
# import datetime as dt
# now = dt.datetime.now()
#
# if now.hour < 12:
#     print(f"현재 시각은 {now.hour}시로 오전입니다.")
# else:
#     print(f"현재 시각은 {now.hour}시로 오후입니다.")

# # 성적 나누기
# user_input = input("성적 입력: ")
#
# if user_input.isdigit():
#     user_input = int(user_input)
#     if user_input < 60:
#         print("F")
#     elif user_input < 70:
#         print("D")
#     elif user_input < 80:
#         print("C")
#     elif user_input < 90:
#         print("B")
#     else:
#         print("A")

# # p. 169 문장 끝에 \ 붙이면 다음 줄도 한 줄로 인식
# last_number = int(input("정수 입력"))
# if last_number == 0 \
#     or last_number == 2 \
#     or last_number == 4 \
#     or last_number == 6 \
#     or last_number == 8:
#     print("짝수")
# else:
#     print("홀수")

# # p.170 짝 홀 구분 2
# number = int(input("정수 입력 : "))
# last_char = str(number)[-1]
#
# if last_char in "02468":
#     print("짝수입니다")
# else:
#     print("홀수입니다")

# # if : 무조건 처음, 하나만 가능
# # elif : 여러 개 가능, 두번째부터 사용 가능, 생략 가능
# # else: 생략 가능, 하나만 가능

# number = int(input("정수입력: "))
#
# if number%2 == 0:
#     print("짝수")
# else:
#     print("홀수")

# # p.178 계절 구하기
# import datetime
# now = datetime.datetime.now()
# month = now.month
# print(month)
# if 3 <= month <= 5:
#     print("봄")
# elif 6 <= month <= 8:
#     print("여름")
# elif 9 <= month <= 11:
#     print("가을")
# else:
#     print("겨울")


# # ex)
# # datetime을 이용해서 요일을 조회 -> 평일이면 등원, 주말이면 등원 X
# # 사용자가 가진 돈 입력
# # 택시 요금은 5000원
# # 사용자가 날씨가 맑음 or 비 중 하나를 입력
# # 날씨가 비가오면 택시를 타고 맑으면 걷는다.
# import datetime
# weekday = datetime.datetime.today().weekday()     # 0(월) ~ 6(일)
# '''
# if weekday < 5:     # 평일
#     money = int(input("현재 가진 돈 입력: "))
#     weather = input("현재 날씨 입력(맑음 / 비): ")
#
#     if money >= 5000:   # 5000원 이상 -> 택시 가능
#         if weather == '비':
#             print("택시를 타고 등원한다.")
#         else:
#             print("걸어서 등원한다.")
#     else:
#         print("걸어서 등원한다.")
# else:       # 주말
#     print("집에 있는다.")
# '''
#
# week = '월화수목금토일'
# print(f"오늘 요일: {week[weekday]}")
#
# if weekday < 5:     # 평일
#     weather = input("현재 날씨 입력(맑음 / 비): ")
#
#     if weather == "비":
#         money = int(input("현재 가진 돈 입력: "))
#         if money >= 5000:
#             print("택시를 타고 등원한다.")
#         else:
#             pass
#
#     print("걸어서 등원한다.")
# else:       # 주말
#     print("집에 있는다.")

# p. 188
# 1. 대화 프로그램
import datetime
input_str = input("입력: ")
if "안녕" in input_str:
    print("안녕하세요.")
elif "몇 시" in input_str:
    print("현재 시각은 {}시 입니다.".format(datetime.datetime.now().hour))
else:
    print(input_str)
