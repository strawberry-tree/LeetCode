class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        curr = []

        # start번째 인덱스의 수부터 선택 가능
        def add_num(curr_sum, start):
            if curr_sum == target:
                answer.append(curr[:])
            
            if curr_sum > target:
                return

            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                add_num(curr_sum + candidates[i], i)
                curr.pop()

        add_num(0, 0)
        return answer