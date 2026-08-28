class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record_size = 0
        total_score = 0

        for operation in operations:
            if operation == "C":
                record_size -= 1
                total_score -= operations[record_size]
                continue

            if operation == "+":
                score = operations[record_size - 1] + operations[record_size - 2]
            elif operation == "D":
                score = 2 * operations[record_size - 1]
            else:
                score = int(operation)

            operations[record_size] = score
            total_score += score
            record_size += 1

        return total_score
