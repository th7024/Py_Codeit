numbers=[]
print(len(numbers)) #리스트 길이

numbers.append(5) #값 추가
numbers.append(8) #값 추가
print(numbers)
print(len(numbers)) #리스트 길이

numbers = [2,3,5,7,11,13,17,19]
del numbers[3] #값 삭제
print(numbers)

numbers.insert(4,37) #해당 인덱스(4)에 값을 삽입(37) 원래 있던 값들은 뒤로 한칸씩 밀림
print(numbers)
