def my_f():
    x = 3
    print(x)
my_f()
#print(x) => 변수 x는 my_f함수 내에 있는 변수이기 때문에 함수 밖에서는 출력이 안됨.

x = 2 #함수 밖에서 선언한 전역변수
def my_f2(): #함수에서 변수를 사용하면 항상 지역변수가 있는지 확인하고 전역변수를 확인함
    x = 3 #함수 내에서 선언한 지역변수
    print(x) # x = 3
my_f()
print(x) # x = 2

