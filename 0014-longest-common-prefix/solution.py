class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        test=strs[0]
        for i in range(1,len(strs)):
            ind=-1
            for j ,k in zip(strs[i],test):
                if j==k:
                    ind+=1
                else:
                    break
            test=strs[0][0:ind+1]
        return test
                


        

        