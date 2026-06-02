class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                row_key = f"{value} in row {r}"
                col_key = f"{value} in col {c}"
                block_key = f"{value} in block {(r // 3) * 3 + (c // 3)}"

                if (
                    row_key in seen
                    or col_key in seen
                    or block_key in seen
                ):
                    return False

                seen.add(row_key)
                seen.add(col_key)
                seen.add(block_key)

        return True
