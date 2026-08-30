class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        open_brackets = []
        matching_brackets = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        for bracket in s:
            if bracket in matching_brackets:
                if not open_brackets or open_brackets[-1] != matching_brackets[bracket]:
                    return False
                open_brackets.pop()
            else:
                open_brackets.append(bracket)

        return not open_brackets
