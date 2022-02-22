# 상수(constant) -> 대문자로 표시
# 대문자로 쓰는 이유
# 일반 변수랑 구별하기 위해
# 실수를 하지 않기 위해
PI = 3.14 #원주율 '파이'

def cal(r):
    return PI * r * r

radius = 4
print("반지름{}, 넓이 {}".format(radius, cal(radius)))

radius = 6
print("반지름{}, 넓이 {}".format(radius, cal(radius)))

radius = 7
print("반지름{}, 넓이 {}".format(radius, cal(radius)))