class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_ht=0
        ht=0
        for i in gain:
            ht+=i
            max_ht=max(max_ht,ht)
        return max_ht

        