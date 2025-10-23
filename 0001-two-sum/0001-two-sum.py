class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_nums = set(nums)

        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in set_nums:
                for j in range(i + 1, len(nums)):
                    if nums[j] == rest:
                        return [i, j]
