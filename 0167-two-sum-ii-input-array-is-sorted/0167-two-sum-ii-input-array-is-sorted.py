

class Solution:
    

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bisearch(left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] < target:
                    left = mid + 1
                elif numbers[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1



        N = len(numbers)
        for i in range(N):
            first_num = numbers[i]
            second_num = target - first_num
            j = bisearch(i + 1, N - 1, second_num)
            if j != -1:
                return [i + 1, j + 1]

