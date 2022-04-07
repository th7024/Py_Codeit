import random

generate_list = []
lotto_list = []


def generate_numbers(n):
    nlist = []
    lotto_num = random.randint(1, 46)
    for i in range(0, n):
        while lotto_num in nlist:
            lotto_num = random.randint(1, 46)
        nlist.append(lotto_num)
    return nlist


def draw_winning_numbers():
    nlist = []
    lotto_num = random.randint(1, 46)
    for i in range(0, 7):
        while lotto_num in nlist:
            lotto_num = random.randint(1, 46)
        nlist.append(lotto_num)
    nlist.sort()

    lotto_num = random.randint(1, 46)
    while lotto_num in nlist:
        lotto_num = random.randint(1, 46)
    nlist.append(lotto_num)
    return nlist


def count_matching_numbers(list1, list2):
    set_list = []
    set_list = set(list1) & set(list2)
    return len(set_list)


def check(list1, list2):
    bonusN = int(list2[7]) #왜 7인지 모르겠음
    select_count = int(count_matching_numbers(list1, list2[0:6]))
    if select_count == 6:
        return 1000000000
    elif select_count == 5 and bonusN in list1:
        return 50000000
    elif select_count == 5:
        return 1000000
    elif select_count == 4:
        return 50000
    elif select_count == 3:
        return 5000
    else:
        return 0


generate_list = generate_numbers(6)
lotto_list = draw_winning_numbers()
print(check(generate_list, lotto_list))
