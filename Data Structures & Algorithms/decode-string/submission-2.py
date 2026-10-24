class Solution:
    def decodeString(self, s: str) -> str:
        def decode(start: int) -> tuple[str, int]:
            decoded_parts = []
            current_count = 0
            index = start

            while index < len(s):
                character = s[index]

                if character.isdigit():
                    current_count = current_count * 10 + int(character)
                elif character == "[":
                    inner_string, index = decode(index + 1)
                    decoded_parts.append(inner_string * current_count)
                    current_count = 0
                elif character == "]":
                    return "".join(decoded_parts), index
                else:
                    decoded_parts.append(character)

                index += 1

            return "".join(decoded_parts), index

        decoded_string, _ = decode(0)

        return decoded_string
