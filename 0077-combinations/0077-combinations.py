from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        for cmb in combinations(range(1, n + 1), k):
            answer.append(list(cmb))

        return answer