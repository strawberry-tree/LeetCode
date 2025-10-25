class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []

        # i일, i+1일의 주가 비교
        # i+1 > i일인 경우 바로 구매
        for i in range(len(prices) - 1):
            profits.append(prices[i + 1] - prices[i])

        return sum(p for p in profits if p > 0)
        
        