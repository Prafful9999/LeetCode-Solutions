class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        
        for ch in s:
            if ch.isalnum():          # sirf letters aur digits
                filtered += ch.lower()
        
        return filtered == filtered[::-1]

        