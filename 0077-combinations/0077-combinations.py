class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        # start 이상부터 고를 수 있음. 현재 고른 숫자는 curr에 있음
        
        def pick(start, curr):
            if len(curr) >= k:
                answer.append(curr[:])
                return

            if start > n:
                return
            
            for i in range(start, n + 1):
                pick(i + 1, curr + [i])

        pick(1, [])
        return answer