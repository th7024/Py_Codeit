year = 2022
month = 2
day = 14

print("오늘은 " + str(year)+"년 " + str(month)+ "월 " + str(day)+ "일입니다.")
print("오늘은 {}년 {}월 {}일입니다.".format(year,month,day))
date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year,month,day+1))