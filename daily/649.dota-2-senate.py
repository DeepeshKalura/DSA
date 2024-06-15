#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#

# @lc code=start

from typing import List

class Solution:
    def toogleFunction(self, voter:str) -> str:
        if(voter == "R"):
            return "D"
        return "R"
    
    def checking(self, array:List[str]) -> bool:
        if(len(array) == 0):
            return False
        value = array[0]

        for i in range(1, len(array)):
            if(value != array[i]):
                return True 
            
        return False

    def predictPartyVictory(self, senate: str) -> str:
        array:List[str] = []
        for i in senate:
            array.append(i)

        hm = {
            "R": "Radiant",
            "D": "Dire"
        }
        while(self.checking(array)):
            value:str = array.pop(0)
            removingValue:str = self.toogleFunction(value)
            array.remove(removingValue)
            array.append(value)

        return hm[array[0]]

        
                


# @lc code=end

senate = "RRDDD"
print(Solution().predictPartyVictory(senate))

