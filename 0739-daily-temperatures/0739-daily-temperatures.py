# [(73, 0)]
# [(74, 1)] -> 0에 1 대입
# [(75, 2)] -> 1에 1 대입
# [(75, 2) (71, 3)]
# [(75, 2) (71, 3) (69, 4)]
# [(75, 2) (72, 5)] -> 3에 2 대입, 4에 1 대입...
# [(76, 6)] -> 2에 4 대입, 5에 1 대입
# [(76, 6) (73, 7)]
# 나머지 칸은 0으로 놔두기

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, p_idx = stack.pop()
                answer[p_idx] = i - p_idx   # 이만큼이나 기다려야 됐음
            stack.append((temp, i))

        return answer