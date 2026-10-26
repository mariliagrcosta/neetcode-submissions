class Solution:
    def decodeString(self, s: str) -> str:
        while "[" in s:
            closing_index = s.index("]")
            opening_index = s.rindex("[", 0, closing_index)

            repeat_start = opening_index
            while repeat_start > 0 and s[repeat_start - 1].isdigit():
                repeat_start -= 1

            repeat_count = int(s[repeat_start:opening_index])
            expanded_string = s[opening_index + 1 : closing_index] * repeat_count
            s = s[:repeat_start] + expanded_string + s[closing_index + 1 :]

        return s
