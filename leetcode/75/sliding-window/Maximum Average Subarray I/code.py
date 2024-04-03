class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        _max = -10000
        size:int = len(nums) 
        if(size == 1 and k==1):
            return nums[0]
        for i in range(size - k):
            _sum:int = 0
            for z in range(k+i, size):
                _div += nums[z]
            if(_div == 0):
                _div = 1
            result = _sum / _div

            if(_max < result):
                _max = result

            _rem+=nums[i]
        return _max