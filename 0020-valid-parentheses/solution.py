class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brackets={'(':')','[':']','{':'}'}
        for i in s:
            if len(stack)>0:
                if i==brackets[stack[-1]]:
                    stack.pop()
                else:
                    if i==')' or i==']' or i=='}':
                        return False
                    else:
                        stack.append(i)
            else:
                if i==')' or i==']' or i=='}':
                    return False
                else:
                   stack.append(i)
        if len(stack)==0:
            return True
        else:
            return False
            