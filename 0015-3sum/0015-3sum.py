class Solution:


    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # key: 숫자값, value: 해당값 마지막 인덱스
        nums.sort()

        sum_dict = dict()
        for i, value in enumerate(nums):
            sum_dict[value] = i

        N = len(nums)
        answer = []
        for i in range(N - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, N - 1):
                rest = 0 - (nums[i] + nums[j])
                
                if rest in sum_dict and j < sum_dict[rest]:
                    answer.append((nums[i], nums[j], rest))

        answer = [list(tup) for tup in set(answer)]
        return answer