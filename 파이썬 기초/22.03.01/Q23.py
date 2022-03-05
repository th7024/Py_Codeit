for b in range(1,400):
    for a in range(1,b):
        c = 400 - (a + b)
        if c*c==a*a+b*b and a < b < c:
            print(a*b*c)
            break