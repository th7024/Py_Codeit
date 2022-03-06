#딕셔너리 (여러자료를 모아놓음)
#key-value pair 
my_dictionary = {
    5: 25, #key = 5 , value = 25
    2:4, 
    3: 9
}
print(type(my_dictionary)) #<class 'dict'>

#자료 찾기
print(my_dictionary[3]) #키를 넣어주면 value가 나옴

#추가
my_dictionary[9] = 81 #9라는 key에 81이라는 value가 존재

print(my_dictionary) #순서의 개념이 없음

my_family = {
    '엄마' : '가가가',
    '아빠' : '아빠다',
    '아들' : '나'
}
print(my_family)