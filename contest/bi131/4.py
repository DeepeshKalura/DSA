from typing import List

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        result: List[bool] = []
        obtacle = set()

        for query in queries:
            if query[0] == 1:
                obtacle.add(query[1])
            else:
                sz = query[2]

                # logic to check obstacle in given range and append in result

                


