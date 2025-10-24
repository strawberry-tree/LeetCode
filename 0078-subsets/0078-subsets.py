class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        curr = []
        answer = []

        def pick_num(start):
            if start >= N:
                answer.append(curr[:])
                return

            # start 이후 인덱스의 숫자를 고르거나
            for i in range(start, N):
                curr.append(nums[i])
                pick_num(i + 1)
                curr.pop()
            
            # 더 이상 고르지 않기
            pick_num(N)
        
        pick_num(0)
        return answer