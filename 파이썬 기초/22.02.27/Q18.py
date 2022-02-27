# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    i = 0
    while i < len(prices):
        prices[i] = prices[i] / 1000
        i += 1


# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    i = 0
    while i < len(prices):
        prices[i] = prices[i] * 125
        i += 1


# 원화(￦)으로 각각 얼마인가요?
prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))

# prices를 원화(￦)에서 달러($)로 변환하기
krw_to_usd(prices)

# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(prices))

# prices를 달러($)에서 엔화(￥)으로 변환하기
usd_to_jpy(prices)

# 엔화(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(prices))