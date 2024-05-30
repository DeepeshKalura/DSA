class Solution:
    def minimumDifference(self, nums, k):
        n = len(nums)
        md = float('inf')
        
        for i in range(n):
            ca = nums[i]
            md = min(md, abs(k - ca))
            
            if md == 0:
                return 0
            
            for j in range(i + 1, n):
                ca &= nums[j]
                md = min(md, abs(k - ca))
                
                if md == 0:
                    return 0
                
                if ca == 0:
                    break
                
        return md
    






