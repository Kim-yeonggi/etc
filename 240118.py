# # 240118 클래스
#
# # 객체 지향 프로그래밍 언어
# # 객체 개체 object : OOP
# # 객체를 우선으로 생각해서 프로그래밍을 한다.
# # 클래스 기반의 프로그래밍 언어
# # 클래스를 기반으로 객체를 생성한다.
#
# # 추상화 : 필요한 요소만을 사용해서 객체를 표현하는 것
# # 객체 : 속성을 가질 수 있는 것
#
#
# # 클래스 선언 : 틀을 정의
# class className:
#     def __init__(self):     # 생성자 함수의 정의 __init__(self)
#         pass    # 클래스 내용
#
#
# # 클래스 내부 함수는 첫 매개변수로 self 입력
# # self : 자기 자신
#
# # 클래스는 클래스 이름과 같은(==) 함수(생성자)를 통해 객체를 만들어 낸다.
# className1 = className()    # className 클래스를 틀로 사용해서 className1을 만듦
#
#
# class Student:
#     num=1
#     def __init__(self, name):   # 생성자 함수
#         self.name = name    # self는 자기자신 / name 변수를 만든 것 / 뒤의 네임(=name)은 매개변수
#         self.age = 100
#         print("생성자")    # 호출 할 때마다 매번 실행
#     def __del__(self):      # 소멸자 함수
#         print("소멸자")    # 코드 종료시 호출한 생성자 수만큼 한 번에 소멸
#     def xxx(self):
#         self.name = "111"
#
# # students = [Student("1번학생"), Student("2번학생")]   # 인스턴스
# # print(students)
# # print(students[0].name)     # 1번학생
#
# # x = Student()   # TypeError: Student.__init__() missing 1 required positional argument: 'name'
# x = Student("3번학생")   # TypeError: Student.__init__() missing 1 required positional argument: 'name'
# print(type(x))
# print(x.num)    # 1
# print(x.name)   # 3번학생
# print(x.age)    # 100
# print(Student.num)  # 1
# # print(Student.age)  # AttributeError: type object 'Student' has no attribute 'age'
# x.xxx()


# 문제) 학생을 생성할 수 있는 클래스 구조를 만든다.
# 모든 학생은 1번 강의실에 포함되어 있다.
# 개인별 학생은 이름, 나이, 국어, 영어, 수학
# 학생을 객체로 3명 만들어서
# 학생 중 성적의 평균이 가장 높은 학생의 소속 강의실 번호, 이름, 나이 출력

class Students:
    average = 0
    classNumber = 1
    def __init__(self, name, age, kor, eng, math):
        self.name = name
        self.age = age
        self.kor = kor
        self.eng = eng
        self.math = math
    def cal_avg(self):
        return (self.kor + self.eng + self.math)/3

    def to_list(self):
        return [self.classNumber, self.name, self.age, self.cal_avg()]

students = [
    Students("1번학생", 27, 60, 10, 70),
    Students("2번학생", 24, 60, 100, 100),
    Students("3번학생",25, 65, 75, 85)
]
avg = 0
idx = -1
for s in students:
    if avg < s.to_list()[-1]:
        avg = s.to_list()[-1]
        idx += 1
print(f"강의실:{students[idx].classNumber}  이름:{students[idx].name}  나이:{students[idx].age}")
