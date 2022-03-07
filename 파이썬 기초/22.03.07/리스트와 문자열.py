#리스트 : 자료형을 나열하는 것
#문자열 : 문자를 나열하는 것
alpha_list = ['A','B','C','D','E','F','G']
print(alpha_list[0])
print(alpha_list[1])
print(alpha_list[2])
print(alpha_list[3])

alpha_str = 'ABCDEFG'
print(alpha_str[0])
print(alpha_str[1])
print(alpha_str[2])
print(alpha_str[3])

#슬라이싱
print(alpha_list[0:3])
print(alpha_list[4:])
print(alpha_list[:4])

print(alpha_str[0:3])
print(alpha_str[1:])
print(alpha_str[:2])

#연결
str_1 = "안"
str_2 = "녕"
str_3 = str_1+str_2
print(str_3)

list_1 = [1,2,3,4]
list_2 = [5,6,7,8]
list_3 = list_1 + list_2
print(list_3)

#길이(len())
list_1 = [1,2,3,4]
print(len(list_1))
str_11 = "asdasdasdasd asdasd"
print(len(str_11))

#문자열은 리스트와 달리 수정이 불가능
name = 'codeit' + 'it' #수정이 아닌 새로운 문자열을 만드는 것은 가능
print(name)