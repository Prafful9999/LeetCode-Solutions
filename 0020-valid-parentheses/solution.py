class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brackets={'(':')','[':']','{':'}'}
        for i in s:
            if i in brackets:
               stack.append(i)
            else:
                if not stack:
                    return False
                top=stack.pop()
                if brackets[top] !=i:
                    return False
        return not stack
                
        




        