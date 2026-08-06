class Solution:
    def frequencySort(self, s: str) -> str:
        freq = dict()
        for i in s:
            freq[i]=freq.get(i,0)+1
        sorted_dict={}
        for key in sorted(freq , key=freq.get, reverse=True):
            sorted_dict[key] = freq[key]
        string = ""
        for i in sorted_dict:
            string+= i*freq[i]
        return string
            
        


        
        