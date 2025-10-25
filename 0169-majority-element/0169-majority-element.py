class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def rec_majority(left, right):
            
            if left == right:
                return nums[left]
            mid = (left + right) // 2
            left_majority = rec_majority(left, mid)
            right_majority = rec_majority(mid + 1, right)
            
            if left_majority and right_majority:
                if left_majority == right_majority:
                    return left_majority
                else:
                    left_count, right_count = 0, 0
                    for i in range(left, right + 1):
                        if nums[i] == left_majority:
                            left_count += 1
                        elif nums[i] == right_majority:
                            right_count += 1
                    
                    if left_count > right_count:
                        return left_majority
                    elif left_count < right_count:
                        return right_majority
                    else:
                        return None
            
            return left_majority or right_majority
        return rec_majority(0, len(nums) - 1)
            
        