class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand_stack = []

        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                operand_stack.append(int(token))
                continue

            right_operand = operand_stack.pop()
            left_operand = operand_stack.pop()

            if token == "+":
                result = left_operand + right_operand
            elif token == "-":
                result = left_operand - right_operand
            elif token == "*":
                result = left_operand * right_operand
            else:
                result = int(left_operand / right_operand)

            operand_stack.append(result)

        return operand_stack.pop()
