class Solution:
    def pivotIndex(self, nums ) -> int:
        # nums = [1,7,3,6,5,6]
        # output = 3
        # cs = [1, 8, 11, 17, 22, 28]
        cs = [nums[0]] # cummulative_sum
        pe = 0 # pivot_element
        for i in range(1, len(nums)):
            cs.append(cs[i-1]+nums[i])
        print(cs)
        _ls = 0 # left_sum
        for i in range(len(nums)):
            _rs = cs[-1] - nums[i]  - _ls # right_sum

            if(_rs == _ls):
                return i
            _ls += nums[i]

        return -1
            
sol = Solution()
nums = [1,7,3,6,5,6]
print(sol.pivotIndex(nums))