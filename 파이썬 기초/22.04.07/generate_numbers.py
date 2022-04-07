import random


def generate_numbers(n):
    nlist = []
    lotto_num = random.randint(1, 46)
    for i in range(0, n):
        while lotto_num in nlist:
            lotto_num = random.randint(1, 46)
        nlist.append(lotto_num)
    return nlist


print(generate_numbers(6))