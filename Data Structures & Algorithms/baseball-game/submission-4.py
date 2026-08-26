class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_record = deque()
        total_score = 0

        for operation in operations:
            match operation:
                case "+":
                    score = score_record[-1] + score_record[-2]
                    score_record.append(score)
                    total_score += score
                case "D":
                    score = 2 * score_record[-1]
                    score_record.append(score)
                    total_score += score
                case "C":
                    total_score -= score_record.pop()
                case _:
                    score = int(operation)
                    score_record.append(score)
                    total_score += score

        return total_score
