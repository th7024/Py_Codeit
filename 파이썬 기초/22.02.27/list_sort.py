numbers = [19,13,2,5,3,11,7,17]
#오름차순 정렬
# 1. sotred
new_list = sorted(numbers)
print(new_list)

#내림차순
new_list = sorted(numbers, reverse=True)
print(new_list)

print(numbers) # 기존의 리스트는 건들지 않음
# 2. sort
print(numbers.sort()) #sort는 아무것도 리턴하지 않음
print(numbers)
numbers.sort(reverse=True)#내림차순
print(numbers)