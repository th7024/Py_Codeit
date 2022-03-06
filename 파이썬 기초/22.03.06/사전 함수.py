my_family = {
    '엄마' : '엄마다',
    '아빠' : '아빠다',
    '아들' : '나'
}

print(my_family.values()) #my_family 딕셔너리 value 출력

print('나' in my_family.values()) #value중 '나'라는 값이 있는 확인 후 boolean값을 리턴

print('아들' in my_family.keys())

for value in my_family.values(): #반복문으로 하나씩 받아옴
    print(value)
    
for key in my_family.keys():
    value = my_family[key] # value라는 변수에 my_family[key]값 즉 key-value를 받아옴
    print(key,value)
    
for key, value in my_family.items(): #items를 이용해서 key, value모두 인자로 받아옴 
    print(key,value)