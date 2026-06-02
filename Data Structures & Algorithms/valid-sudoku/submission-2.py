class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        blocks = [0] * 9

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                value_bit = 1 << (int(value) - 1)
                block_idx = (r // 3) * 3 + (c // 3)

                if (
                    (rows[r] & value_bit)
                    or (cols[c] & value_bit)
                    or (blocks[block_idx] & value_bit)
                ):
                    return False

                rows[r] |= value_bit
                cols[c] |= value_bit
                blocks[block_idx] |= value_bit

        return True
