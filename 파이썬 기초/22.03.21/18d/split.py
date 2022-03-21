
my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split(". ")) #파라미터를 기준으로 문자열을 나눔 "."을 기준으로 나눈것

full_name = "Kim, Yuna"
name_data = full_name.split(", ")
last_name = name_data[0]
first_name = name_data[1]
print(last_name, first_name)

print("          \n\n        2  \t  3 \n 5  7 11   \n\n".split()) #파라미터를 안넘겨주면 화이트 스페이스가 기준이 됨
numbers = "          \n\n        2  \t  3 \n 5  7 11   \n\n".split()
print(numbers[0]+numbers[1]) #split을 이용해서 리스트를 만들면 문자열로 리스트를 만들어줌.

