class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        val=image[sr][sc]
        rows=len(image)
        cols=len(image[0])
        def dfs(r,c):
            if r<0 or r>rows-1 or c<0 or c>cols-1:
                return 
            if image[r][c]==color:
                return
            if image[r][c]==val:
                image[r][c]=color
                dfs(r,c-1)
                dfs(r,c+1)
                dfs(r-1,c)
                dfs(r+1,c)
        dfs(sr,sc)
        return image
        