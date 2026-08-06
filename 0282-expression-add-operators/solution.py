class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        n = len(num)

        def helper(ind, st, total, prev):
            if ind == n:
                if total == target:
                    ans.append(st)
                return

            for i in range(ind, n):

                if i > ind and num[ind] == '0':
                    break

                curr = int(num[ind:i+1])

                if ind == 0:
                    helper(i+1, num[ind:i+1], curr, curr)
                else:
                    helper(i+1, st + "+" + num[ind:i+1],
                           total + curr, curr)

                    helper(i+1, st + "-" + num[ind:i+1],
                           total - curr, -curr)

                    helper(i+1, st + "*" + num[ind:i+1],
                           total - prev + prev * curr,
                           prev * curr)

        helper(0, "", 0, 0)
        return ans

        
                    


        