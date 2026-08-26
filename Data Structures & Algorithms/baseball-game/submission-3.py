class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_record = deque()

        for operation in operations:
            match operation:
                case "+":
                    score_record.append(score_record[-1] + score_record[-2])
                case "D":
                    score_record.append(2 * score_record[-1])
                case "C":
                    score_record.pop()
                case _:
                    score_record.append(int(operation))

        return sum(score_record)
