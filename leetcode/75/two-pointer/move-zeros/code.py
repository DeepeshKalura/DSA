class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # firstly i will find zero are where
        for i in range(len(nums)):
            if(nums[i]==0):
                nums.pop(i)
                nums.append(0)
            

            
        
        
