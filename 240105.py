# # p.254
#
# # enumerate() 함수
# # 리스트 내부 요소를 반복문을 통해 출력할 때
# # enumerate()를 사용해서 열거 순서를 반환 받을 수 있다.
#
# lista = [3, 2, 1, 4, 5, 6]
# print(enumerate(lista))
# # enumerate()를 호출하면 enumerate object(열거 객체)가 반환
# print(list(enumerate(lista)))
# # 리스트를 enumerate() 후 다시 list()로 형변환 시
# # 리스트의 요소별 인덱스 변호와 요소의 값을 튜플형태로 없을 수 있다.
# # => [(0, 3), (1, 2), (2, 1), (3, 4), (4, 5), (5, 6)]
#
#
# # for 문과 사용 예
# for idx, value in enumerate(lista):
#     print("{}번째 요소의 값: {}".format(idx, value))



# # 이터러블 / 이터레이터
# # 반복할 수 있는 것 : 이터러블 (iterable)
# # 반복가능 객체 : 이터러블 객체 ex) list, string, enum 객체 등
# # 이터러블은 내부에 있는 요소를 차례로 꺼낼 수 있는 객체
#
# # 이터레이터 : 이터러블에서 next() 함수를 통해 하나씩 꺼낼 수 있는 요소
#
# numbers = [-6,-5,253,254,255,256,257]
# print(id(numbers), "리스트 주소")
# print(id(numbers[0]))
# print(id(numbers[1]))
# print(id(numbers[2]))
# print(id(numbers[3]))
# print(id(numbers[4]))
# print(id(numbers[5]))
# print(id(numbers[6]))
# # -5 ~ 256 까지의 정수는 파이썬 메모리에 기본적으로 할당되어 있음
#
# r_num = reversed(numbers)
# print((r_num))      # reversed 함수의 반환 값 : reverseiterator 객체
#
# # 위 reverseiterator 같은 이터러블 객체를 대상으로 next()함수를 적용
# print((next(r_num)))    # 6 출력
# print((next(r_num)))    # 5 출력
# print((next(r_num)))    # 4 출력
# print((next(r_num)))    # 3 출력
# print((next(r_num)))    # 2 출력
# print((next(r_num)))    # 1 출력
#
# # 반복문 for를 사용하지 않고 next함수를 통해 차례로 하나씩 값 호출 가능

# # p.267
# output=[]
# for i in range(1,101):
#     if "{:b}".format(i).count("0") == 1:
#         output.append(i)
#         print("{} : {:b}".format(i, i))
#
# print("합계:", sum(output))



# # p.268
# # 1. 숫자의 종류
# nums = [1,2,3,4,1,2,3,1,4,1,2,3]
# number = list(range(0,10))
# dict = {}
# c = 0
# for i in number:
#     if i in nums:
#         c += 1
#         dict[f"{i}"] = nums.count(i)
# print("사용된 숫자의 종류는 {}개입니다.\n참고: {}".format(c, dict))
#
# '''
# nums = [1,2,3,4,1,2,3,1,4,1,2,3]
# count = {}
# for i in num:
#     if i not in count:
#         count[i]=0
#     count[i]+=1
# print("{}")
# '''


# # 2. 염기의 개수
# dna = ['a', 't', 'g', 'c']
# input_dna = input("염기 서열을 입력해주세요: ")
# # input_dna = "ctacaatgtcagtatacccattgcattagccgg"
# for i in dna:
#     print(f"{i}의 개수: {input_dna.count(i)}")


# # 3. 염기 코돈 개수
# dict = {}
# input_dna = input("염기 서열을 입력해주세요: ")
# # input_dna = "ctacaatgtcagtatacccattgcattagccgg"
# for i in range(0, len(input_dna) ,3):
#     if len(input_dna[i:i + 3]) == 3:
#         if input_dna[i:i+3] in dict.keys():
#             dict[input_dna[i:i+3]] += 1
#         else:
#             dict[input_dna[i:i+3]] = 1
# print(dict)
#
#
#
# # 4. 리스트 평탄화
# li = [1,2,[3,4],5,[6,7],[8,9]]
# res = []
# for i in li:
#     if type(i) == list:
#         for j in i:
#             res.append(j)
#     else:
#         res.append(i)
# print("{}를 평탄화 하면\n{}입니다.".format(li, res))




# # Ch5 함수
# # 함수 function, method
#
#
# # 함수의 호출 = 함수의 사용 = call
# # 함수의 매개변수
# # 함수의 리턴 = 함수의 반환 = 함수의 결과
#
#
# # listb = [1,2,3,4]
# # x=len(listb)
# # print(x)
#
#
# # 함수의 기본 형태
# # def 키워드를 사용한다.
#
# # print(myfunc)       # error : 정의하기 전에 호출 X
#
# def myfunc():               # 함수의 정의
#     print("함수실행문1")      # 함수 내부 실행문
#     print("함수실행문2")
#     print("함수실행문3")
#     print("함수실행문4")
#
# myfunc()    #함수의 호출
# # 매개변수 : 함수의 정의 측면에서 용어
# # 매개변수 : 함수에서 요구하는 재료 변수
# #

# print(locals(), "local1")
#
# def myfunc2(mV,nV):
#     print(id(mV))
#     print(id(nV))
#     print(id(mV+nV))
#     print(locals(), "locals2")
#     locals()['xx'] = 10     # 프로그램 실행 중에 변수 생성 가능
#     print(locals(), "locals3")
#
# # myfunc2()       # TypeError: myfunc2() missing 2 required positional arguments: 'a' and 'b'
# print(locals(), "locals4")
# myfunc2(127,128)
# # print(a)        # NameError: 함수의 매개변수는 함수 내에서만 유효하다.
#
#
# # parameter : 매게변수 (함수의 호출에서 전달한 값을 정의에서 받는 변수) : myfunc2 ; mV, nV
# # argument : 전달인자(함수 호출 시점에서 함수의 정의로 전달하는 값) : myfunc2 ; 127, 128


# # 가변 매개변수 : *
# # 가변 매개변수 뒤에는 일반 매개변수가 올 수 없다.
# # 가변 매개변수는 하나만 사용 가능
# def myfunc(a, b, *c):
#     print(a,b,c)
#
# myfunc(1,2,3,4,5,6) # 1 2 (3, 4, 5, 6) => 가변매개변수 : 튜플 형태로 할당
#
# # p.278
# def print_n_times(n, *values):
#     # n번 반복
#     for i in range(n):
#         for value in values:    # values(가변 매개변수)는 리스트처럼 사용 가능
#             print(value)
#         print() # 줄바꿈
# # 함수 호출
# print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")


# #  매개변수 : 일반 / 가변 / 기본
# # 일반은 가변보다 뒤에 오면 안되지만 기본은 가능

# # 기본 매개변수
# # 매개변수 = 값 형태
# # 기본 매개변수는 기본 값을 가짐
# # 따라서 안써도 되고 써도 됨
# # default 값이 있음
# print("첫번째 줄", "내용", sep=" # ", end=' // ', flush=False)
# print("두번째 줄")
# # ex) 기본 : sep=" " => sep=""하면 , 해도 붙어서 출력

# # p.279
# def print_n_times(value, n=3):
#     for i in range(n):
#         print(value)
#
# print_n_times("3번 반복")


# # 리턴 return
# # 어떤 함수는 원본을 바꾸고
# # 어떤 함수는 원본을 바꾸지 않고
# # 어떤 함수는 리턴값이 있고
# # 어떤 함수는 리턴값이 없고
#
# a = 'hello'     # 문자열 ; 값 변경 불가
# # 비파괴 함수 -> return 값 O
# print(a.replace('h', '!'))
# # print(a)
# print(a.upper())
# # print(a)
# print(a.strip())
# # print(a)
#
# b=[1,2]         # 리스트 ; 값 변경 가능
# print(b.append(3))      # None 출력 -> return 값 X
# print(b)


# def rt():
#     print(1)
#     return 100
#     print(2)
#
# rt()            # 1만 출력
# print(rt())     # 1과 100 출력 : print() -> return 값도 출력
#
# # return 은 함수 내에 작성 가능
# # 함수 내에서 return 키워드가 읽히면 함수를 탈출한다.
# # return 뒤에 작성된 value를 들고 탈출함. ; return value
# # return 뒤에 value가 있으면 None 반환

# # p.287, 288
# def sum_all(start, end):
#     output = 0
#     for i in range(start, end+1):
#         output += i
#
#     return output
#
# print("0 to 100: ", sum_all(0, 100))
# print("0 to 1000: ", sum_all(0, 1000))
# print("50 to 100: ", sum_all(50, 100))
# print("500 to 1000: ", sum_all(500, 1000))


def sum_all(start=0, end=100, step=1):
    output = 0
    for i in range(start, end+1, step):
        output += i

    return output

print("A.", sum_all(0, 100, 10))
print("B.", sum_all(end=100))
print("C.", sum_all(end=100, step=2))
# default 값이 있어도 argument 설정 가능
