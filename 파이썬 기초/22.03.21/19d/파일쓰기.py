with open('new_file.txt','w') as f: #'a'와 'w'의 차이점 : a는 append로서 위 글에 이어서 작성, w는 위의 글을 덮어버리고 새로운 글을 작성
    f.write("Hello world!\n")
    f.write("My name is codeit")