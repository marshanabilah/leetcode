from typing import List

def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0

        for index, value in enumerate(prices):
            profit = value - buy

            if value < buy:
                buy = value

            if profit > maxProfit:
                maxProfit = profit
                print(maxProfit)

        return maxProfit