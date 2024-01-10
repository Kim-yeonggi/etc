# # 재귀함수
# # 일부 반복문으로 대체 가능
# # Recursion / Recursive
# # def myfunc():
# # 함수가 자기 자신을 다시 호출하는 함수
#
# # f(x) = 2x + 1 - 일반함수
# # 재귀함수 - 팩토리얼
# # n! = n * (n-1) * (n-2) * ... * 1
#
# # p.293
# def factorial(n):
#     output = 1
#     for i in range(1, n+1):
#         output *= i     # output = output * i
#     return output
# print(factorial(0))

#
# # p.294
# # fac(n) = n*fac(n-1)
#
# def fac2(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fac2(n-1)
# print(fac2(5))


# # ex) 딕셔너리
# d1 = {"1":{"1":{'1':{'1':10000}}}}
# def show(d):
#     if type(d['1']) != int:
#         show(d['1'])
#
#     else:
#         print(d['1'])
# show(d1)
#
#
# # p.304 리스트 평탄화
# ex = [[1,2,3],[4,[5,6]],7,[8,9]]
# def flatten(data):
#     out = []
#     for i in data:              # [1 2 3] [4 [5 6]] 7 [8 9]
#         if type(i) == list:
#             out += flatten(i)
#         else:
#             out.append(i)
#     return out
# print(flatten(ex))

# # p.314
# # 앉힐 수 있는 최소 사람 수 = 2
# # 앉힐 수 있는 최대 사람 수 = 10
# # 전체 사람 수 = 100
# memo = {}
#
# def sit(sp1, sp2):
#     key = str([sp1, sp2])
#
#     if key in memo:
#         pass
#     if sp1 < 0:
#         return 0
#     if sp2 < 1:
#         return 1
#
#
# print(str([1, 2])[0])





