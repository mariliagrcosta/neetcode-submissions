class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_record = []

        for operation in operations:
            if operation == "+":
                score_record.append(score_record[-1] + score_record[-2])
            elif operation == "D":
                score_record.append(2 * score_record[-1])
            elif operation == "C":
                score_record.pop()
            else:
                score_record.append(int(operation))

        return sum(score_record)
