with open('vocabulary.txt','a',encoding='utf-8') as f:
    while True:
        en = input("영어 단어를 입력하세요:")
        if en == 'q':
            break
        f.write(en+": ")
        kr = input("한국어 뜻을 입력하세요:")
        f.write(kr + "\n")