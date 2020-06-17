"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
class Solution:
    def fill(self, i, j, board):
        if i==-1 or i==len(board):
            return
        if j==-1 or j==len(board[0]):
            return
        if board[i][j]=='O':
            board[i][j]=''
            self.fill(i-1, j, board)
            self.fill(i+1, j, board)
            self.fill(i, j-1, board)
            self.fill(i, j+1, board)
        
    
    def solve(self, board):
        if not board or not board[0]:
            return []
        
        M, N = len(board), len(board[0])
        for i in range(M):
            self.fill(i, 0, board)
            self.fill(i, N-1, board)
        for j in range(N):
            self.fill(0, j, board)
            self.fill(M-1, j, board)
        
        for i in range(M):
            for j in range(N):
                if board[i][j]=='':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
