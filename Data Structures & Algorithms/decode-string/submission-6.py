import re


class Solution:
    def decodeString(self, s: str) -> str:
        innermost_pattern = re.compile(
            r"(?P<repeat_count>\d+)\[(?P<inner_string>[a-z]*)\]"
        )

        while "[" in s:
            s = innermost_pattern.sub(
                lambda match: int(match["repeat_count"]) * match["inner_string"], s
            )

        return s
