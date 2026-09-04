class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            previous_length = len(s)

            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")

            if len(s) == previous_length:
                break

        return not s
