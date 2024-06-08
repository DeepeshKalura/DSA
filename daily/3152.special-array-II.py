from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        result:List[bool] = []
        for query in queries:
            er  = True
            mr:str = "none"
            if(nums[query[0]] % 2 == 0):
                mr = "even"
            else:
                mr = "odd"
            for i in range(query[0] +1 , query[1] + 1):
                if(nums[i] % 2 == 0 ):
                    if (mr == "even"):
                        result.append(False)
                        er = False
                        break
                    
                    mr = "even"
                else:
                    
                    if (mr == "odd"):
                        result.append(False)
                        er = False
                        break

                    mr = "odd"
            if(er):
                result.append(True)


        return result
    



nums = [4,3,1,6]

queries = [[0,2], [2, 3]]

sol = Solution()

print(sol.isArraySpecial(nums, queries))