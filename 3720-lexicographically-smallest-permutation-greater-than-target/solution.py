class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # frequency of characters in s
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # right se left jaayenge
        for i in range(n - 1, -1, -1):

            # target[0:i] ko exactly match karne ke liye
            temp = cnt.copy()

            possible = True

            for j in range(i):
                x = ord(target[j]) - ord('a')
                temp[x] -= 1

                if temp[x] < 0:
                    possible = False
                    break

            if not possible:
                continue

            # position i par target[i] se bada character dhundo
            x = ord(target[i]) - ord('a')

            bigger = -1

            for c in range(x + 1, 26):
                if temp[c] > 0:
                    bigger = c
                    break

            if bigger == -1:
                continue

            # target[0:i] + bigger character
            ans = target[:i] + chr(bigger + ord('a'))

            temp[bigger] -= 1

            # baaki characters smallest order me
            for c in range(26):
                ans += chr(c + ord('a')) * temp[c]

            return ans

        return ""