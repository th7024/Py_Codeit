# 표준 라이브러리(다양한 모듈이 있는것) 파이썬을 설치하면 딸려옴
import math
#math
print(math.log(100))
print(math.cos(0))
print(math.pi)#변수 파이

#random
import random
print(random.random())
#randint 함수
#randint는 두 수 사이의 어떤 랜덤한 정수를 리턴하는 함수입니다.
#randint(a, b)를 하면, a ≤ N ≤ b를 만족하는 어떤 랜덤한 정수 N을 리턴하는 것이죠.
print(random.randint(1, 20))
print(random.randint(1, 20))
#uniform은 두 수 사이의 랜덤한 소수를 리턴하는 함수입니다.
# randint와 다른 것은 리턴하는 값이 정수가 아니라 소수라는 점입니다.
#uniform(a, b)를 하면, a ≤ N ≤ b를 만족하는 어떤 랜덤한 소수 N을 리턴하는 것이죠.
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))

#os
import os
print(os.getlogin()) #로그인 되어있는 계정 알아보기
print(os.getcwd()) #경로 알아보기

#datetime
import datetime
pi_day = datetime.datetime(2022, 3, 8,21,55,30) #시간 설정
print(pi_day)
print(type(pi_day))
#오늘 날짜 받아오기
today = datetime.datetime.now()
print(today)
print(type(today))
#timedelta
#두 datetime 값 사이의 기간을 알고 싶으면, 마치 숫자 뺄셈을 하듯이 그냥 빼면 됩니다.
today = datetime.datetime.now()
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(today - pi_day)
print(type(today - pi_day))

today = datetime.datetime.now()
print(today)
print(today.year)  # 연도
print(today.month)  # 월
print(today.day)  # 일
print(today.hour)  # 시
print(today.minute)  # 분
print(today.second)  # 초
print(today.microsecond)  # 마이크로초

#datetime 포맷팅
#datetime 값을 출력하면 별로 예쁘지 않습니다. 하지만 strftime을 사용하면, 우리 입맛대로 바꿀 수 있습니다.

today = datetime.datetime.now()

print(today)
print(today.strftime("%A, %B %dth %Y"))