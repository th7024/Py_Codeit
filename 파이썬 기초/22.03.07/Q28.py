# 자리수 합 리턴
def sum_digit(num):
    str_num = str(num)
    sum = 0
    for i in str_num:
        a = int(i)
        sum += a
    return sum
total = 0
for i in range(1,1001):
    n = sum_digit(i)
    total +=n
print(total)
# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 코드를 입력하세요.