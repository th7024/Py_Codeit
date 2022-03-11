print("Hello\n")
# \n 공백 한줄 넣기
print("Hello")

#strip 문자열 맨 앞과 맨 뒤에 있는 공백을 지워줌
print("           asdasd asdasd           ".strip())


with open('data/chicken.txt', 'r', encoding='UTF-8') as f: #파일명, r(읽기), w(쓰기) as 변수명
    for line in f:
        print(line.strip())