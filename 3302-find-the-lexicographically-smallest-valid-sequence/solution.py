class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:

        last = [-1] * len(word2)
        n = len(word1)
        j = len(word2) - 1

        while j >= 0:

            # next character ki position ke left mein hi search karo
            if j == len(word2) - 1:
                start = n - 1
            else:
                start = last[j + 1] - 1

            for i in range(start, -1, -1):
                if word1[i] == word2[j]:
                    last[j] = i
                    break

            j -= 1

        ans = []
        j = 0
        changed = False

        for i in range(len(word1)):

            if j == len(word2):
                return ans

            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            elif changed == False:

                if j == len(word2) - 1 or last[j + 1] > i:
                    ans.append(i)
                    changed = True
                    j += 1

        if j == len(word2):
            return ans

        return []