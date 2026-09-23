class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        index = len(tokens) - 1

        def evaluate() -> int:
            nonlocal index
            token = tokens[index]
            index -= 1

            if token not in ("+", "-", "*", "/"):
                return int(token)

            right_operand = evaluate()
            left_operand = evaluate()

            if token == "+":
                return left_operand + right_operand
            elif token == "-":
                return left_operand - right_operand
            elif token == "*":
                return left_operand * right_operand
            else:
                return int(left_operand / right_operand)

        return evaluate()
