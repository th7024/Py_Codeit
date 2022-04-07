import random


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


print(generate_numbers(6))
print(draw_winning_numbers())