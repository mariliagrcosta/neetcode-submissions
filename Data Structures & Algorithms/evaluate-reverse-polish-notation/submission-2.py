class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand_stack = [0] * len(tokens)
        top = -1

        for token in tokens:
            if token == "+":
                operand_stack[top - 1] += operand_stack[top]
                top -= 1
            elif token == "-":
                operand_stack[top - 1] -= operand_stack[top]
                top -= 1
            elif token == "*":
                operand_stack[top - 1] *= operand_stack[top]
                top -= 1
            elif token == "/":
                operand_stack[top - 1] = int(
                    operand_stack[top - 1] / operand_stack[top]
                )
                top -= 1
            else:
                top += 1
                operand_stack[top] = int(token)

        return operand_stack[top]
