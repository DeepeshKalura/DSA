class Solution:
    def maxArea(self, height: List[int]) -> int:
        i:int = 0
        j:int = len(height) - 1
        _max:int = 0
        while(i<j):
            cal = 0
            if(height[i] < height[j]):
                cal = height[i] * (j-i)
                i+=1
            else:
                cal = height[j] * (j-i)
                j-=1
            if(cal > _max):
                _max = cal
            
        return _max
        