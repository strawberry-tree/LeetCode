from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # 그래프 - key: bi, value: ai
        graph = defaultdict(list)
        
        # ai를 수강하기 위해 수강해야 하는 선수과목 수
        indegrees = defaultdict(int)

        for ai, bi in prerequisites:
            graph[bi].append(ai)
            indegrees[ai] += 1

        # 바로 들을 수 있는 수업만 큐에 추가
        queue = deque([])
        result = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        while queue:
            # 수업 수강하기
            curr = queue.popleft()
            result.append(curr)
        
            for adj in graph[curr]:
                indegrees[adj] -= 1
                if indegrees[adj] == 0:
                    queue.append(adj)

        # 모든수업 수강가능?
        return len(result) == numCourses