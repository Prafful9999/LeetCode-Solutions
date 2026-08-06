class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        n=len(word)
        substr=[]
        for i in range(n):
            for j in range(i+1,n+1):
                substr.append(word[i:j])
        
        count=0
        for i in patterns:
            if i in substr:
                count+=1
        return count

        