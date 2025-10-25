class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)

        # 해당 인덱스의 값을 subarray의 마지막 값으로 취급
        dp = [0] * (N)
        for i in range(N):
            if i == 0 or dp[i - 1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]
        
        print(dp)
        return max(dp)