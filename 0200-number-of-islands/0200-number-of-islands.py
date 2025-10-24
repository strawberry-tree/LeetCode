from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])
        visited = [[False] * N for _ in range(M)] 
        
        def bfs(sx, sy):
            dx = [-1, 0, 1, 0]
            dy = [0, -1, 0, 1]

            queue= deque([(sx, sy)])
            visited[sx][sy] = True
            while queue:
                cx, cy = queue.popleft()
                for i in range(4):
                    nx, ny = cx + dx[i], cy + dy[i]
                    if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == "1":
                        queue.append((nx, ny))
                        visited[nx][ny] = True
        
        answer = 0
        for i in range(M):
            for j in range(N):
                if not visited[i][j] and grid[i][j] == "1":
                    answer += 1
                    bfs(i, j)

        return answer