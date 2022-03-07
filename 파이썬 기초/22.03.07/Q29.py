def mask_security_number(security_number):
    new_l = list(security_number)
    new_str = ""
    for i in range(-4, 0):
        new_l[i] = '*'

    for i in range(0, len(new_l)):
        new_str += new_l[i]
    return new_str


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))