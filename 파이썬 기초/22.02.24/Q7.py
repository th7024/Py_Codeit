def calculate_change(payment, cost):
    number = payment - cost
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    cnt_4 = 0
    if number >= 50000:
        cnt_1 = number // 50000
        number = number % 50000

    if number >= 10000:
        cnt_2 = number // 10000
        number = number % 10000

    if number >= 5000:
        cnt_3 = number // 5000
        number = number % 5000

    if number >= 1000:
        cnt_4 = number // 1000
        number = number % 1000

    print("50000원 지폐: {}장".format(cnt_1))
    print("10000원 지폐: {}장".format(cnt_2))
    print("5000원 지폐: {}장".format(cnt_3))
    print("1000원 지폐: {}장".format(cnt_4))

# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)


def calculate_change(payment, cost):
    change = payment - cost  # 거스름돈 총액

    fifty_count = change // 50000  # 50,000원 지폐
    ten_count = (change % 50000) // 10000  # 10,000원 지폐
    five_count = (change % 10000) // 5000  # 5,000원 지폐
    one_count = (change % 5000) // 1000  # 1,000원 지폐

    # 답 출력
    print("50000원 지폐: {}장".format(fifty_count))
    print("10000원 지폐: {}장".format(ten_count))
    print("5000원 지폐: {}장".format(five_count))
    print("1000원 지폐: {}장".format(one_count))


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
