from typing import List

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()
        possible_rewards = {0}
        
        for reward in rewardValues:
            new_rewards = set()
            for x in possible_rewards:
                if reward > x:
                    new_rewards.add(x + reward)
            possible_rewards.update(new_rewards)
        
        return max(possible_rewards)
