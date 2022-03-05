#range : 구간을 만들어줌
#장점 : 간편함, 깔끔함, 메모리 효율성

#range(a,b) 파라미터 두개
for i in range(1,6): #1부터 5(b-1)까지의 범위
    print(i)

#range(a) 파라미터 한개
for i in range(10): #0부터 9(a-1)까지의 범위
    print(i)

# range(a,b,c) 파라미터 세개
for i in range(3, 17, 3):  # 3부터 16(b-1)까지,간격 c
    print(i)