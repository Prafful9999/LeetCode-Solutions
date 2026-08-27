class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        ans = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            # k se zyada 1 ho gaye
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            # starting ke unnecessary 0 hatao
            while ones == k and s[left] == '0':
                left += 1

            if ones == k:
                curr = s[left:right + 1]

                if ans == "":
                    ans = curr
                elif len(curr) < len(ans):
                    ans = curr
                elif len(curr) == len(ans) and curr < ans:
                    ans = curr

        return ans