from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for pm in permutations(nums):
            answer.append(list(pm))

        return answer