class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        i:int = 0
        while (i < len(s)):
            if("("==s[i]):
                stack.append("(")
                i+=1

            elif(")"==s[i] ):
                try:
                        stack.pop()
                        i+=1
                except:
                        s = s[:i] + s[i+1:]
            else:
                i+=1
            
        
        stack_size:int = len(stack)
        string_size:int = len(s)
        while(stack_size > 0):
            i:int = string_size-1
            if(s[i] == "("):
                s = s[:i] + s[i+1:]
                stack_size-=1
            
            string_size-=1
        return s
            

        
sol = Solution()
print(sol.minRemoveToMakeValid("))(("))
