class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        open_brackets = []

        for bracket in s:
            match bracket:
                case "(" | "[" | "{":
                    open_brackets.append(bracket)
                case ")":
                    if not open_brackets or open_brackets.pop() != "(":
                        return False
                case "]":
                    if not open_brackets or open_brackets.pop() != "[":
                        return False
                case "}":
                    if not open_brackets or open_brackets.pop() != "{":
                        return False

        return not open_brackets
