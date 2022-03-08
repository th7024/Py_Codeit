#코드를 여러파일로 나눠서 구현
# 다른 파이썬 프로그램에서 사용할 수 있는 파이썬 코드 : 모듈
# 같은 15d 폴더에 있는걸 불러오는 것
#import calculator as calc   #calculator라는 파일을 불러오겠다는 뜻 as clac : calculator대신 calc라는 이름으로 대신 쓰겠다는 것
#print(calc.add(2,5)) 이렇게 사용 앞에 함수명 붙음
from calculator import add,mul #calculator 함수 중에서 add와 mul만 불러오겠다는 의미, *(모든 함수)
print(add(2,5))
print(mul(3,3))