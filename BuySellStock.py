class Solution(object):
    def maxProfit(self,prices):
        if len(prices)==1 :
            return 0
        profit = []

        for i in range (1, len(prices)):
            profit.append(max(prices[i]-prices[i-1]))
        return sum(profit)
        

    