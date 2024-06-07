from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        if k == 0:
            max_length = 1
            current_length = 1
            for i in range(1, n):
                if nums[i] == nums[i - 1]:
                    current_length += 1
                    max_length = max(max_length, current_length)
                else:
                    current_length = 1
            return max_length
        
        start = 0
        max_length = 0
        current_changes = 0
        en = nums
        
        for end in range(1, len(en)):
            if en[end] != en[end - 1]:
                current_changes += 1
                
            while current_changes > k:
                if en[start] != en[start + 1]:
                    current_changes -= 1
                start += 1
                
            max_length = max(max_length, end - start + 1)
        
        return max_length

# Example usage
nums = [19, 2, 19, 13]
k = 0
print(Solution().maximumLength(nums, k))  # Expected output: 2
