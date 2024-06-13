#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        print(path)
        for i in path:
            if (i == ".."):
                try :
                    stack.pop()
                    stack.pop()
                except:
                    continue

            elif (i == "."):
                continue

            elif (i != ""):
                stack.append("/")
                stack.append(i)
        if(stack):
            return "".join(stack)
        return "/"
        
# @lc code=end


path = "/a/../../b/../c//.//"
print(Solution().simplifyPath(path))

# a little improvement comes in my answer afer seeing a good solution
# but i think it can be done with regular expression to 