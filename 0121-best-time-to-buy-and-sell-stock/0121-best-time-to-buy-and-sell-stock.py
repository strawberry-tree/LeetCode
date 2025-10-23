class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        # prices의 i번째 인덱스 이후 값들 중 최댓값
        max_price = [0] * (N)
        for i in range(N - 2, -1, -1):
            max_price[i] = max(max_price[i + 1], prices[i + 1])
        
        # prices와 max_price 비교
        answer = 0
        for i in range(N - 1):
            answer = max(answer, max_price[i] - prices[i])
        
        return answer