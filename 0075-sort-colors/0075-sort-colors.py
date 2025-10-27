class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def mergeSort(start, end):
            if start >= end:
                return

            mid = (start + end) // 2
            mergeSort(start, mid)
            mergeSort(mid + 1, end)

            l = start
            r = mid + 1
            result = []

            while l <= mid and r <= end:
                if nums[l] <= nums[r]:
                    result.append(nums[l])
                    l += 1
                else:
                    result.append(nums[r])
                    r += 1
            
            while l <= mid:
                result.append(nums[l])
                l += 1
            while r <= end:
                result.append(nums[r])
                r += 1
            
            nums[start:end+1] = result

        mergeSort(0, len(nums) - 1)