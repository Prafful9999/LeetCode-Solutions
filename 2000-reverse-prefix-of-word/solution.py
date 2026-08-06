class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)  # safer than index(), avoids ValueError
        if i == -1:
            return word
        return word[:i+1][::-1] + word[i+1:]
