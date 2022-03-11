
with open('data/chicken.txt', 'r', encoding='UTF-8') as f: #파일명, r(읽기), w(쓰기) as 변수명
    for line in f:
        print(line)