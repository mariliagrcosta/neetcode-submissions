class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                if value == ".":
                    continue

                block_idx = (r // 3) * 3 + (c // 3)

                if (
                    value in rows[r]
                    or value in cols[c]
                    or value in blocks[block_idx]
                ):
                    return False

                rows[r].add(value)
                cols[c].add(value)
                blocks[block_idx].add(value)

        return True
