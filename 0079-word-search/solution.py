class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board),len(board[0])
        path = set()
        def helper(r,c,i):
            if r >= row or r < 0 or c >= col or c < 0 :
                # if (r,c) in path: path.remove((r,c))
                return False
            if board[r][c] != word[i] or (r,c) in path:
                # if (r,c) in path: path.remove((r,c))
                return False
            if i == len(word)-1:
                return True
            path.add((r,c))
            if helper(r+1,c,i+1) or helper(r,c+1,i+1) or helper(r-1,c,i+1) or helper(r,c-1,i+1):
                return True
            path.remove((r,c))
            
            return False
        for i in range(row):
            for j in range(col):
                if helper(i,j,0):
                    return True
        return False
                

        