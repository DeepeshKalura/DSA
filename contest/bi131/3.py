from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
            counts = {}
            good_pairs = 0
            max_num = max(nums1)

            for num in nums1:
                counts[num] = counts.get(num, 0) + 1

            for num in nums2:
                multiple = num * k
                while multiple <= max_num:
                    good_pairs += counts.get(multiple, 0)
                    multiple += num * k

            return good_pairs