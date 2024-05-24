from typing import List
from collections import defaultdict

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        freq = defaultdict(int)
        for num in nums2:
            freq[num] += 1
        
        count = 0
        
        for num in nums1:
            required_divisor = num // k
            
            if num % k == 0 and required_divisor in freq:
                count += freq[required_divisor]
        
        return count
        



"""

You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.

A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).

Return the total number of good pairs.



You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.

A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).

Return the total number of good pairs.


"""