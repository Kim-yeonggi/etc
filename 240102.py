# Ch1. 파이썬

import keyword          # 주황색 : 키워드 / 흰색 : 식별자
print(keyword.kwlist)   # 보라색 : 함수
10                      # 청록색 : 정수
"10"                    # 녹색 : 문자열
x=100

# 주석 : 인터프리터 처리 X
# 키워드 -> 대소문자 구분  / ex) True true
# 노란줄 : 사용 X / 빨간줄 : 문법 오류
# 키워드 : 개별적으로 기능 보유

# 식별자(= 변수명) id
# 키워드는 식별자로 사용 불가
# 특수문자는 언더바_ 만 허용
# 숫자로 시작 X, 공백 포함 X

# 스네이크 케이스 : 단어 사이 언더바 사용 snake_case
# 캐멀 케이스 : 단어 첫글자에 대문사 사용 CamelCase

# 연산자 : + - * / %(나머지)
# 독립적 사용 X -> 값과 값 사이에 사용

# 리터럴 : (고정된 값) 자료
print(10)     # console에 출력하는 (내장)함수
print(x)
print("100")
print(1,2,3,4,5)    # 쉼표 -> 공백

# p.77
# 하나만 출력합니다.
print("# 하나만 출력합니다.")
print("Hello Python Programming...!")
print()     # 줄바꿈

# 여러 개를 출력합니다.
print("# 여러 개를 출력합니다.")
print(10, 20, 30, 40, 50)
print("오늘 날짜는", "2024년", "1월", "2일", "입니다.")
print()

# 아무것도 입력하지 않으면 단순하게 줄바꿈합니다.
print("# 아무것도 출력하지 않습니다.")
print("ㅡㅡㅡ확인 전용선ㅡㅡㅡ")
print()
print()
print("ㅡㅡㅡ확인 전용선ㅡㅡㅡ")
print()

# Ch2 자료형
# string(문자열) (python은 문자, 문자열 구분 X) : text
# number(숫자) : 10, 20, 10.5, ...
# bool(논리형) : True / False
print(10)
print(type(10))     # 자료형 확인
print(type("hello"))
print(type(True))
print(type(type(len("hello"))))     # 5 -> int -> type
print()

# 문자열 : "" or ''로 텍스트 감싸기
# "hello" / 'hello'
# "hello' / 'hello"  X
# 공백 O

# "", '' 같이 사용하는 경우
print("오늘 날짜는 '2024년 01월 02일' 입니다.")
print(len("오늘 날짜는 '2024년 01월 02일' 입니다."))
print(len(" "))     # 1 출력 -> 공백도 문자열 길이에 포함
print()

# syntax error 구문오류 or 문법오류 : 빨간 밑줄

# 이스케이프 코드
# \t : tab
# \n : 줄바꿈
# \\ : \
# \' : '
# \" : "

print("이름\t나이\t지역")
print("윤인성\t25\t서구")
print("윤아린\t24\t중구")
print("김영기\t27\t유성구")
print("aa\taaa\naaaa\'aaaaa\"aaaaaa\\\n")

print("""123""")
print(              # """ : 세개로 감싸면 입력한 그대로 출력
    """123
    
    \t123
    111123 111~~
222
    """
)
print()

# 연산자
# + - * /
# 1. 문자열 + 문자열 : 문자열 연결
print("abc" + "def")

# 2. 문자 + 숫자 : 불가능
# print("hello" + 123)    #TypeError

# 3. 문자열 * 숫자 : 숫자만큼 문자열 반복 출력
print("문자 " * 3, "\n")

# 문자열 인덱싱
# 대활호 [] 안에 인덱스 번호 (0부터 시작)
# 제로 인덱스
x="hello"
print(x)

print(x[1])
print(x[-1])        # -1 : 마지막 인덱스
print("012345"[-1])     # 문자열에서 직접 선택 가능
print("012345"[-2], "\n")     # -1, -2 ... : 뒤에서 부터 호출 가능

# 문자열 슬라이싱
#대괄호 안에 start:end 형태로 사용
print("012345"[1:4])    # end 인덱스는 호출 X  (start <= i < end)
print("012345"[1:-3])
print("012345"[2:])     # 공백 = 끝까지
print()

# IndexError(index out of range)
# print("안녕하세요"[5])   # IndexError: string index out of range -> 문자열 길이를 초과하는 index를 호출함

print(len("안녕하세요     "))
print()

# 숫자 데이터
# 정수 / 실수 로 구분
# 정수 int : 0, 1, 100, -100
# 실수 float : 0.0, 1.5, -3.141592
# floating point 부동 소수점
# 소수점이 움직이는 숫자
# ex) 52.273 = 0.52273 * 10^2   or   5.2273 * 10^1

print(200)
print("200")
print(100.0)
print(type(100.0))
print(type(100))
print()

# 숫자의 연산자
# + - * /
# 숫자는 사칙연산 모두 사용 가능 / 문자는 + * 만 가능
# // : 목
# % : 나머지

print(4/2)      # 정수와 정수의 사칙 연산 중 나누기 연산은 실수 형태로 결과 출력
print(4//2)     # // 연산자 : 정수 형태로 결과 출력
print(4%2)      # % 연산자 : 정수 형태로 출력
print()

print(10//3)
print(10%3)

# 제곱 연산자 : **
print(5**2)
print(5**3)
print()


# 변수
x       # x라는 이름의 변수 선언 : x -> 식별자
x = 10  # 변수 x에 값 할당 ( = : 대입 연산자 -> 우측을 좌측(변수)에 할당)
pi = 3.14   # 변수 pi 선언, 할당

print(id(10))
print(id(11))
print(id(x))        # -> 변수는 중계자 역할 (값을 변수 x에 저장한게 아님)
y = x
print(id(y))        # x, y는 모두 10을 가리키고 있음 => 변수의 참조
print()

a=10
b=20
print(a*b)
print()

# p.115 : 변수의 선언과 할당
pi = 3.14159265
r = 10

# 변수 참조
print("원주율 =", pi)
print("반지름 =", r)
print("원의 둘레 =", 2*r*pi)
print("원의 넓이", pi*(r**2))
print()

# 대입 연산자
# ex) x=10 형태 -> 우측항을 좌측항에 할당

# 복합 대입 연산자 : 자신에게 우측항 연산 후 재할당
# +=
# -=
# *=
# /=
x=100
x+=1    # x = x + 1
print(x)

x-=100
print(x)    # x = x - 1

x *= 100    # x = x * 100
print(x)

x /= 100    # x = x / 100
print(x)

y="hello"
y+="!!"
y*=3
print(y)
print()


# 사용자 입력 대기 합수
# y = input("값을 입력해주세요: ")
# print(y, "\n")

# input 함수 괄호 안에 입력한 내용 == 프롬프트 문자열
# 사용자에게 입력 요구하는 안내 멘트
# 인터프리터 방식인 파이썬이 input 함수를 호출하면 실행 도중 해당 라인에서 블록 상태(입력전까지 정지)

# input을 통해 입력한 값 -> 문자열 처리
# print(type(input("타입확인을 위한 사용자 값 입력:")))
z = input("타입확인을 위한 사용자 값 입력:")     # ex) 10 입력
z = float(z)        # 형 변환    10.0
z = str(z)          # "10.0"
print(type(z))      # str
print(z)            # 10.0
print(len(z))       # 4
z = float(z[2:])    # .0
print(z)            # 0.0

print()

# p.121
string_a = input("입력A> ")
int_a = int(string_a)

string_b = input("입력B> ")
int_b = int(string_b)

print("문자열 자료:", string_a + string_b)
print("숫자 자료:", int_a + int_b)

print()

# p.122_1
output_a = int("52")
output_b = float("52.273")
print(type(output_a), output_a)
print(type(output_b), output_b)

print()

# p.122_2
input_a = float(input("첫번째 숫자>"))
input_b = float(input("두번째 숫자>"))

print("덧셈 결과:", input_a + input_b)
print("뺄셈 결과:", input_a - input_b)
print("곱셈 결과:", input_a * input_b)
print("나눗셈 결과:", input_a / input_b)

print()

# debug 실행 : 중단점 => f9로 한 줄씩 실행 가능