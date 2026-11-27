from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
  
        for i in range(9):
            hashRow = {}
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in hashRow:
                    return False
                hashRow[val] = 1

        for i in range(9):
            hashColumn = {}
            for j in range(9):
                val = board[j][i]
                if val == ".":
                    continue
                if val in hashColumn:
                    return False
                hashColumn[val] = 1

        for i in range(9):
            hash3 = {}
            for j in range(3):
                for k in range(3):
                    row = (i // 3) * 3 + j
                    col = (i % 3) * 3 + k
                    val = board[row][col]
                    if val == ".":
                        continue
                    if val in hash3:
                        return False
                    hash3[val] = 1

        return True