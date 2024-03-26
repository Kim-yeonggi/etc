def outer_function(x):
    def inner_function(y):
        return x+y
    return inner_function

# 함수 중첩 선언 : 클로저 현상 발생

closure_instance = outer_function(10)   # 변수지만 함수(inner_function)가 담겨있음
# print(closure_instance)
# result = closure_instance(5)
# print(result)

print(closure_instance)
print(closure_instance(5))