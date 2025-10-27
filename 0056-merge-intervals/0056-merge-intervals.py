from collections import deque

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        queue = deque()
        intervals.sort()
        for start, end in intervals:
            if queue and queue[-1][1] >= start:
                queue[-1][1] = max(end, queue[-1][1])
            else:
                queue.append([start, end])

        return list(queue)
                


        