with open('vocabulary.txt','r',encoding='UTF-8') as f:
    for line in f:
        str =line.strip().rsplit(":")
        print(str[1]+":")
        en = input()
        if str[0]==en:
            print("맞았습니다!\n")
        else:
            print("아쉽습니다. 정답은 {}입니다.".format(str[0]))