class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        n=len(words)
        stri=""
        for i in words:
            total=0
            for j in i:
                total+=weights[ord(j)-97]
            stri+=chr(122-total%26)
        return stri
            
                
        