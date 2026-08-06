class Solution:
    
    def checkValidString(self, s: str) -> bool:
        memo = {}
        
        def helper(ind, count):
            if (ind, count) in memo:
                return memo[(ind, count)]
            
            if ind == len(s):
                return count == 0
            
            if count < 0:
                return False
            
            if s[ind] == "(":
                ans = helper(ind+1, count+1)
            
            elif s[ind] == ")":
                ans = helper(ind+1, count-1)
            
            else:  # '*'
                ans = (helper(ind+1, count+1) or 
                       helper(ind+1, count-1) or 
                       helper(ind+1, count))
            
            memo[(ind, count)] = ans
            return ans
        
        return helper(0, 0)
        