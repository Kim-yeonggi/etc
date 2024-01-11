# #240111
#
# # 튜플
# # 괄호가 없는 튜플
# # 1. 만들었을 때
# # 2. return 으로 반환 받는 형태로 튜플 많이 사용
#
# tp = 10,20,30,40
# print(tp)
#
# a,b = 10,20
# print(a)
# print(b)
# a,b=b,a
# print(a)
# print(b)


# # 람다 lambda 표현
# # 함수의 표현법 중 하나
#
# def xxxx():         # 사용자 함수 정의
#     print("xxxx함수가 호출")
#
# # 일반 함수 : 호출 부분 따로 존재
# xxxx()

# # p.322
# def call_10_times(func):
#     for i in range(10):
#         func()
#
# def print_hello():
#     print('hello')
#
# # print(print_hello)
# # print(id(print_hello))
# # 함수 선언하면 실제 메모리에 할당 -> 식별자(print_hello)를 통해 호출함
# call_10_times(print_hello)
# # 콜백 함수 : 함수의 매개변수에 사용되는 함수
# # 콜백함수 : 함수() 가 아니라 함수의 명(식별자) 전달

#
# def play(func):
#     for i in range(10):
#         func()
# def a():
#     print('a')
# def b():
#     print("b")
# def c():
#     print('c')
# play(a)     # 매개변수로 전달하는 함수를 식별자처럼 사용
#

# # filter 함수
# # map 함수
# # 함수를 매개변수로 사용하는 대표적인 함수들
# # map(함수명, 리스트) : 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트 구성
#
# # filter(함수명,리스트) : 리스트의 요소를 함수에 넣고 리턴된 값이 True인 것으로 새로운 리스트 구성
#
# # p.323,4
# def power(item):
#     return item * item
# def under_3(item):
#     return item < 3
#
# list_input_a = [0,1,2,3,4,5]
#
# output_a = map(power, list_input_a)
# print('# map() gkatndml 실행결과')
# print('map(power, list_input_a):', output_a)
# print('map(power, list_input_a:', list(output_a))
# print()
#
# output_b = filter(under_3, list_input_a)
# print('# filter() 함수의 실행 결과')
# print('filter(under_3, list_input_a):', output_b)
# print('filter(under_3, list_input_a):', list(output_b))
#
# print(list(filter(power, list_input_a)))

# # filter object 와 map object는 제너레이터 라고 한다.
# # 메모리 절약을 위해서 제너레이터 object형태로 반환이 온다.
# # 제너레이터 내부 값을 조회하려면 list로 형 변환
# #


# # 일반 함수(사용자 정의 def)
# # 재귀 함수 :
# #   1. 탈추 조건이 있어야 함
# #   2. 문제 해결 방법이 동일
#
# # 콜백 함수 :
# #   1. 매개변수를 통해서 전달되는 함수
#
#
# # 람다 : 코드 중간에 정의와 호출을 하는 방법
# # def를 사용하지 않는다. == 정의 단계가 없다.
# # 함수를 간단하게 선언하는 방법
#
# under_3 = lambda x: x < 3
#
# a= map(lambda x: x * x, [1,2,3,4,5])
# print(a)
# print(list(a))
#
# # lambda 사용 장점 : 미리 선언되지 않은 함수를 코드 중간에 선언 가능
# # 단점 : 간단한 return 방식의 함수 구성만 가능



# # 파일 처리
# # 파일 처리 관련 함수
#
# # 파일 열기 함수 open
# # 파일 읽기 함수 read
# # 파일 쓰기 함수 write
# # 파일 닫기 함수 close
#
# # open()
# # 파일 오픈 함수의 매개변수 :
# #   1. 파일 경로
# #   2. 파일 오픈 모드 :
# #       2.1. 오픈모드 w : write 모드(새로쓰기)
# #       2.2. 오픈 모드 a : append 모드(이어쓰기)
# #       2.3. 오픈모드 r : read 모드(읽기)
#
# file = open("basic.txt",'w')
# file.write("hello python")
# file.write("hello python")
# file.write("hello python")
# file.write("hello python")
# file.close()
# # 파일을 열면 항상 닫아줘야함 : 파일을 중복으로 열리면 생기는 문제 방지


# # with 방식으로 파일을 여는 방법
# with open("basic.txt", 'w') as f:
#     f.write('hello ')
#     f.write('hello ')
#     f.write('hello ')
#     f.write('hello ')
# # with open() as f: 방식으로 파일을 오픈하면 close 생략 가능
#
#
# # 텍스트 읽기 read()
# with open('basic.txt', 'r') as f1:
#     contents = f1.read()
# print(contents)
#
#
# # 텍스트 한 줄씩 읽기
# # 데이터를 구조적으로 표현하는 형식 : CSV, JSON, XML
# # ex) CSV
# # 이름 , 키 , 몸무게
# # A , 170 , 80
# # b , 160 , 53
#
# # CSV파일은 한 줄에 하나의 데이터
# # 쉼표(,)로 데이터 구분
# # 첫 줄은 데이터의 헤더(헤어는 데이터가 무엇을 나타내는지)




# # p.331
# import random
#
# hanguls = list("가나다라마바사아자차카타파하")
# first = list("김이박최강나")
# # with open('info.txt', 'w') as file:
# with open('info.csv', 'w') as file:
#     for i in range(100):
#         name = random.choice(first) + random.choice(hanguls) + random.choice(hanguls)
#         weight = random.randrange(40, 100)
#         height = random.randrange(140, 200)
#         file.write("{}, {}, {}\n".format(name, weight, height))

# # p.332
# with open("info.csv", 'r') as file:
#     for line in file:
#         (name, weight, height) = line.strip().split(', ')       # 공백 삭제, 정렬
#
#         if (not name) or (not weight) or (not height):      # 값이 비어있는지 체크
#             continue
#         bmi = int(weight) / ((int(height) / 100) ** 2)
#         result = ""
#         if 25 <= bmi:
#             result = '과제중'
#         elif 18.5 <= bmi:
#             result = '정상체중'
#         else:
#             result = "저체중"
#
#         print('\n'.join([
#             '이름: {}',
#             '몸무게: {}',
#             '키: {}',
#             'BMI: {}',
#             '결과: {}',
#         ]).format(name, weight, height, bmi, result))
#         print()
#

#
# # p. 352,3 확인문제
# numbers = [1,2,3,4,5,6]
# print("::".join(map(str, numbers)))
#
# numbers2 = list(range(1, 10+1))
# print('# 홀수만 추출하기')
# print(list(filter(lambda x : x%2 == 1, numbers2)))
#
# print('# 3 이상, 7 미만 추출하기')
# print(list(filter(lambda x: 3 <= x < 7, numbers2)))
#
# print('# 제곱해서 50미만 추출하기')
# print(list(filter(lambda x: (x**2) < 50, numbers2)))


# p. 354 하노이 탑
count = 0
num = int(input("입력: "))
def hanoi(num, from_, to_, via_):
    # A  B  C
    global count
    count += 1
    if num == 1:
        print(num,' : ',from_, "=>", to_)
        return
    hanoi(num-1, from_, via_, to_)
        # A  C  B  # 가장 아래를 제외한 모든 원판 내려놓기
    print(num, " : ", from_,"=>",to_)   # 최하단 원판 옮기기 : 1회
    hanoi(num-1, via_, to_, from_)
        # C  B  A  # 가장 아래 원판 제외한 내려놓은 원판을 가장 아래 원판의 위에 올리기

hanoi(num, 'A', "B", 'C')
print(count)