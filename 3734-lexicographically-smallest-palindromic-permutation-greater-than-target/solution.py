class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Frequency count
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Palindrome possible hai ya nahi
        odd = 0
        mid = ''

        for i in range(26):
            if cnt[i] % 2:
                odd += 1
                mid = chr(i + ord('a'))

        if odd > 1:
            return ""

        # Left half ke liye counts
        half = [x // 2 for x in cnt]

        # Left half ko greedily build karenge
        left = []

        def possible():
            # Current prefix ke baad remaining ko
            # largest order me lagao
            temp = left[:]

            for i in range(25, -1, -1):
                temp += [chr(i + ord('a'))] * half[i]

            l = ''.join(temp)
            pal = l + mid + l[::-1]

            return pal > target

        for _ in range(n // 2):

            found = False

            # smallest possible character try karo
            for i in range(26):

                if half[i] == 0:
                    continue

                ch = chr(i + ord('a'))

                half[i] -= 1
                left.append(ch)

                if possible():
                    found = True
                    break

                # ye character kaam nahi karega
                left.pop()
                half[i] += 1

            if not found:
                return ""

        left = ''.join(left)

        ans = left + mid + left[::-1]

        return ans if ans > target else ""