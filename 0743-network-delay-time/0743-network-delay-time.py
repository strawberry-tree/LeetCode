from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    
        # 연결리스트 구성
        graph = defaultdict(list)

        for source, target, time in times:
            graph[source].append((target, time))

        # 다익스트라 알고리즘
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        queue = []
        heapq.heappush(queue, (0, k))

        while queue:
            cost, curr = heapq.heappop(queue)
            if cost > dist[curr]:
                continue
            for adj, adj_cost in graph[curr]:
                new_cost = cost + adj_cost
                if new_cost < dist[adj]:
                    dist[adj] = new_cost
                    heapq.heappush(queue, (new_cost, adj))
        

        result = max(dist[1:])
        if result >= float('inf'):
            return -1
        return result