def count_matching_numbers(list1, list2):
    set_list = []
    set_list = set(list1) & set(list2)
    return len(set_list)

def check(list1, list2):
    bonusN = int(list2[6])
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

# 테스트
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))