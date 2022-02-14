print(type(3))
print(type(3.0))
print(type("3"))
print(type(True))

def hello():
    print("hello")

print(type(hello)) # 'function' : 내가 정의한 함수
print(type(print)) # 'builtin_function_or_method' : 내장되어있는 함수