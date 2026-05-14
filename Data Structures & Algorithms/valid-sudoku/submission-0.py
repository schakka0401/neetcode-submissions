class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for c in range(9):
            for r in range(9):
                value = board[r][c]
                if value == ".":
                    continue

                if value in row[r]: return False
                row[r].add(value)

                if value in col[c]: return False
                col[c].add(value)

                index_box = (r//3)*3 + (c//3)
                if value in box[index_box]: return False
                box[index_box].add(value)

        return True
        

       

   
