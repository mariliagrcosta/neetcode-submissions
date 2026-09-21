import operator


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand_stack = []
        apply_operator = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda left, right: int(left / right),
        }

        for token in tokens:
            if token not in apply_operator:
                operand_stack.append(int(token))
                continue

            right_operand = operand_stack.pop()
            left_operand = operand_stack.pop()

            operand_stack.append(
                apply_operator[token](left_operand, right_operand)
            )

        return operand_stack.pop()
