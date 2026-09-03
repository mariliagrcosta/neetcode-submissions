class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            remaining_brackets = []
            index = 0

            while index < len(s):
                if index + 1 < len(s) and s[index : index + 2] in ("()", "[]", "{}"):
                    index += 2
                else:
                    remaining_brackets.append(s[index])
                    index += 1

            if len(remaining_brackets) == len(s):
                break

            s = "".join(remaining_brackets)

        return not s
