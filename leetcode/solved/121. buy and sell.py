#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

prices = [1,2,4,6,8,9,1,2,3,4,6,9,1,1,2,301,4]
profit = 0
buy = prices[0]

for i in range(1, len(prices)):
    if buy > prices[i]:
        buy = prices[i]
    a = (prices[i] - buy)
    if profit < a:
        profit = a

print(profit)