# # 240122
#
# # 클래스 사용 이점
# # class
# # 생성자 __init__
# # 소멸자 __del__
# # 모듈화
# # 추상화
# # 함수를 포함
# # 식별자가 존재
# # 필드
# # self
# # 틀
# # 객체
# # object
#
# class testclass:
#     def __init__(self):     # 생성자(메서드)
#         self.name = 'testclass'     # 필드
#     def __del__(self):      # 소멸자(메서드)
#         pass
#
# testclass1 = testclass()    # 틀로 객체 생성
# print(testclass1)   # 객체 출력
#
# # testclass1은 객체이다.
# # testclass1은 testclass 클래스로 만든 객체이다.
# # testclass1은 ovject이다.
# # testclass1은 testclass의 인스턴스이다.
#
#
#
# # 클래스 구조를 이용해서 4개의 계산기가 돌아갈 수 있게 구현
# # 두 개의 숫자만 연산
# # 사칙연산만 지원
#
# class calculator:
#     value = 100
#     ssss = 200      # 클래스 변수
#     def __init__(self):
#         self.name = "계산기"   # 필드 : 객체마다의 독립적 변수 : 인스턴스 변수
#         self.num1 = 0
#         self.num2 = 0
#         self.value = 0
#     def add(self, x, y):
#         self.num1 = x
#         self.num2 = y
#         self.value = self.num1 + self.num2
#         return self.num1 + self.num2
#     def sub(self, x, y):
#         self.num1 = x
#         self.num2 = y
#         self.value = self.num1 - self.num2
#         return self.num1 - self.num2
#     def mul(self, x, y):
#         self.num1 = x
#         self.num2 = y
#         self.value = self.num1 * self.num2
#         return self.num1 * self.num2
#     def div(self, x, y):
#         self.num1 = x
#         self.num2 = y
#         self.value = self.num1 / self.num2
#         return self.num1 / self.num2
#     def __del__(self):
#         # pass
#         print(f"{self.name}파괴되었습니다.")
#     def quit(self):
#         self.__del__()
#
# num1 = calculator()
# num2 = calculator()
# num3 = calculator()
# num4 = calculator()
# # print(num1, "계산기 실행")
# # num1.quit()      # 강제 소멸
# # num1.__del__()   # 강제 소멸
# print(num3.mul(10,20))
# print(num3.value, "계산기에 기억된 마지막 값")
#
# print(num2.sub(20,10))
#
# print(num3.value, "계산기에 기억된 마지막 값")
# print(num2.value, "계산기2에 기억된 값")
#
# # 클래스 변수와 인스턴스 변수의 이름이 같다면 . 우선 접근
# print(num2.value)   # 객체 기준으로 접근 -> 인스턴스 변수
# print(calculator.value) # 클래스 기준으로 접근 -> 클래스 변수
# print(num2.ssss)
#
#
# # 클래스 변수 : 특정 클래스로 만들어진 객체끼리 공유하는 데이터(공용)
# # 인스턴스 변수 : 만들어진 인스턴스 객체 전용 데이터(전용)
#
#
#
# class fortest:
#     # def __init__(self):   # 객체를 생성하지 않는다면 init 생략 가능
#     #     self.x = 0
#     def __enter__(self):    # 스코프 자동 진입 함수
#         return self     # self : 인스턴스 객체 자신
#         # pass    # 오류 : x가 정의되지 않음
#     def __exit__(self, exc_type, exc_val, exc_tb):  # 스코프 자동 퇴장
#         # 예외 발생하지 않으면 모두 None 상태
#         pass
#
# with fortest() as test:
#     print(test)
#     # print(test.x)
#
#
# # 클래스 변수 :
# # 1. 클래스에 속한 변수
# # 2. 클래스의 모든 인스턴스 간 공유 가능
# # 3. 클래스 정의 내부에서 생성
# # 4. 클래스 자체 속성 상태 등에 사용
#
# # 인스턴스 변수 :
# # 1. 각 인스턴스에 속한 변수로 인스턴스와 연결되어 있음
# # 2. 독립적인 변수
# # 3. 객체 자체의 속성 상태 등 표현
#
# class myclass:
#     count = 0
#     grp = 1
#     def __init__(self):
#         myclass.count += 1
#         self.name = "dddd"
#     def __del__(self):  # 수동 호출 X : 파이썬 메모리 문제 발생 가능성 있음
#         print("삭제",self)
#         myclass.count -= 1
# class1 = myclass()
# class2 = myclass()
# class3 = myclass()
# del class2      # del 키워드로 객체 삭제
#
# print(myclass.count)
# print(myclass.grp)
#
#
# class ttt:
#     def setdata(self, a):   # init 함수 X
#         self.a = a
#
# t = ttt()   # 생성자 함수가 없어도 객체 생성 가능
# # 생성자 합수를 쓰는 이유 : 자동호출
#
# # print(t.a)    # 에러
# t.setdata("dddd")
# print(t.a)
#


# class c1:
#     def __init__(self, name):
#         self.name = name
#     def show(self):
#         print(self)
#     def plus(self,a,b):
#         return a+b
#
# # 클래스의 상속 inherit   : 클래스 확장, 변형, 카피 등에 사용
#
# class c2(c1):   # 클래스명(상속받을 클래스명)
#     def m(self, a, b):
#         return a-b
#     def show(self):     # 메서드 오버라이딩
#         return self
#
# ins2 = c2("c1으로부터 상속받은 c2클래스의 인스턴스")
# print(ins2.name)
# print(ins2.show())
# # 메서드 오버라이딩
#
#
# if isinstance(ins2, c2):
#     print("True")
#
# if isinstance(ins2, c1):
#     print("True")
#
#
# class c3(c1):
#     def c3method(self):
#         print("c3에만 구현된 함수")
#
# class c4(c2, c3):
#     def c4method(self):
#         self.c4Value = 100
#         self.__c4V = 400    # 프라이빗 변수(__var) : 클래스 밖에서 사용 불가
#         # 게터와 세터를 통해 사용 해야 함.
#
#         print("c2 + c3")
#
#     def showc4V(self):  # getter
#         print(self.__c4V)
#     def setc4V(self, value):    # setter
#         self.__c4V = value
#
# cc4 = c4("123")
# cc4.c4method()
# print(cc4.c4Value)
#
# cc4.showc4V()   # getter
# cc4.setc4V(300)
# cc4.showc4V()   # setter



# 문제) 추상화
# 클래스 구조로
# 콘솔에서 진행되는 게임
# 1. 건물 클래스 / 2. 사람 클래스 / 3. npc 클래스  / 4. 맵 클래스 / 5. 운영 클래스


























