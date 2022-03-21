lines = []
with open('data/chicken.txt', 'r', encoding='UTF-8') as f: #파일명, r(읽기), w(쓰기) as 변수명
    for line in f:
        lines.append(line.strip())
num = []
for i in range(1,len(lines)+1):
    num.append(int(lines[i-1].lstrip("{}일:".format(i))))
print(sum(num)/len(num))

""" 답안
with open('data/chicken.txt', 'r') as f:
    total_revenue = 0
    total_days = 0

    for line in f:
        data = line.strip().split(": ")
        revenue = int(data[1])  # 그날의 매출

    total_revenue += revenue
    total_days += 1

    print(total_revenue / total_days)
"""