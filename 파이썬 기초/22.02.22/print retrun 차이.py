def print_sq(x):
    print(x * x)

def get_sq(x):
    return x * x
print("1 = ")
print_sq(3)
print("2 = ")
get_sq(3)
print("3 = ")
print(get_sq(3))
print("4 = ")
print(print_sq(3)) #print_sq는 리턴값이 없어 None을 출력함