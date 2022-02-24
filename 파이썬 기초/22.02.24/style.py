# 이해하기 쉬운 코드 = 좋은 스타일을 가진 좋은 코드

#안 좋은 스타일의 코드
print(6.28*4)
print(3.14*4*4)
print(6.28*8)
print(3.14*8*8)

#변수 사용
a = 3.14 #원주율
b = 4 #반지름
print(2*a*b)
print(a*b*b)
b=8 #반지름
print(2*a*b)
print(a*b*b)


#변수명 변경 및 줄띄움 사용
PI = 3.14 #원주율

radius = 4 #반지름
print(2*PI*radius)
print(PI*radius*radius)

radius=8 #반지름
print(2*PI*radius)
print(PI*radius*radius)

#함수 사용
PI = 3.14#원주율

#반지름이 r인 원의 둘레 계산
def calculate_circumference(r):
    return  2* PI * r

#반지름이 r인 원의 넓이 계산
def calculate_area(r):
    return PI * r * r

radius = 4 #반지름
print(calculate_circumference(radius))
print((calculate_area(radius)))

radius = 8 #반지름
print(calculate_circumference(radius))
print((calculate_area(radius)))