class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        open_brackets = []

        for bracket in s:
            if bracket in "([{":
                open_brackets.append(bracket)
            elif bracket == ")":
                if not open_brackets or open_brackets.pop() != "(":
                    return False
            elif bracket == "]":
                if not open_brackets or open_brackets.pop() != "[":
                    return False
            elif bracket == "}":
                if not open_brackets or open_brackets.pop() != "{":
                    return False

        return not open_brackets
