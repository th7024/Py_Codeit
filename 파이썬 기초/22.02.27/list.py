#리스트 (List)
numbers = [2,3,5,7,11,13]
names = ["윤수","혜린","태호","영훈"]

print(numbers)
print(names)

#리스트 요소 꺼내오기 (인덱싱)
print(names[1])
print(numbers[1]+numbers[3])
print(numbers[-1])

#리스트 슬라이싱
print(numbers[0:4]) #0번 인덱스부터 3까지 자르는 것 0<=~<4
print(numbers[2:]) #2번 인덱스부터 끝까지
print(numbers[:3]) #맨 앞부터 2번 인덱스까지 자름름
numbers[0]=7 #0번 인덱스에 7을 넣어줌