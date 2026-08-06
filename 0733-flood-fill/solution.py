class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        val=image[sr][sc]
        rows=len(image)
        cols=len(image[0])
        def solver(r,c):
            if r<0 or r>rows-1:
                return
            if c<0 or c>cols-1:
                return
            if image[r][c]==color:
                return
            if image[r][c]==val:
                image[r][c]=color
                solver(r,c-1)
                solver(r,c+1)
                solver(r+1,c)
                solver(r-1,c)
        solver(sr,sc)
        return image
        