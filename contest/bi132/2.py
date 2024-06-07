from typing import List
from collections import deque

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:

        n = len(skills)
        queue = deque(range(n))
        win_count = 0
        winner = queue.popleft()

        while win_count < k:
            if (win_count > n):
                break
            player = queue.popleft()
            if skills[player] > skills[winner]:
                queue.append(winner)
                winner = player
                win_count = 1
            else:
                queue.append(player)
                win_count += 1

    

        return winner

        # while(win_count < k):
        #     player = queue.popleft()
        #     if(skills[player] > skills[winner]):
        #         skills.append(winner)
        #         winner = player
        #         win_count+=1
            
        #     else:
        #         queue.append(player)
        #         win_count += 1
        #     queue.append(winner)

        # return winner


nums = [16, 4, 7, 17]
# [4,2,6,3,9]
k = 562084119
# 2

print(Solution().findWinningPlayer(nums, k))
# [2,5,4]
# 3
# [7,11]
# 2
# [16,4,7,17]
# 562084119