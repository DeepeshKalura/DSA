from typing import List

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()

        possible_rewards = {0}

        for reward in rewardValues:
            current_rewards = list(possible_rewards)
            for x in current_rewards:
                if reward > x:
                    possible_rewards.add(x + reward)
        
        return max(possible_rewards)