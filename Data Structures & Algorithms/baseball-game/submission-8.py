class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_record = [0] * len(operations)
        record_size = 0

        for operation in operations:
            if operation == "C":
                record_size -= 1
                continue

            if operation == "+":
                score = score_record[record_size - 1] + score_record[record_size - 2]
            elif operation == "D":
                score = 2 * score_record[record_size - 1]
            else:
                score = int(operation)

            score_record[record_size] = score
            record_size += 1

        return sum(score_record[:record_size])
