#sort 메소드
#저번에 정렬된 새로운 리스트를 리턴시켜주는 sorted 함수를 보여드렸습니다. some_list.sort()는 새로운 리스트를 생성하지 않고 some_list를 정렬된 상태로 바꿔줍니다.

numbers = [5, 3, 7, 1]
numbers.sort()
print(numbers)

#reverse 메소드
#some_list.reverse()는 some_list의 원소들을 뒤집어진 순서로 배치합니다.

numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)

#index 메소드
#some_list.index(x)는some_list에서 x의 값을 갖고 있는 원소의 인덱스를 리턴해줍니다.

members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))
print(members.index("태호"))

#remove 메소드
#some_list.remove(x)는some_list에서 첫 번째로 x의 값을 갖고 있는 원소를 삭제해줍니다.

fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론"]
fruits.remove("파인애플")
print(fruits)