class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])

        def search(sr, sc, ind):
            if ind == len(word):
                return True

        
            if sr < 0 or sc < 0 or sr >= rows or sc >= columns:
                return False
            if board[sr][sc] != word[ind]:
                return False

            
            temp = board[sr][sc]
            board[sr][sc] = "#"


            found = (
                search(sr, sc + 1, ind + 1) or
                search(sr, sc - 1, ind + 1) or
                search(sr + 1, sc, ind + 1) or
                search(sr - 1, sc, ind + 1)
            )

        
            board[sr][sc] = temp
            return found

        for i in range(rows):
            for j in range(columns):
                if board[i][j] == word[0]:
                    if search(i, j, 0):
                        return True

        return False
