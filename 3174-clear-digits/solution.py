class Solution:
    def clearDigits(self, s: str) -> str:
        stk = []
        for c in s:
            if c.isdigit():
                stk.pop()            # remove the closest letter to the left
            else:
                stk.append(c)        # keep non-digit characters
        return "".join(stk)
