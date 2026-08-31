class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        expected_brackets = []

        for bracket in s:
            if bracket == "(":
                expected_brackets.append(")")
            elif bracket == "[":
                expected_brackets.append("]")
            elif bracket == "{":
                expected_brackets.append("}")
            elif not expected_brackets or expected_brackets.pop() != bracket:
                return False

        return not expected_brackets
