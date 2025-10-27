class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1


        while left <= right:
            mid = (left + right) // 2
            first_val = nums[left]
            last_val = nums[right]

            if nums[mid] == target:
                return mid

            # 우측 정렬, 좌측 정렬X
            elif nums[mid] < last_val:
                if nums[mid] < target <= last_val:
                    left = mid + 1
                else:
                    right = mid - 1
                
            # 좌측 정렬, 우측 정렬X
            else:
                if first_val <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1