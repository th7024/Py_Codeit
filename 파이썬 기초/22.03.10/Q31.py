import random

num = random.randint(1,20)
print(num)
cnt =0
for i in range(4, 0, -1):
    n = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(i)))
    if n > num:
        print("Up")
    elif n< num:
        print("Down")
    else:
        print("축하합니다. {}번만에 숫자를 맞히셨습니다.".format(4-i+1))
        cnt = 1
        break
if cnt==0:
    print("아쉽습니다. 정답은 {}입니다.".format(num))