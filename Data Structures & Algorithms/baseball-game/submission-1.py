class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_record = []
        total_score = 0

        for operation in operations:
            if operation == "+":
                score = score_record[-1] + score_record[-2]
                score_record.append(score)
                total_score += score
            elif operation == "D":
                score = 2 * score_record[-1]
                score_record.append(score)
                total_score += score
            elif operation == "C":
                total_score -= score_record.pop()
            else:
                score = int(operation)
                score_record.append(score)
                total_score += score

        return total_score
