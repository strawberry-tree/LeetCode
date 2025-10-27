# 최대 k번만?
# 몇번 건넜는지도 저장해야되나

from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        price = [[float('inf')] * (k + 2) for _ in range(n)]
        price[src][0] = 0
        queue = []
        heapq.heappush(queue, (0, src, 0))   # 가격, 인덱스번호, 건넌 다리 수

        for from_i, to_i, price_i in flights:
            graph[from_i].append((to_i, price_i))

        while queue:
            curr_price, curr_idx, curr_stops = heapq.heappop(queue)
            if curr_stops >= k + 1:
                continue

            for adj_idx, adj_price in graph[curr_idx]:
                new_price = curr_price + adj_price
                if curr_stops + 1 <= k + 1 and new_price < price[adj_idx][curr_stops + 1]:
                    price[adj_idx][curr_stops + 1] = new_price
                    heapq.heappush(queue, (new_price, adj_idx, curr_stops + 1))
        

        result = min(price[dst])
        if result >= float('inf'):
            return -1
        return result

        
