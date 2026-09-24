class Node:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Build
        head = Node(tokens[0])
        current = head

        for i in range(1, len(tokens)):
            current.next = Node(tokens[i], previous=current)
            current = current.next

        # Evaluate
        current = head

        while current is not None:
            if current.value in ("+", "-", "*", "/"):
                left_operand = int(current.previous.previous.value)
                right_operand = int(current.previous.value)

                if current.value == "+":
                    result = left_operand + right_operand
                elif current.value == "-":
                    result = left_operand - right_operand
                elif current.value == "*":
                    result = left_operand * right_operand
                else:
                    result = int(left_operand / right_operand)

                current.value = str(result)
                current.previous = current.previous.previous.previous

                if current.previous is not None:
                    current.previous.next = current

            answer = int(current.value)
            current = current.next

        return answer
