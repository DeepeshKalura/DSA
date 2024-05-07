#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
from typing import  List
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Step 1: Check if grouping is possible
        if len(hand) % groupSize != 0:
            return False
        
        # Step 2: Count the occurrences of each card
        count = Counter(hand)
        
        # Step 3: Sort the unique card values
        sorted_keys = sorted(count.keys())
        
        # Step 4: Form consecutive groups
        for key in sorted_keys:
            if count[key] > 0:  # If this card is still available
                start_count = count[key]
                # Check and form a group starting from `key`
                for i in range(key, key + groupSize):
                    if count[i] < start_count:
                        return False
                    count[i] -= start_count
        
        # Step 5: Return True if all groups are formed successfully
        return True
        
        
# @lc code=end

hand = [6,7,4,5]
groupSize = 4

print(Solution().isNStraightHand(hand, groupSize))