from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            x_first = int(str(x) + str(y))
            y_first = int(str(y) + str(x))
            if x_first > y_first:
                return -1
            elif x_first == y_first:
                return 0
            else:
                return 1

        nums.sort(key = cmp_to_key(compare))

        return str(int("".join([str(n) for n in nums])))