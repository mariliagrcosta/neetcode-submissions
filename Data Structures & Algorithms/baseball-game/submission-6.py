class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record_size = 0

        for operation in operations:
            if operation == "C":
                record_size -= 1
                continue

            if operation == "+":
                operations[record_size] = operations[record_size - 1] + operations[record_size - 2]
            elif operation == "D":
                operations[record_size] = 2 * operations[record_size - 1]
            else:
                operations[record_size] = int(operation)

            record_size += 1

        return sum(operations[:record_size])
