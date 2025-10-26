class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        # i번째 인덱스까지 누적곱 ([1, 2, 6, 24])
        pre = [1] * N

        # i번째 인덱스부터 누적곱 ([0, 24, 12, 4])
        post = [1] * N

        for i in range(N):
            if i == 0:
                pre[i] = nums[i]
                post[N - i - 1] = nums[N - i - 1]
            else:
                pre[i] = pre[i - 1] * nums[i]
                post[N - i - 1] = post[N - i] * nums[N - i - 1]   

        answer = []
        # print(pre, post)
        for i in range(N): 
            if i == 0:
                answer.append(post[i + 1])
            elif i == N - 1:
                answer.append(pre[i - 1])  
            else:
                answer.append(post[i + 1] * pre[i - 1])
        
        return answer