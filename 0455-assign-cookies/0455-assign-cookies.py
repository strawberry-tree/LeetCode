class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort(reverse=True)
        g.sort(reverse=True)

        j = 0   # 몇번째 쿠키?

        # 몇 명의 아이들에게 나눠줄 수 있지?
        for i in range(len(g)):
            # 쿠키가 다 떨어진 경우
            if j >= len(s):
                break
            if s[j] >= g[i]:
                j += 1
        
        return j