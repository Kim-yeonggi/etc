# # a = [1,2,3]
# # b = {'key1':1, 2:5, 4:'ss'}
# # c=100
# # d='ss'
# # e='ss'
# # print(id(a), ":a list id")
# # print(id(b), ":b dict id")
# # print(id(c), ":c int id")
# # print(id(d), ":d str id")
# # print(id(e), ":e str id")
# # print("--"*20)
# # print(id(a[0]), ":a[0] list 0 idx id")
# # print(id(a[1]), ":a[1] list 0 idx id")
# # print(id(a[2]), ":a[2] list 0 idx id")
# # print("--"*20)
# # print(id(b['key1']))
# # print(id(b[2]))
#
#
# # Ch4. 반복문
# # 반복문 for
# print(range(100))           # range(0, 100)
# print(type(range(100)))
# for i in range(3):          # 이터러블 객체 : list, 문자열, range
#     print("for 100번")
#
#
# '''
# for i in 반복 가능한 이터러블 객체:
#     실행 문장
#     실행 문장
# '''
# for i in "hello":
#     print(i)
#
# for i in [2,2,3,4,5,5,5,5,5,]:
#     print(i)
#
#
# # for i in 100:     # Type Error : 'int' object is not iterable
# #     print(i)
#
#
# x = 200
# dict1 = {'key1':100, 'key2':x}
# for i in dict1:
#     print(i)        # key 값 출력
#     print(dict1[i]) # value 값 출력
#
# print(i)        # key2 -> 변수 i에 for 문 마지막 값 저장되어 있음
#
# for i in list(dict1.values()):
#     print(i)
#
#
# print(id(i), i)
# print(id(x), x)
#
#
# s = '안녕하세요'
# for i in s:
#     print(i)
#
# for i in range(len(s)):
#     print(s[i])
#
#
# s2 = "11111"
# for i in s2:
#     print(id(i), i)
# print(id(s2), s2)
#
# print(id(dict1), dict1)
# print(id(dict1['key1']), dict1['key1'])
# print(id(dict1.keys()), dict1.keys())
#
# # => iterable 객체들 모여있음
#
#
# x=[(1,2),(3,4),(5,6)]
# for a,b in x:    # 리스트를 개별적으로 호출 가능
#     if a + b == 7:
#         # continue
#         break
#     print(a+b)
#
#
# # continue 키워드
# # for 반복문의 진행 중 continue 키워드가 실행되면 for문의 처음으로 돌아감.
# # continue는 반복문의 자식으로만 사용 가능
# # 다음 바퀴로
#
# # break 키워드
# # for 반복문의 진행 중 break 키워드가 실행되면 for 문을 완전히 탈출함.
# # 종료
#
#
#
# # range() 범위 객체를 생성하는 range함수
# r = range(10)
# print(r)        # range(0,10)       0 <= ~ <10
# print(list(r))  # [0, 1, 2, ..., 9]  -> list 형변환 가능
#
# r1 = range(5,10)    # range(start, end)
# print(r1)
#
# list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in list2:
#     for j in i:
#         print(j)
#
#
#
# # 리스트와 for문의 사용법2
# # case1
# a = [1,2,3,4]
# res = []
# for num in a:
#     res.append(num*3)
# print(res)
#
# # case 2
# b = [1,2,3,4]
# res2 = [num*3 for num in b if num%2==0]     # [실행문 for문 조건문]
# print(res2)

# # ex)
# # 딕셔너리에는 5개의 키가 있다.
# # 5개의 키는 5명의 사람 이름
# # value에는 각 인원의 키(cm), 몸무게(kg)가 리스트로 묶여서 할당되어 있음
# # 사용자에게 어떤 사람인지를 입력받고
# # 입력 받는 사람의 bmi 출력
# # bmi = 몸무게(kg) / 키(m)^2 -> 소수점 1자리 까지만 표현
# # 미터단위의 키는 소수점 2자리까지만 표현
# # 결과 출력 예시 : "A의 키는 165cm 몸무게는 50kg으로 bmi는 x 입니다."
#
# user_list = {'kim':[165,64], 'lee':[170, 80], 'park':[155, 45], 'choi':[185, 90], 'kang':[160, 60]}
# user = input("이름을 입력하세요: ")
# # user = 'kim'
#
# if user in user_list:
#     high, weight = user_list[user]
#     bmi = weight / (high * 0.01)**2
#         print("{}의 키는 {}cm 몸무게는 {}kg으로 bmi는 {:.1f}입니다.".format(user, high, weight, bmi))\
#
# for i in list(user_list):
#     if user == i:
#         high = user_list[i][0]
#         weight = user_list[i][1]
#         bmi = weight / (high * 0.01) ** 2
#         print("{}의 키는 {}cm 몸무게는 {}kg으로 bmi는 {:.1f}입니다.".format(user, high, weight, bmi))
#     else:
#         continue


# # dictionary NameError 오류
# dict_key = {
#     name:"망고",          # 변수를 선언해놓거나, ""로 감싸 문자열로 작성해야함
#     type:"당절임"
# }


# # while 반복문
# # for문과 마찬가지로 실행문 반복하는 역할
# # while문의 기본 구조 형태
# '''
# while 조건문:
#     실행문
#     싷행문
# '''

# # while문은 while뒤에 작성되어 있는 조건문이 참인 동안 계속 반복된다.
#
# count = 10
# while count > 0:
#     count -= 1
#     if count%2 == 0:
#         continue
#     print(count)
#
# # while에서도 continue와 break를 for문에서 사용하는 것과 동일하게 작동한다.


# num = 0
# while num != 3:
#     print("1.음료, 2.음식, 3.나가기")
#     num = int(input("메뉴 번호 입력: "))
#     print(num, "선택")


# # 무한루프
# # 무한으로 반복되는 조건의 while문
# count = 0
# s = ""
# while 1:
#     count += 1
#     if count == 10:
#         break
#     s += str(count)
#     for i in range(3):
#         s += ","
#         s += str(i)
#     print(s)
#     s = ''
#
# count1 = 0
# count2 = 0
# while 1:
#     print("1단계")
#     count1 += 1
#     while 1:
#         print("2단계")
#         count2 += 1
#         if count2 > 5:
#             for i in range(3):
#                 print("for문")
#
#             count2 = 0
#             break
#         print("219")
#     print("220")
#     if count1 == 3:
#         break


# # p.237 별짓기(피라미드)
# output = ""
#
# for i in range(1, 10):
#     for j in range(0, i):
#         output += "*"
#     output += '\n'
# print(output)

# # range(시작, 끝, 부호(진행방향, +-)간격)
# print(list(range(1, 10, 2)))        # [1, 3, 5, 7, 9]
# print(list(range(10,0,-2)))         # [10, 8, 6, 4, 2]

# # p.238 별짓기2
# output = ""
# for i in range (1, 15):             # 1 ~ 14
#     for j in range(14, i, -1):      # 14 ~ i : 공백
#         output += " "
#     for k in range (0, 2*i - 1):    # 0 ~ i*2-1 : 별
#         output += '*'
#     output += '\n'
# print(output)


# # ex)
"""

$#############$         // 15글자 (13 # + 2 $)
 $###########$
  $#########$
   $#######$
    $#####$
     $###$
      $#$
       $
       
"""
# n = int(input("몇 행?: "))
# output = ""
# for i in range(n, 0, -1):
#     for j in range(0, n-i):
#         output += " "
#     for k in range(0, i*2-1):
#         if k == 0 or k == i*2-2:
#             output += "$"
#         else:
#             output += "#"
#     output += '\n'
# print(output)


# n = int(input("몇 행?"))
# output = '\n'
# for i in range(n):
#     output += ' '*i
#     output += '$'
#     output += "#"*(2*(n-i)-3)
#     if i != len(list(range(n)))-1:
#         output += "$"
#     output += '\n'
# print(output)


# p.243
import time
# print(time.time())

number = 0
print(time.time(), "start t")

# 5초동안 반복
target_tick = time.time() + 5

while time.time() < target_tick:
    number += 1
print(f"5초 동안 {number}번 반복했습니다.")
print(time.time(), "end t")
# 시간이나 날짜시간 객체는 해당 함수를 인터프리터가 읽어서 호출하는 시점의 시간을 반환




