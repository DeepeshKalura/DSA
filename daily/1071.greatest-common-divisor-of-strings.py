#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
class Solution:
    def gcd(self, nums1:int, nums2:int) -> int:
        answer = 1
        i:int = 2
        while(nums1 >= i):
            if(nums1 % i == 0 and nums2 % i == 0):
                answer = i
            i+=1        
        return answer

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        result = self.gcd(n, m)

        a:str= str1[:result]

        if(a*(n//result) == str1 and a*(m//result) == str2):
            return a
        else:
            return ""
        
        
# @lc code=end

