import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [dict() for x in range(9)]
        col = [dict() for x in range(9)]
        box = [dict() for x in range(9)]

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                box_i = math.floor(i/3)*3 + math.floor(j/3)

                if value == '.':
                    continue

                if value in row[i].keys() or value in col[j].keys() or value in box[box_i].keys():
                    return False
                else:
                    row[i][value] = True
                    col[j][value] = True
                    box[box_i][value] = True

        return True
                

        