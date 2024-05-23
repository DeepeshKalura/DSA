from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        i:int = 0 
        count:int = 0
        current_val = 1
        while(i < len(board)):
            array = board[i]
            store = {}
            for j in range(len(array)):
                if(array[j] != -1 ):
                    p = 0
                    if(i % 2 == 0):
                        p = i*6 + j
                    else:
                        p = i*6 + 6 - j
                    
                    store[p] = array[j]
            
            # logic issue hai yaha
            if(store == {}):
                count+=1
                current_val += 6
            else:
                for pos , val in store.items():
                    if(pos > current_val):
                        count+=1
                        current_val = val 
                    else:
                        count+=2
                        current_val = val

            
            i = current_val // len(board)
        

        return count
 

board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
print(Solution().snakesAndLadders(board))