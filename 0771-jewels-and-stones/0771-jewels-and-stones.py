from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        num_stones = Counter(stones)
        jewels_set = set(jewels)

        result = 0
        for key, value in num_stones.items():
            if key in jewels_set:
                result += value

        return result