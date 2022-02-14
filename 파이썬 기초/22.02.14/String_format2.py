print("저는 {1},{0},{2}를 좋아합니다.".format("박지성","유재석","손흥민"))
num1= 1
num2 = 3
print("{0}나누기 {1}은 {2}입니다.".format(num1,num2,num1/num2))
print("{0}나누기 {1}은 {2:.2f}입니다.".format(num1,num2,num1/num2)) #{2:.2f} 2번format을 .2소수점 두번째 자리만큼 반올림하기. ex>.0정수

#f-sting 새로운 방식
name = "최지웅"
age = 32

print(f"제 이름은 {name}이고 {age}살입니다.")